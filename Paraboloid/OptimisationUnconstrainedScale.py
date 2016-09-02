__author__ = 'sebasanper'
from openmdao.main.api import Assembly
from openmdao.lib.drivers.api import SLSQPdriver
from Paraboloid_scaled_shift import ParaboloidScaledShift


class OptimizationUnconstrainedScale(Assembly):
    """Unconstrained optimization of the Paraboloid Component."""

    def configure(self):
        # Create Optimizer instance
        self.add('driver', SLSQPdriver())

        # Create Paraboloid component instances
        self.add('paraboloid', ParaboloidScaledShift())

        # Iteration Hierarchy
        self.driver.workflow.add('paraboloid')

        # SLSQP Flags
        self.driver.iprint = 1

        # Objective
        self.driver.add_objective('paraboloid.f_xy')

        # Design Variables
        # self.driver.add_parameter('paraboloid.x', low=-1000., high=1000.)
        # self.driver.add_parameter('paraboloid.y', low=-10000, high=1000.)

        # self.driver.add_parameter('paraboloid.x', low=-1000., high=1000., scaler=0.001)
        # self.driver.add_parameter('paraboloid.y', low=-1000., high=1000., scaler=1000.0)

        self.driver.add_parameter('paraboloid.x', low=-1000000., high=1000000., scaler=0.001)
        self.driver.add_parameter('paraboloid.y', low=-1000000., high=1000000., scaler=1000.0, adder=-1000.0)

if __name__ == "__main__":
    opt_problem = OptimizationUnconstrainedScale()

    import time

    tt = time.time()

    opt_problem.run()

    print "\n"
    print "Minimum found at (%f, %f)" % (opt_problem.paraboloid.x, \
                                         opt_problem.paraboloid.y)
    print "Elapsed time: ", time.time() - tt, "seconds"
    print "Execution count: ", opt_problem.paraboloid.exec_count