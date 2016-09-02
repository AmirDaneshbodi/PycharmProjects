from openmdao.api import Component


class Ct(Component):
    def __init__(self):
        super(Ct, self).__init__()

        self.add_param('U_total')
        self.add_output('CT')

    def solve_nonlinear(self, params, unknowns, resids):

        u0 = params['U_total']
        if u0 < 4.0:
            ct = 0.1

        elif u0 <= 25.0:
            ct = 7.3139922126945e-7 * u0 ** 6.0 - 6.68905596915255e-5 * u0 ** 5.0 + 2.3937885e-3 * u0 ** 4.0 - 0.0420283143 * u0 ** 3.0 + 0.3716111285 * u0 ** 2.0 - 1.5686969749 * u0 + 3.2991094727

        else:
            ct = 0.1

        unknowns['CT'] = ct

    def linearize(self, params, unknowns, resids):
        J = {}
        u0 = params['U_total']

        if u0 < 4.0:
            dct = 0.0
        elif u0 <= 25.0:
            dct = 6.0 * 7.3139922126945e-7 * u0 ** 5.0 - 5.0 * 6.68905596915255e-5 * u0 ** 4.0 + 4.0 * 2.3937885e-3 * u0 ** 3.0 - 3.0 * 0.0420283143 * u0 ** 2.0 + 2.0 * 0.3716111285 * u0 - 1.5686969749
        else:
            dct = 0.0
        J['CT', 'U_total'] = dct


if __name__ == '__main__':
    pass
