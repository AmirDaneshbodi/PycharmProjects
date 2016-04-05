__author__ = 'Sebastian Sanchez Perez-Moreno. Email: s.sanchezperezmoreno@tudelft.nl'

from numpy.random import random
from wake import distance
from numpy import array
# from jensenOKoptimise import jensen as fit
from ainslieOKoptimise import ainslie as fit
# from larsenOKoptimise import larsen as fitW
from copy import deepcopy
import time
from math import floor
start = time.time()
windrose = open('horns_rev_windrose2.dat', 'r')
windrose_angle = []
windrose_speed = []
windrose_frequency = []
for line in windrose:
    columns = line.split()
    windrose_angle.append(float(columns[0]))
    windrose_speed.append(float(columns[1]))
    windrose_frequency.append(float(columns[2]))

windrose.close()

layout_file = open('360deg_0_layout.dat', 'w', 1)
fitness_file = open('360deg_0_best_global_fitness.dat', 'w', 1)

nt = 80
diam = 80.0

layout = open('horns_rev.dat', 'r')
# layout = open('last_good.dat', 'r')
ll = 0
horns = array([[0.0, 0.0] for x in range(nt)])
for line in layout:
    columns = line.split()
    horns[ll] = [float(columns[0]) - 423974.0, float(columns[1]) - 6147543.0]
    # horns[ll] = [float(columns[0]), float(columns[1])]
    ll += 1
layout.close()

fitness = fit(horns, windrose_angle, windrose_speed, windrose_frequency)
print fitness
best_fitness = fitness * 1.0
improve_flag = False

for g in range(nt):
    layout_file.write('{0:f} {1:f}\n'.format(horns[g][0], horns[g][1]))
layout_file.write('\n')

def feasible(h, num):
    feasible2 = True
    for i in range(nt):
        if i != num:
            if distance(h[num][0], h[num][1], h[i][0], h[i][1]) < 2.0 * diam:
                feasible2 = False
                break
    return feasible2

best_layout = horns * 1.0

for iter in range(3000):
    horns = best_layout * 1.0

    if improve_flag == False:
        chosen = int(floor(random() * nt - 0.0000000001))
        # print horns[chosen]
        while True:
            v = array([(random() * 2.0 - 1.0) * 5457.0, (random() * 2.0 - 1.0) * 3907.0])
            nada = horns * 1.0
            nada[chosen] += v
            if nada[chosen][1] < 3907.0 and nada[chosen][1] > 0.0 and nada[chosen][1] < 3907.0 / 417.0 * (- nada[chosen][0] + 5457.0 + 10.0) and nada[chosen][1] > - 3907.0 / 412.0 * (nada[chosen][0] + 10.0) + 3907.0 and feasible(nada, chosen):
                horns[chosen] = horns[chosen] + v
                break
    else:
        while True:
            v = random() * v
            nada = horns * 1.0
            nada[chosen] += v
            if nada[chosen][1] < 3907.0 and nada[chosen][1] > 0.0 and nada[chosen][1] < 3907.0 / 417.0 * (- nada[chosen][0] + 5457.0 + 10.0) and nada[chosen][1] > - 3907.0 / 412.0 * (nada[chosen][0] + 10.0) + 3907.0 and feasible(nada, chosen):
                horns[chosen] = horns[chosen] + v
                break

    fitness = fit(horns, windrose_angle, windrose_speed, windrose_frequency)
    # print fitness

    if fitness < best_fitness:
        best_fitness = fitness * 1.0
        best_layout = horns * 1.0
        improve_flag = True
        fitness_file.write('{0:d} {1:.20f}\n'.format(iter, best_fitness))
        for t in range(nt):
            layout_file.write('{0:f} {1:f} {2:d}\n'.format(best_layout[t][0], best_layout[t][1], t))
        layout_file.write('\n')
        print best_fitness
    else:
        improve_flag = False
    if iter % 1 == 0:
        print str(iter) + ' iter ------ ' + str(- start + time.time()) + ' s'
print 'Total time ------ ' + str(- start + time.time()) + ' s'
fitness_file.close()
layout_file.close()