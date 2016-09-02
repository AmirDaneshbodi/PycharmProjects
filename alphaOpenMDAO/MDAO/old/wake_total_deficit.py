from openmdao.api import Component
from math import sqrt


class TotalDeficit(Component):
    def __init__(self):
        super(TotalDeficit, self).__init__()

        self.add_param('U_ij')
        self.add_param('U_inf')
        self.add_output('U_total', val=0.0)

    def solve_nonlinear(self, params, unknowns, resids):

        u_ij = params['U_ij']
        sum_squares = 0.0
        for tur in range(len(u_ij)):
            sum_squares += u_ij[tur] ** 2.0
        total_deficit = sqrt(sum_squares)
        unknowns['U_total'] = params['U_inf'] * (1.0 - total_deficit)
