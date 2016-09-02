from math import radians, cos, sqrt, sin
from openmdao.api import Component


class OrderLayout(Component):
    def __init__(self):
        super(OrderLayout, self).__init__()

        self.add_param('layout_x')
        self.add_param('layout_y')
        self.add_param('wind_angle')
        self.add_output('ordered_x')
        self.add_output('ordered_y')
        self.add_output('indices')

    def solve_nonlinear(self, params, unknowns, resids):

        x = params['layout_x']
        y = params['layout_y']
        wind_angle = params['wind_angle']
        ordered = []

        for tur in range(len(x)):
            ordered.append([distance_to_front(x[tur], y[tur], wind_angle), tur])

        ordered.sort()

        unknowns['indices'] = [ordered[i][1] for i in range(len(ordered))]
        unknowns['ordered_x'] = [x[i] for i in range(len(ordered))]
        unknowns['ordered_y'] = [y[i] for i in range(len(ordered))]


def distance_to_front(x, y, angle):

    theta = 90.0 - angle
    thetar = radians(theta)
    a = sin(thetar)
    b = - cos(thetar)

    return (a * x - b * y) / sqrt(a ** 2.0 + b ** 2.0)


if __name__ == '__main__':
    pass

