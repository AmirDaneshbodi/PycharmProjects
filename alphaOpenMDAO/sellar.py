# For printing, use this import if you are running Python 2.x
from __future__ import print_function

import numpy as np

from openmdao.core.component import Component


class SellarDis1(Component):
    """Component containing Discipline 1."""

    def __init__(self):
        super(SellarDis1, self).__init__()

        # Global Design Variable
        self.add_param('z', shape=2)

        # Local Design Variable
        self.add_param('x', val=0.0)

        # Coupling parameter
        self.add_param('y2', val=1.0)

        # Coupling output
        self.add_output('y1', val=1.0)

    def solve_nonlinear(self, params, unknowns, resids):
        """Evaluates the equation
        y1 = z1**2 + z2 + x1 - 0.2*y2"""

        z1 = params['z'][0]
        z2 = params['z'][1]
        x1 = params['x']
        y2 = params['y2']

        unknowns['y1'] = z1 ** 2 + z2 + x1 - 0.2 * y2

    def jacobian(self, params, unknowns, resids):
        """ Jacobian for Sellar discipline 1."""

        J = {('y1', 'y2'): - 0.2, ('y1', 'z'): np.array([[2 * params['z'][0], 1.0]]), ('y1', 'x'): 1.0}

        return J


class SellarDis2(Component):
    """Component containing Discipline 2."""

    def __init__(self):
        super(SellarDis2, self).__init__()

        # Global Design Variable
        self.add_param('z', val=np.zeros(2))

        # Coupling parameter
        self.add_param('y1', val=1.0)

        # Coupling output
        self.add_output('y2', val=1.0)

    def solve_nonlinear(self, params, unknowns, resids):
        """Evaluates the equation
        y2 = y1**(.5) + z1 + z2"""

        z1 = params['z'][0]
        z2 = params['z'][1]
        y1 = params['y1']

        # Note: this may cause some issues. However, y1 is constrained to be
        # above 3.16, so lets just let it converge, and the optimizer will
        # throw it out
        y1 = abs(y1)

        unknowns['y2'] = y1 ** .5 + z1 + z2

    def jacobian(self, params, unknowns, resids):
        """ Jacobian for Sellar discipline 2."""
        J = {}

        J['y2', 'y1'] = .5 * params['y1'] ** -.5
        J['y2', 'z'] = np.array([[1.0, 1.0]])

        return J

class StateConnection(Component):
    """ Define connection with an explicit equation"""

    def __init__(self):
        super(StateConnection, self).__init__()

        # Inputs
        self.add_param('y2_actual', 1.0)

        # States
        self.add_state('y2_command', val=1.0)

    def apply_nonlinear(self, params, unknowns, resids):
        """ Don't solve; just calculate the residual."""

        y2_actual = params['y2_actual']
        y2_command = unknowns['y2_command']

        resids['y2_command'] = y2_actual - y2_command

    def solve_nonlinear(self, params, unknowns, resids):
        """ This is a dummy comp that doesn't modify its state."""
        pass

    def jacobian(self, params, unknowns, resids):
        """Analytical derivatives."""

        J = {}

        # State equation
        J[('y2_command', 'y2_command')] = -1.0
        J[('y2_command', 'y2_actual')] = 1.0

        return J