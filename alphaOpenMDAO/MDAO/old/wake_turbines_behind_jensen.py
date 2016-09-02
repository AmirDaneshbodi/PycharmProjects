from openmdao.api import Component
from math import radians, tan, sin, sqrt, cos


class TurbinesInWakeJensen(Component):
    def __init__(self):
        super(TurbinesInWakeJensen, self).__init__()

        self.add_param('upstream', shape=2)
        self.add_param('layout_x')
        self.add_param('layout_y')
        self.add_param('layout_ordered_x')
        self.add_param('layout_ordered_y')
        self.add_param('wind_angle', val=0.0)
        self.add_param('k', val=0.0)
        self.add_param('r0', val=0.0)
        self.add_output('downstream_distances')

    def solve_nonlinear(self, params, unknowns, resids):

        xt = params['upstream'][0]
        yt = params['upstream'][1]
        r0 = params['r0']
        k = params['k']
        in_wake = []

        for tur in range(len(params['layout_x'])):

            xw = params['layout_x'][params['layout_ordered_x'][tur][1]]
            yw = params['layout_y'][params['layout_ordered_y'][tur][1]]
            alpha = radians(self.params['wind_angle'] + 180.0)
            X_int = (xw + tan(alpha) * yw + tan(alpha) * (tan(alpha) * xt - yt)) / (tan(alpha) ** 2.0 + 1.0)
            Y_int = (- tan(alpha) * (- xw - tan(alpha) * yw) - tan(alpha) * xt + yt) / (tan(alpha) ** 2.0 + 1.0)
            distance_to_centre = abs(- tan(alpha) * xw + yw + tan(alpha) * xt - yt) / sqrt(1.0 + tan(alpha) ** 2.0)
            distance_to_turbine = sqrt((X_int - xt) ** 2.0 + (Y_int - yt) ** 2.0)
            radius = r0 + k * distance_to_turbine

            if (xw - xt) * cos(alpha) + (yw - yt) * sin(alpha) <= 0.0:
                if abs(radius) >= abs(distance_to_centre):
                    in_wake.append((distance_to_turbine, params['layout_ordered_x'][tur][1]))

        unknowns['downstream_list_distances'] = in_wake
