from math import exp, sqrt, cos, pi, e


def goldstein(x, y):
    return (1.0 + ((x + y + 1) ** 2.0) * (
    19.0 - 14.0 * x + 3.0 * x ** 2.0 - 14.0 * y + 6.0 * x * y + 3.0 * y ** 2.0)) * (30.0 + ((
    (2.0 * x - 3.0 * y) ** 2.0) * (18.0 - 32.0 * x + 12.0 * x ** 2.0 + 48.0 * y - 36.0 * x * y + 27.0 * y ** 2.0)))


def goldstein2(x, y):
    return (1.0 + ((x + y + 1) ** 2.0) * (
    19.0 - 14.0 * x + 3.0 * x ** 2.0 - 14.0 * y + 6.0 * x * y + 3.0 * y ** 2.0)) * (30.0 + ((
    (2.0 * x - 3.0 * y) ** 2.0) * (18.0 - 32.0 * x + 12.0 * x ** 2.0)))


def goldstein3(x, y):
    return (1.0 + ((x + y + 1) ** 2.0) * (
    19.0 - 14.0 * x + 3.0 * x ** 2.0 - 14.0 * y + 6.0 * x * y + 3.0 * y ** 2.0)) * (30.0 + ((
    (2.0 * x - 3.0 * y) ** 2.0) * (12.0 * x ** 2.0 + 48.0 * y - 36.0 * x * y + 27.0 * y ** 2.0)))


def goldstein4(x, y):
    return (1.0 + ((x + y + 1) ** 2.0) * (
    19.0 - 14.0 * x + 3.0 * x ** 2.0 - 14.0 * y + 6.0 * x * y + 3.0 * y ** 2.0)) * (30.0 + ((
    (2.0 * x - 3.0 * y) ** 2.0) * (18.0 - 32.0 * x + 12.0 * x ** 2.0 + 48.0 * y - 36.0 * x * y + 27.0 * y ** 2.0)))

y = 1.0
output = open('goldstein_modified.dat', 'w')
for i in range(100):
    output.write("{0:f}\t{1:f}\t{2:f}\t{3:f}\t{4:f}\n".format(- 1.0 + 0.04 * i, goldstein(- 1.0 + 0.04 * i, y), goldstein2(- 1.0 + 0.04 * i, y), goldstein3(- 1.0 + 0.04 * i, y), goldstein4(- 1.0 + 0.04 * i, y)))

output.close()
