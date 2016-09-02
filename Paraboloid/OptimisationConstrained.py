__author__ = 'sebasanper'
from openmdao.main.api import Assembly
from openmdao.lib.drivers.api import SLSQPdriver
from Paraboloid import Paraboloid


class OptimizationConstrained(Assembly):
    """Unconstrained optimization of the Paraboloid Component."""

    def configure(self):
        # Create Optimizer instance
        self.add('driver', SLSQPdriver())

        # Create Paraboloid component instances
        self.add('paraboloid', Paraboloid())

        # Iteration Hierarchy
        self.driver.workflow.add('paraboloid')

        # SLSQP Flags
        self.driver.iprint = 3

        # Objective
        self.driver.add_objective('paraboloid.f_xy')

        # Design Variables
        self.driver.add_parameter('paraboloid.x', low=-50., high=50.)
        self.driver.add_parameter('paraboloid.y', low=-50., high=50.)

        # Constraints
        self.driver.add_constraint('paraboloid.x-paraboloid.y >= 15.0')

if __name__ == "__main__":
    opt_problem = OptimizationConstrained()

    import time

    tt = time.time()

    opt_problem.run()

    print "\n"
    print "Minimum found at (%f, %f)" % (opt_problem.paraboloid.x, \
                                         opt_problem.paraboloid.y)
    print "Elapsed time: ", time.time() - tt, "seconds"
    print "Execution count: ", opt_problem.paraboloid.exec_count
    print "Derivatives count: ", opt_problem.paraboloid.derivative_exec_count