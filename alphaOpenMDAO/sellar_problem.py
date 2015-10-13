from openmdao.components.execcomp import ExecComp
from openmdao.components.paramcomp import ParamComp
from openmdao.core.group import Group
from openmdao.solvers.nl_gauss_seidel import NLGaussSeidel
from sellar import SellarDis1, SellarDis2, StateConnection
import numpy as np
from openmdao.core.problem import Problem
from openmdao.drivers.scipy_optimizer import ScipyOptimizer
from openmdao.solvers.newton import Newton

class SellarStateConnection(Group):
    """ Group containing the Sellar MDA. This version uses the disciplines
    with derivatives."""

    def __init__(self):
        super(SellarStateConnection, self).__init__()

        self.add('px', ParamComp('x', 1.0), promotes=['*'])
        self.add('pz', ParamComp('z', np.array([5.0, 2.0])), promotes=['*'])

        self.add('state_eq', StateConnection())
        self.add('d1', SellarDis1(), promotes=['x', 'z', 'y1'])
        self.add('d2', SellarDis2(), promotes=['z', 'y1'])
        self.connect('state_eq.y2_command', 'd1.y2')
        self.connect('d2.y2', 'state_eq.y2_actual')

        self.add('obj_cmp', ExecComp('obj = x**2 + z[1] + y1 + exp(-y2)',
                                     z=np.array([0.0, 0.0]), x=0.0, y1=0.0, y2=0.0),
                  promotes=['x', 'z', 'y1', 'obj'])
        self.connect('d2.y2', 'obj_cmp.y2')

        self.add('con_cmp1', ExecComp('con1 = 3.16 - y1'), promotes=['*'])
        self.add('con_cmp2', ExecComp('con2 = y2 - 24.0'), promotes=['con2'])
        self.connect('d2.y2', 'con_cmp2.y2')

        self.nl_solver = Newton()

class SellarDerivatives(Group):
    """ Group containing the Sellar MDA. This version uses the disciplines
    with derivatives."""

    def __init__(self):
        super(SellarDerivatives, self).__init__()

        self.add('px', ParamComp('x', 1.0), promotes=['*'])
        self.add('pz', ParamComp('z', np.array([5.0, 2.0])), promotes=['*'])

        self.add('d1', SellarDis1(), promotes=['*'])
        self.add('d2', SellarDis2(), promotes=['*'])

        self.add('obj_cmp', ExecComp('obj = x**2 + z[1] + y1 + exp(-y2)',
                                     z=np.array([0.0, 0.0]), x=0.0, y1=0.0, y2=0.0),
                 promotes=['*'])

        self.add('con_cmp1', ExecComp('con1 = 3.16 - y1'), promotes=['*'])
        self.add('con_cmp2', ExecComp('con2 = y2 - 24.0'), promotes=['*'])

        self.nl_solver = NLGaussSeidel()  # Non linear solver
        self.nl_solver.options['atol'] = 1.0e-12

if __name__ == '__main__':

    top = Problem()
    # top.root = SellarDerivatives()
    top.root = SellarStateConnection()

    top.driver = ScipyOptimizer()
    top.driver.options['optimizer'] = 'SLSQP'
    top.driver.options['tol'] = 1.0e-8

    top.driver.add_param('z', low=np.array([-10.0, 0.0]),
                         high=np.array([10.0, 10.0]))
    top.driver.add_param('x', low=0.0, high=10.0)

    top.driver.add_objective('obj')
    top.driver.add_constraint('con1')
    top.driver.add_constraint('con2')

    top.setup()
    top.run()

    print("\n")
    print( "Minimum found at (%f, %f, %f)" % (top['z'][0], top['z'][1], top['x']))
    # print("Coupling vars: %f, %f" % (top['y1'], top['y2']))
    print("Coupling vars: %f, %f" % (top['y1'], top['d2.y2']))
    print("Minimum objective: ", top['obj'])