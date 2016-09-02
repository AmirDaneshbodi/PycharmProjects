from openmdao.api import Component
from math import pi, tan
self.add_param('b')

        self.add_param('Dp1')
        self.add_output('w1')


class Moment(Component):
    def __init__(self):
        super(Moment, self).__init__()
        self.add_param('np')
        self.add_output('M')
    def solve_nonlinear(self, params, unknowns, resids):
        P = 10000.0
        unknowns['M'] = 60.0 * 10 ** 6.0 * P / (2.0 * pi * params['np'])


class RadialLoad(Component):
    def __init__(self):
        super(RadialLoad, self).__init__()
        self.add_param('m')
        self.add_param('z')
        self.add_param('M')
        self.add_output('Fr')

    def solve_nonlinear(self, params, unknowns, resids):
        a = 20
        unknowns['Fr'] = 2.0 * params['M'] * tan(a) / (params['m'] * params['z'])

class GearWeight(Component):
    def __init__(self):
        super(GearWeight, self).__init__()
        self.add_param('d1')
        self.add_param()

    def solve_nonlinear(self, params, unknowns, resids):
        pass
