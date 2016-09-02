from math import sin, pi


def michalewicz(x, n, m):
    a = 0.0
    for i in range(n):
        a += sin(x[i]) * (sin(float(i + 1) * (x[i] ** 2.0) / pi)) ** (2.0 * m)
    return - a

output = open('michalewicz_m10.dat', 'w')
for x in range(100):
    for y in range(100):
        output.write('{0:f}\t{1:f}\t{2:f}\n'.format(x * 0.06 - 3.0, y * 0.06 - 3.0, michalewicz([x * 0.06 - 3.0, y * 0.06 - 3.0], 2, 10.0)))
    output.write('\n')
output.close()