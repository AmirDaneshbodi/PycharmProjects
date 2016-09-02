__author__ = 'sebasanper'
from openmdao.main.api import Assembly
from openmdao.lib.drivers.api import *
from pyopt_driver.pyopt_driver import pyOptDriver
from crease import *
from pyOpt.pySLSQP.pySLSQP import SLSQP


class CreaseOptimizationUnconstrained(Assembly):
    """Unconstrained optimization of the Paraboloid Component."""

    def configure(self):
        # Create Optimizer instance
        self.add('driver', pyOptDriver())

        # Create Paraboloid component instances
        self.add('one', one())

        # Iteration Hierarchy
        self.driver.workflow.add('one')

        # SLSQP Flags
        self.driver.iprint = 2

        # Objective
        self.driver.add_objective('one.f')

        # Design Variables
        self.driver.add_parameter('one.x', low=3.5, high=50.5)
        # self.driver.add_parameter('one.y', low=1.0, high=500.)
        # Constraints
        # self.driver.add_constraint('3.0*one.x**2.0*one.y>=50.0')
        # self.driver.add_constraint('3.0*one.x**2.0*one.y<=50.0')

        # self.driver.gradient_options.fd_form = 'forward'
        # self.driver.xmax = 0.000000000001
        self.driver.optimizer = 'ALPSO'

if __name__ == "__main__":
    opt_problem = CreaseOptimizationUnconstrained()

    import time

    tt = time.time()

    opt_problem.run()

    print "\n"
    print "Minimum found at (%f)" % (opt_problem.one.x)
    print "Elapsed time: ", time.time() - tt, "seconds"