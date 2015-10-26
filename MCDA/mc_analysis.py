__author__ = 'sebasanper'
from random import random
from numpy import std
from math import ceil, floor, fabs
files1 = open('time_stats.dat', 'r')
files2 = open('efficiency_stats.dat', 'r')
out1 = open('mcda_ranks_weights.dat', 'w')
out2 = open('mcda_alternatives_statistics.dat', 'w')
out3 = open('mcda_percentages', 'w')
exe_time = []
efficiency = []
for line1 in files1:
    columns1 = line1.split()
    exe_time.append((37.203561 - float(columns1[5])) / (37.203561 - 0.836113))
for line2 in files2:
    columns2 = line2.split()
    efficiency.append((10.8964 - fabs(float(columns2[5]) - 89.0)) / (10.8964 - 0.01338))
m = []
for g in range(len(efficiency)):
    m.append([exe_time[g], efficiency[g]])
n_alt = len(efficiency)
dim = len(m)
n = 100.0  # MonteCarlo simulations
n1 = int(n)
counter = [[0.0 for y in range(n_alt)] for x in range(n_alt)]
median = [0 for f in range(n_alt)]
quartile25 = [0 for f in range(n_alt)]
quartile75 = [0 for f in range(n_alt)]
average = [0 for f in range(n_alt)]
deviation = [0 for f in range(n_alt)]
r = [0 for f in range(n_alt)]
q = [0 for f in range(n_alt)]

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
    vector.sort()
    if len(vector) % 2 == 0:
        return (vector[int(len(vector) / 2.0 - 0.5)] + vector[int(len(vector) / 2.0 + 0.5)]) / 2.0
    else:
        return vector[len(vector) / 2]

# best = [4 for f in range(n_alt)]
best = [999 for i in range(n_alt)]
worst = [0 for i in range(n_alt)]
vec = [[] for b in range(n_alt)]

 #  Here starts the Monte Carlo loop with n1 simulations.
for x in range(n1):
    w = [0.0 for o in range(dim)]
    w[0] = random() / 2.0 + 0.5
    w[1] = 1.0 - w[0]
    for l in range(n_alt):
        q[l] = [a * b for a, b in zip(m[l], w)]
        r[l] = [sum(q[l]), l]
    r.sort(reverse=True)
    # Gives best and worst positions in ranking during all simulation.
    for v in range(n_alt):
        for num in range(n_alt):
            if r[num][1] == v:
                vec[v].append(num)
                if num < best[v]:
                    best[v] = num
                if num > worst[v]:
                    worst[v] = num

    # Gives the number of times each alternative fell in each ranking.
    for rank in range(n_alt):
        for alt in range(n_alt):
            if r[rank][1] == alt:
                counter[rank][alt] += 1.0

    # Write ranking and weights to file.
    for i in range(n_alt):
        out1.write('{0:d} '.format(r[i][1]))
    out1.write('{0:f} {1:f}\n'.format(w[0], w[1]))

# Calculates the median and other statistical measures of every alternative.
for alt in range(n_alt):
    median[alt] = median_function(vec[alt])
    quartile25[alt] = median_function(vec[alt][:len(vec) / 2])
    quartile75[alt] = median_function(vec[alt][len(vec) / 2:])
    average[alt] = mean(vec[alt])
    deviation[alt] = std(vec[alt])
    out2.write('{0:d} {1:f} {2:f} {3:f} {4:f} {5:f} {6:f} {7:f}\n'.format(alt, best[alt], quartile25[alt], median[alt], quartile75[alt], worst[alt], average[alt], deviation[alt]))


for rank in range(n_alt):
    for alt in range(n_alt):
        if counter[rank][alt] != 0:
            out3.write('{0:d} {1:d} {2:.2f}\n'.format(rank, alt, counter[rank][alt] / n * 100.0))

files1.close()
files2.close()
out1.close()
out2.close()
out3.close()