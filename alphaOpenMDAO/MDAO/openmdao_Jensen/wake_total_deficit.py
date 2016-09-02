from math import sqrt
from openmdao.api import Component


class TotalWindSpeed(Component):
    def __init__(self):
        super(TotalWindSpeed, self).__init__()

        self.add_param('u_ij')
        self.add_param('U_inf')
        self.add_output('U_total')

    def solve_nonlinear(self, params, unknowns, resids):

        sum_squares = 0.0

        for tur in range(len(params['u_ij'])):
            sum_squares += params['u_ij'][tur] ** 2.0

        total_deficit = sqrt(sum_squares)

        unknowns['U_total'] = params['U_inf'] * (1.0 - total_deficit)

if __name__ == '__main__':
    pass
