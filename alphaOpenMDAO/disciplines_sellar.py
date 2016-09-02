from scipy.optimize import fsolve
from numpy import polyfit as fit
from math import exp

x1 = 1.0
z1 = 5.0
z2 = 2.0


def dis1(z1, z2, x1, y2):
    return z1 ** 2.0 + z2 + x1 - 0.2 * y2


def dis2(z1, z2, y1):
    return y1 ** 0.5 + z1 + z2


def equations(p):
    y1, y2 = p
    return (z1 ** 2.0 + z2 + x1 - 0.2 * y2) - y1, (y1 ** 0.5 + z1 + z2) - y2


def objective(y1, y2):
    return x1 ** 2.0 + z2 + y1 + exp(- y2)


y1, y2 = fsolve(equations, (1.0, 1.0))
print(y1, y2)
print(objective(y1, y2))

if __name__ == '__main__':
    # out = open('simple.dat', 'w')
    # x1 = 1.0
    # for i in range(20):
    #         z1 = 2.5 + i * 0.1
    #     for j in range(20):
    #         z2 = 0.1 + j * 0.1
    #         y1, y2 = fsolve(equations, (1.0, 1.0))
    #         out.write('{0:f}\t{1:f}\t{2:f}\n'.format(z1, z2, objective(y1, y2)))
    #     out.write('\n')
    # out.close()

    for i in range(4):
        z1 = 0. + i * 0.8
        z1s = '{:1.1f}'.format(z1)
        for j in range(4):
            z2 = 0. + j * 0.8
            z2s = '{:1.1f}'.format(z2)
            for k in range(4):
                y2 = 0. + k * 0.8
                y2s = '{:1.1f}'.format(y2)
                filename = 'sens_y2x1_dis1_z1_' + z1s + '_z2_' + z2s + '_y2_' + y2s + '.dat'
                out2 = open(filename, 'w')
                x1 = []
                ans = []
                for l in range(10):
                    x1.append(0. + l * 0.8)
                    ans.append(dis1(z1, z2, x1[-1], y2))
                    out2.write('{0:f}\t{1:f}\n'.format(x1[-1], ans[-1]))
                    # print(y2, ans)
                print('{0:f}\t{1:f}\t{2:f}\t{3:f}\t{4:s}\n'.format(z1, z2, y2, x1[-1], fit(x1, ans, 1)))
                out2.close()


