from random import randint
from numpy import mean, var
from time import time


def counted(fn):
    def wrapper(*args, **kwargs):
        wrapper.called += 1
        return fn(*args, **kwargs)
    wrapper.called = 0
    wrapper.__name__ = fn.__name__
    return wrapper


def sobol(number):
    start = time()

    # memo = {}
    # @counted
    # def f(x, y, z):
    #     if not (x, y, z) in memo:
    #         memo[(x, y, z)] = fl(x, y, z)
    #     return memo[(x, y, z)]

    # @counted
    def f(x, y, z):
        return x + y * z ** 2.0

    m = number

    x1 = [float(randint(1, 1000)) for _ in range(m)]
    x2 = [float(randint(1, 100)) for __ in range(m)]
    x3 = [float(randint(1, 10)) for ___ in range(m)]

    Y = [f(x1[i], x2[i], x3[i]) for i in range(m)]

    v = var(Y)
    v1 = var([mean([f(x1[i], x2[o], x3[o]) for o in range(m)]) for i in range(m)])
    v2 = var([mean([f(x1[o], x2[i], x3[o]) for o in range(m)]) for i in range(m)])
    v3 = var([mean([f(x1[o], x2[o], x3[i]) for o in range(m)]) for i in range(m)])
    v12 = var([mean([f(x1[i], x2[i], x3[o]) for o in range(m)]) for i in range(m)]) - v1 - v2
    v13 = var([mean([f(x1[i], x2[o], x3[i]) for o in range(m)]) for i in range(m)]) - v1 - v3
    v23 = var([mean([f(x1[o], x2[i], x3[i]) for o in range(m)]) for i in range(m)]) - v2 - v3

    t1 = 1.0 - var([mean([f(x1[i], x2[o], x3[o]) for i in range(m)]) for o in range(m)]) / v
    t2 = 1.0 - var([mean([f(x1[o], x2[i], x3[o]) for i in range(m)]) for o in range(m)]) / v
    t3 = 1.0 - var([mean([f(x1[o], x2[o], x3[i]) for i in range(m)]) for o in range(m)]) / v

    print t1, t2, t3, t1 + t2 + t3
    #
    s1 = v1 / v
    # print s1
    s2 = v2 / v
    # print s2
    s3 = v3 / v
    # print s3
    s12 = v12 / v
    # print s12
    s13 = v13 / v
    # print s13
    s23 = v23 / v
    # print s23
    # print '------sum----------'
    # print s1 + s2 + s3 + s12 + s13 + s23
    # print
    # print '-----------time in seconds--------------'
    # print time() - start
    return s1, s2, s3, s12, s13, s23, s1 + s2 + s3 + s12 + s13 + s23, time() - start#, fl.called, f.called

if __name__ == '__main__':
    print sobol(1600)
    # out = open('sobol.dat', 'a', 5)
    # out.write('#MCnumber\ts1    \ts2      \ts3      \ts12      \ts13      \ts23      \tsum      \ttime\n')
    # for mc in range(1000, 2000):
    #     a = sobol(mc)
    #     out.write('{8:d}    \t{0:f}\t{1:f}\t{2:f}\t{3:f}\t{4:f}\t{5:f}\t{6:f}\t{7:f}\n'.format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], mc))
    #     print(str((float(mc) - 1000.0) * 100.0 / (2000.0 - 1000.0)) + '%\n')
    # out.close()
