from math import exp, sqrt, cos, pi, e


def auckley(x, y):
    return - 20.0 * exp(- 0.2 * sqrt(0.5 * (x ** 2.0 + y ** 2.0))) - exp(
        0.5 * (cos(2.0 * pi * x) + cos(2.0 * pi * y))) + e + 20.0


def auckley3(x, y):
    return - 20.0 * exp(- 0.2 * sqrt(0.5 * (x ** 2.0 + y ** 2.0))) + e / 2.0 + 20.0


output = open('auckley_modified.dat', 'w')
for i in range(100):
    output.write("{0:f}\t{1:f}\t{2:f}\n".format(- 5.0 + 0.1 * i, auckley(- 5.0 + 0.1 * i, 0.0), auckley3(- 5.0 + 0.1 * i, 0.0)))

output.close()
