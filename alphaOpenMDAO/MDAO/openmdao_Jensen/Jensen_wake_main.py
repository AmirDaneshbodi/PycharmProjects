from openmdao.api import Component
from wake_layout_order import order_layout
from wake_turbines_behind_jensen import turbines_in_wakes_jensen

from old.wake_deficit_Jensen import deficit_jensen


class Jensen(Component):
    def __init__(self):
        super(Jensen, self).__init__()

        self.add_param('ordered_x')
        self.add_param('ordered_y')
        self.add_output('wind_speeds')

    def solve_nonlinear(self, params, unknowns, resids):

        indices, layout_ordered_x, layout_ordered_y = order_layout(params['farm'], params['angle'])
        u_ij = [[] for _ in range(len(layout_ordered_x))]
        wind_speed = []
        for num in range(len(layout_ordered_x)):

            wind_speed.append(total_wind_speed(u_ij[num], params['u_inf']))
            downstream = turbines_in_wakes_jensen(indices, layout_ordered_x, layout_ordered_y, layout_ordered_x[num],
                                                  layout_ordered_y[num], params['angle'], params['r0'], params['k'])
            deficits = deficit_jensen(downstream, params['CT'], params['k'], params['r0'])
            for i in range(0, len(deficits)):
                u_ij[deficits[i][1]].append(deficits[i][0])

        unknowns['wind_speeds'] = wind_speed


if __name__ == '__main__':
    pass
