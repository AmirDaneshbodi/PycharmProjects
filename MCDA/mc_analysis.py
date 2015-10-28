__author__ = 'sebasanper'
from random import random
from numpy import std
from math import ceil, floor, fabs
files1 = open('time_stats.dat', 'r')
files2 = open('efficiency_stats.dat', 'r')  # For TDA: Time, Detail, Accuracy. Order of importance.

def mean(vect):
    return float(sum(vect)) / float(len(vect))


def modes(ff, n):
    maxim = [0.0 for g in range(n)]
    for i in range(n):
        maxim[i] = 0
        for h in range(n):
            if ff[h][i] > ff[maxim[i]][i]:
                maxim[i] = h
    return maxim


def median_function(vector):
    vector = sorted(vector)
    if len(vector) % 2 == 0:
        return (vector[int(len(vector) / 2.0 - 0.5)] + vector[int(len(vector) / 2.0 + 0.5)]) / 2.0
    else:
        return vector[len(vector) / 2]


exe_time = []
accuracy = []
detail = []
for line1 in files1:
    columns1 = line1.split()
    exe_time.append((37.203561 - float(columns1[5])) / (37.203561 - 0.836113))
    detail.append(float(columns1[8]))
for line2 in files2:
    columns2 = line2.split()
    accuracy.append((10.8964 - fabs(float(columns2[5]) - 89.0)) / (10.8964 - 0.01338))
m = []
for g in range(len(accuracy)):
    m.append([exe_time[g], accuracy[g], detail[g]])
n_alt = len(accuracy)
dim = len(m)
n = 10000.0  # MonteCarlo simulations
n1 = int(n)

analysis = ['TDA', 'TAD', 'ALL']
for run in analysis:
    if run == 'TDA':
        out1 = open('TDA_ranks_weights.dat', 'w')  # For TDA: Time, Detail, Accuracy. Order of importance.
        out2 = open('TDA_alternatives_statistics.dat', 'w')
        out3 = open('TDA_percentages.dat', 'w')
    elif run == 'TAD':
        out1 = open('TAD_ranks_weights.dat', 'w')  # For TAD: Time, Accuracy, Detail. Order of importance.
        out2 = open('TAD_alternatives_statistics.dat', 'w')
        out3 = open('TAD_percentages.dat', 'w')
    else:
        out1 = open('ALL_ranks_weights.dat', 'w')  # For all combinations without order of importance.
        out2 = open('ALL_alternatives_statistics.dat', 'w')
        out3 = open('ALL_percentages.dat', 'w')

    counter = [[0.0 for y in range(n_alt)] for f in range(n_alt)]
    median = [0 for f in range(n_alt)]
    quartile25 = [0 for f in range(n_alt)]
    quartile75 = [0 for f in range(n_alt)]
    average = [0 for f in range(n_alt)]
    deviation = [0 for f in range(n_alt)]

    best = [999 for i in range(n_alt)]
    worst = [0 for i in range(n_alt)]
    vec = [[] for b in range(n_alt)]

     #  Here starts the Monte Carlo loop with n1 simulations.
    for x in range(n1):
        q = [0 for f in range(n_alt)]
        r = [0 for f in range(n_alt)]
        w = [0.0 for g in range(dim)]
        o = [[], [], []]
        if run == 'TDA':  # Method for random weights with order, same as J. Butler et al. with 1-w0, 1-w0-w1, a much denser region is found and not uniform.s
            p = [random(), random()]
            p.sort(reverse=True)
            o[0] = 1.0 - p[0]  # No ranking of the criteria at all. All possibilities considered.
            o[1] = p[0] - p[1]
            o[2] = p[1]
            o.sort(reverse=True)
            w[0] = o[0]
            w[2] = o[1]
            w[1] = o[2]
        elif run == 'TAD':
            p = [random(), random()]
            p.sort(reverse=True)
            o[0] = 1.0 - p[0]  # No ranking of the criteria at all. All possibilities considered.
            o[1] = p[0] - p[1]
            o[2] = p[1]
            o.sort(reverse=True)
            w[0] = o[0]
            w[1] = o[1]
            w[2] = o[2]
        else:
            p = [random(), random()]
            p.sort(reverse=True)
            w[0] = 1.0 - p[0]  # No ranking of the criteria at all. All possibilities considered.
            w[1] = p[0] - p[1]
            w[2] = p[1]

        for l in range(n_alt):
            q[l] = [a * b for a, b in zip(m[l], w)]
            r[l] = [sum(q[l]), l]
        r.sort(reverse=True)

        # Gives best and worst positions in ranking during all simulation.
        for alt2 in range(n_alt):
            for rank2 in range(n_alt):
                if r[rank2][1] == alt2:
                    vec[alt2].append(rank2)
                    if rank2 <= best[alt2]:
                        best[alt2] = rank2
                    if rank2 >= worst[alt2]:
                        worst[alt2] = rank2

        # Gives the number of times each alternative fell in each ranking.
        for rank in range(n_alt):
            for alt in range(n_alt):
                if r[rank][1] == alt:
                    counter[rank][alt] += 1.0

        # Write ranking and weights to file.
        for i in range(n_alt):
            out1.write('{0:d} '.format(r[i][1]))
        out1.write('{0:f} {1:f} {2:f}\n'.format(w[0], w[2], w[1]))

    # Calculates the median and other statistical measures of every alternative.
    for alt in range(n_alt):
        median[alt] = median_function(vec[alt])
        quartile25[alt] = median_function(sorted(vec[alt])[:int(len(vec[3])/2.)])
        quartile75[alt] = median_function(sorted(vec[alt])[int(len(vec[3])/2.):])
        average[alt] = mean(vec[alt])
        deviation[alt] = std(vec[alt])
        out2.write('{0:d} {1:f} {2:f} {3:f} {4:f} {5:f} {6:f} {7:f}\n'.format(alt, best[alt], quartile25[alt], median[alt], quartile75[alt], worst[alt], average[alt], deviation[alt]))

    for rank in range(n_alt):
        for alt in range(n_alt):
            if counter[rank][alt] != 0:
                out3.write('{0:d} {1:d} {2:.2f}\n'.format(rank, alt, counter[rank][alt] * 100.0 / n))

    out1.close()
    out2.close()
    out3.close()
files1.close()
files2.close()
