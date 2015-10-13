__author__ = 'sebasanper'

from numpy.random import normal, random
from math import sqrt
from numpy import array

def square():
    iterations =open('iterations.dat', 'w')

    np = 100
    particles = array([[[0.0, 0.0], [0.0, 0.0]] for x in range(np)])
    vel = array([[[random(), random()], [random(), random()]] for x in range(np)])
    fitness = [0.0 for x in range(np)]
    best_local = array([[[0.0, 0.0], [0.0, 0.0]] for x in range(np)])
    best_own_fitness = [0.0 for x in range(np)]
    best_global_fitness = 0.0
    for n in range(np):
        particles[n] = array([[random(), random()], [random(), random()]])

    for iter in range(100):
        for p in range(np):
            fitness[p] = sqrt((particles[p][0][0] - particles[p][1][0]) ** 2.0 + (particles[p][0][1] - particles[p][1][1]) ** 2.0)
            if fitness[p] > best_own_fitness[p]:
                best_own_fitness[p] = fitness[p]
                best_local[p] = particles[p]
            if fitness[p] > best_global_fitness:
                best_global_fitness = fitness[p]
                best = p

        for p in range(np):
            vel[p] = vel[p] + 2.0 * random() * (best_local[p] - particles[p]) + 2.0 * random() * (particles[best] - particles[p])
            particles[p] = particles[p] + vel[p]
            if particles[p][0][0] > 1.0:
                particles[p][0][0] = 1.0
            if particles[p][0][0] < 0.0:
                particles[p][0][0] = 0.0
            if particles[p][0][1] > 1.0:
                particles[p][0][1] = 1.0
            if particles[p][0][1] < 0.0:
                particles[p][0][1] = 0.0
            if particles[p][1][0] > 1.0:
                particles[p][1][0] = 1.0
            if particles[p][1][0] < 0.0:
                particles[p][1][0] = 0.0
            if particles[p][1][1] > 1.0:
                particles[p][1][1] = 1.0
            if particles[p][1][1] < 0.0:
                particles[p][1][1] = 0.0

        for n in range(np):
            for i in range(2):
                for j in range(2):
                    iterations.write('{0:f} '.format(particles[n][i][j]))
            iterations.write('\n')
        iterations.write('\n')
    iterations.close()

    print best_global_fitness
    print particles[best]

def rosenbrock():
    rosenb = open('rosenbrock.dat', 'w')

    np = 20
    particles = array([[0.0, 0.0] for x in range(np)])
    vel = array([[0.0, 0.0] for x in range(np)])
    fitness = [0.0 for x in range(np)]
    best_local = array([[0.0, 0.0] for x in range(np)])
    for n in range(np):
        if random() < 0.5:
            sign1 = 1.0
        else:
            sign1 = - 1.0
        if random() < 0.5:
            sign2 = 1.0
        else:
            sign2 = - 1.0
        particles[n] = array([sign1 * 5.0 * random(), sign2 * 5.0 * random()])
        if random() < 0.5:
            sign3 = 1.0
        else:
            sign3 = - 1.0
        if random() < 0.5:
            sign4 = 1.0
        else:
            sign4 = - 1.0
        vel[n] = array([[5.0 * sign3 * random(), 5.0 * sign4 * random()]])
    for iter in range(2000):
        for p in range(np):
            fitness[p] = (1.0 - particles[p][0]) ** 2.0 + 100.0 * (particles[p][1] - particles[p][0] ** 2.0) ** 2.0
            if iter == 0:
                best_own_fitness = [1000.0 for x in range(np)]
                best_global_fitness = 1000.0 # fitness[0]
                best = 1
            if fitness[p] < best_own_fitness[p]:
                best_own_fitness[p] = fitness[p]
                best_local[p] = particles[p]
            if fitness[p] < best_global_fitness:
                best_global_fitness = fitness[p]
                best = p
        for p in range(np):
            vel[p] = (0.5 + random() / 2.0) * vel[p] + 2.0 * random() * (best_local[p] - particles[p]) + 2.0 * random() * (particles[best] - particles[p])
            particles[p] = particles[p] + vel[p]
            if particles[p][0] > 5.0:
                particles[p][0] = 5.0
            if particles[p][0] < - 5.0:
                particles[p][0] = - 5.0
            if particles[p][1] > 5.0:
                particles[p][1] = 5.0
            if particles[p][1] < - 5.0:
                particles[p][1] = - 5.0
        for n in range(np):
            rosenb.write('{0:f} {1:f}\n'.format(particles[n][0], particles[n][1]))
        rosenb.write('\n')
    rosenb.close()

    print best_global_fitness
    print particles[best]

if __name__ == '__main__':
    rosenbrock()