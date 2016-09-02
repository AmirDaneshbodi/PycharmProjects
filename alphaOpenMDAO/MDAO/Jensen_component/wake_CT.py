from openmdao.api import Component


def ct_poly(U_total):

    U0 = U_total

    if U0 < 4.0:
        ct = 0.1

    elif U0 <= 25.0:
        ct = 7.3139922126945e-7 * U0 ** 6.0 - 6.68905596915255e-5 * U0 ** 5.0 + 2.3937885e-3 * U0 ** 4.0 - 0.0420283143 * U0 ** 3.0 + 0.3716111285 * U0 ** 2.0 - 1.5686969749 * U0 + 3.2991094727

    else:
        ct = 0.1

    return ct


def ct_constant(U_total):
    return 8.0 / 9.0

if __name__ == '__main__':
    print(ct_poly(7.5))