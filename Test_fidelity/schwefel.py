from math import sin, sqrt, fabs


def schwefel(x, n):
    a = 0.0
    for i in range(n):
        a += x[i] * sin(sqrt(fabs(x[i])))
    return 418.9829 * n * a

output = open('schwefel.dat', 'w')
for x in range(100):
    for y in range(100):
        output.write('{0:d}\t{1:d}\t{2:f}\n'.format(x * 10 - 500, y * 10 - 500, schwefel([x * 10 - 500, y * 10 - 500], 2)))
    output.write('\n')
output.close()