from openmdao.api import Component
from math import sqrt


class DeficitJensen(Component):

    def __init__(self):
        super(DeficitJensen, self).__init__()
        self.add_param('downstream_list_distances')
        self.add_param('CT', val=0.0)
        self.add_param('k')
        self.add_param('r')
        self.add_output('deficits_list')

    def solve_nonlinear(self, params, unknowns, resids):

        deficits = []
        Ct = params['CT']
        k = params['k']
        r0 = params['r']

        for tur in range(len(params['downstream_list_distances'])):

            deficits.append(
                (1.0 - sqrt(1.0 - Ct)) / (1.0 + (k * params['downstream_list_distances'][tur][1]) / r0) ** 2.0)

        unknowns['deficits_list'] = deficits
