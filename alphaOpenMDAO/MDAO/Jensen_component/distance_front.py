from openmdao.api import Component
from math import radians, sin, cos, sqrt


class DistanceToFront(Component):

    def __init__(self):
        super(DistanceToFront, self).__init__()

        self.add_param('x')
        self.add_param('y')
        self.add_param('angle')
        self.add_output('distance')

    def solve_nonlinear(self, params, unknowns, resids):

        angle = params['angle']
        x = params['x']
        y = params['y']

        theta = 90.0 - angle
        thetar = radians(theta)
        a = sin(thetar)
        b = - cos(thetar)

        unknowns['distance'] = (a * x - b * y) / sqrt(a ** 2.0 + b ** 2.0)
