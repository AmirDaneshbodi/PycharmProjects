from random import randint
from numpy import array
from time import time
start = time()


def f(x, y, z):
    return x + y * z ** 2.0


def expected(x):
    a = 0
    for j in range(len(x)):
        a += x[j]
    return a / float(len(x))


def variance(x):
    mean = expected(x)
    g = [(x[z] - mean) ** 2.0 for z in range(len(x))]
    return expected(g)

m = 100

x1 = array([randint(1, 1000) for _ in range(m)])
x2 = array([randint(1, 100) for __ in range(m)])
x3 = array([randint(1, 10) for ___ in range(m)])

Y = array([f(x1[i], x2[i], x3[i]) for i in range(m)])


def Y_X1(o):
    return array([f(x1[o], x2[i], x3[i]) for i in range(m)])


def Y_X2(o):
    return array([f(x1[i], x2[o], x3[i]) for i in range(m)])


def Y_X3(o):
    return array([f(x1[i], x2[i], x3[o]) for i in range(m)])


def Y_X1X2(o, oo):
    return array([f(x1[o], x2[oo], x3[i]) for i in range(m)])


def Y_X1X3(o, oo):
    return array([f(x1[o], x2[i], x3[oo]) for i in range(m)])


def Y_X2X3(o, oo):
    return array([f(x1[i], x2[o], x3[oo]) for i in range(m)])

v = variance(Y)
v1 = variance([expected(Y_X1(p)) for p in range(m)])
v2 = variance([expected(Y_X2(p)) for p in range(m)])
v3 = variance([expected(Y_X3(p)) for p in range(m)])
v12 = variance([expected(Y_X1X2(p, u)) for p in range(m) for u in range(m)]) - v1 - v2
v13 = variance([expected(Y_X1X3(p, u)) for p in range(m) for u in range(m)]) - v1 - v3
v23 = variance([expected(Y_X2X3(p, u)) for p in range(m) for u in range(m)]) - v2 - v3


s1 = v1 / v
print s1
s2 = v2 / v
print s2
s3 = v3 / v
print s3
s12 = v12 / v
print s12
s13 = v13 / v
print s13
s23 = v23 / v
print s23
print '------sum----------'
print s1 + s2 + s3 + s12 + s13 + s23

print '-----------time in seconds--------------'
print time() - start
