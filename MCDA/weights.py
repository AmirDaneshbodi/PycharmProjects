__author__ = 'sebasanper'
from random import random
files=open('sensitivity.dat', 'w')
# m0 = [40., 280., 1., 100.]
m0 = [0., 1., 0., 0.5]
# m1 = [50., 240., 10., 102.]
m1 = [0.25, 0.25, 1., 0.]
# m2 = [60., 200., 5., 101.]
m2 = [1., 0., 0.1, 0.4]
l00 = l10 = l20 = l01 = l11 = l21 = l02 = l12 = l22 = 0.0
n = 1000000.0
n1 = int(n)
w = [0.0 for o in range(4)]
for x in range(n1):
    while not w[3] < w[2] < w[1] < w[0]:
        w[3] = random()
        w[0] = random()#* (1.0 - w[3])
        w[2] = random() #* (1.0 - w[0] - w[3])
        w[1] = random()#1.0 - w[0] - w[3] - w[2]
    q0 = [a * b for a, b in zip(m0, w)]
    q1 = [a * b for a, b in zip(m1, w)]
    q2 = [a * b for a, b in zip(m2, w)]
    r = [[sum(q0), 0], [sum(q1), 1], [sum(q2), 2]]
    r.sort(reverse=True)
    # files.write('{0:d} {1:d} {2:d} {3:f} {4:f} {5:f} {6:f}\n'.format(r[0][1], r[1][1], r[2][1], w[0], w[1], w[2], w[3]))
    if r[0][1] == 0:
        l00 += 1
    elif r[0][1] == 1:
        l10 += 1
    elif r[0][1] == 2:
        l20 += 1
    if r[1][1] == 0:
        l01 += 1
    elif r[1][1] == 1:
        l11 += 1
    elif r[1][1] == 2:
        l21 += 1
    if r[2][1] == 0:
        l02 += 1
    elif r[2][1] == 1:
        l12 += 1
    elif r[2][1] == 2:
        l22 += 1
print '1st: 0 = {0:f}% ---- 1 = {1:f}% ---- 2 = {2:f}%\n'.format(l00/n * 100, l10/n * 100, l20/n * 100)
print '2nd: 0 = {0:f}% ---- 1 = {1:f}% ---- 2 = {2:f}%\n'.format(l01/n * 100, l11/n * 100, l21/n * 100)
print '3rd: 0 = {0:f}% ---- 1 = {1:f}% ---- 2 = {2:f}%\n'.format(l02/n * 100, l12/n * 100, l22/n * 100)
files.close()