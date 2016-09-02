from openmdao.api import Component


class CtPoly(Component):

    def __init__(self):
        super(CtPoly, self).__init__()

        self.add_param('U_total', val=0.0)
        self.add_output('CT', val=0.0)

    def solve_nonlinear(self, params, unknowns, resids):
        U0 = params['U_total']
        if U0 < 4.0:
            ct = 0.1
        elif U0 <= 25.0:
            ct = 7.3139922126945e-7 * U0 ** 6.0 - 6.68905596915255e-5 * U0 ** 5.0 + 2.3937885e-3 * U0 ** 4.0 - 0.0420283143 * U0 ** 3.0 + 0.3716111285 * U0 ** 2.0 - 1.5686969749 * U0 + 3.2991094727
        else:
            ct = 0.1

        unknowns['CT'] = ct

    def linearize(self, params, unknowns, resids):
        J = {}
        U0 = params['U_total']
        if U0 < 4.0:
            dct = 0.0
        elif U0 <= 25.0:
            dct = 6.0 * 7.3139922126945e-7 * U0 ** 5.0 - 5.0 * 6.68905596915255e-5 * U0 ** 4.0 + 4.0 * 2.3937885e-3 * U0 ** 3.0 - 3.0 * 0.0420283143 * U0 ** 2.0 + 2.0 * 0.3716111285 * U0 - 1.5686969749
        else:
            dct = 0.0
        J['CT', 'U_total'] = dct
