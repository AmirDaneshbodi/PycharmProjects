__author__ = 'sebasanper'
import sys
from math import ceil, floor, log
from random import randint, random
# from ainslieOKoptimise import ainslie as fitness
# from larsenOKoptimise import larsen as fitness
from jensenOKoptimise import jensen as fitness
from wake import distance
import time
from joblib import Parallel, delayed

result = open('best_layout_jensen.dat', 'w', 1)
result2 = open('fitness_jensen.dat', 'w', 1)
average = open('average_fitness_jensen.dat', 'w', 1)
start_time = time.time()

try:
    def gen_individual(n_turbines, min_x, max_x, min_y, max_y):
        return [gen_turbine(min_x, max_x, min_y, max_y) for k in range(n_turbines)]

    def gen_population(n_ind, n_turbines, min_x, max_x, min_y, max_y):
        return [gen_individual(n_turbines, min_x, max_x, min_y, max_y) for x in range(n_ind)]

    def gen_turbine(min_x, max_x, min_y, max_y):
        a = [float(randint(min_x, max_x)), float(randint(min_y, max_y))]
        while a[1] < - 3907.0 / 412.0 * float(a[0]) + 3907.0:
            a[0] = float(randint(min_x, max_x))
            a[1] = float(randint(min_y, max_y))
        while a[1] > 3907.0 / 417.0 * (5457.0 - float(a[0])):
            a[0] = float(randint(min_x, max_x))
            a[1] = float(randint(min_y, max_y))
        return a

    def grade_gen(b, n):
        average = 0.0
        for item in b:
            average += item / n
        return average

    def find_distance(nt, a, diam, min_x, max_x, min_y, max_y):
        n = 0
        while n == 0:
            n = 1
            for i in range(nt):
                for j in range(nt):
                    if i != j and distance(a[i][0], a[i][1], a[j][0], a[j][1]) < diam:
                        # print 'counting'
                        a[j] = gen_turbine(min_x, max_x, min_y, max_y)
                        n = 0
        return a

    n_iter = 50
    n_ind = 300
    nt = 80
    diam = 80.0
    min_x = 0
    max_x = 5457
    min_y = 0
    max_y = 3907
    mutation_rate = 0.01
    selection_percentage = 0.2
    random_selection = 0.05

    pops = gen_population(n_ind, nt, min_x, max_x, min_y, max_y)
    # pops.append([])
    # layout = open('horns_rev.dat', 'r')
    # for line in layout:
    #    columns = line.split()
    #    pops[-1].append([float(columns[0]) - 423974.0, float(columns[1]) - 6147540.0])
    # layout.close()
    n_ind = len(pops)
    for iteration in range(n_iter):  # Iteration through generations loop
        start_time2 = time.time()
        pop = pops
        # for x in range(nt):
        #     result.write('{0:d}\t{1:d}\n'.format(int(pop[0][x][0]), int(pop[0][x][1])))
        # result.write('\n')
        pop = Parallel(n_jobs=8)(delayed(find_distance)(nt, pop[x], diam, min_x, max_x, min_y, max_y) for x in range(n_ind))  # Parallel verification of minimum distance between turbines to 1D
        # for x in range(nt):
        #     result.write('{0:d}\t{1:d}\n'.format(int(pop[0][x][0]), int(pop[0][x][1])))
        # result.write('\n')
        fit = Parallel(n_jobs=8)(delayed(fitness)(pop[i]) for i in range(n_ind))  # Parallel evaluation of fitness of all individuals

        aver = grade_gen(fit, float(n_ind))

        average.write('{0:f}\n'.format(aver))

        for i in range(n_ind):
            fit[i] = [fit[i], i]
        for x in range(nt):
            result.write('{0:d}\t{1:d}\n'.format(int(pop[max(fit)[1]][x][0]), int(pop[max(fit)[1]][x][1])))
        result.write('\n')

        for y in range(n_ind):
            result2.write('{0:f}\n'.format(fit[y][0]))
        result2.write('\n')

        graded = [x[1] for x in sorted(fit, reverse=True)]

        retain_length = int(len(graded) * selection_percentage)
        parents_index = graded[:retain_length]

        # Add randomly other individuals for variety
        for item in graded[retain_length:]:
            if random_selection > random():
                parents_index.append(item)

        # Mutation of individuals
        for item in parents_index:
            if mutation_rate > random():
                place = randint(0, len(pop[item]) - 1)
                pop[item][place] = gen_turbine(min_x, max_x, min_y, max_y)

        pops = []
        for item in parents_index:
            pops.append(pop[item])

        # Crossover function. Create children from parents
        parents_length = len(parents_index)
        desired_length = n_ind - parents_length
        children = []
        while len(children) < desired_length:
            parent1 = randint(0, parents_length - 1)
            parent2 = randint(0, parents_length - 1)
            if parent1 != parent2:
                parent1 = pop[parents_index[parent1]]
                parent2 = pop[parents_index[parent2]]
                cross_place = randint(0, nt - 1)
                child = parent1[:cross_place] + parent2[cross_place:]
                children.append(child)
        pops.extend(children)

        print("%d iteration--- %s minutes ---" % (iteration, (time.time() - start_time2) / 60.0))
    print("--- %s minutes ---" % ((time.time() - start_time) / 60.0))
    result.close()
    result2.close()
    average.close()
except KeyboardInterrupt:
    sys.stdout.flush()
    sys.exit()
