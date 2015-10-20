__author__ = 'sebasanper'
from random import random
from numpy import std
from math import ceil, floor
files = open('sensitivity.dat', 'w')
out = open('statistics.dat', 'w')
m = [[0.8, 0.3, 0.4], [0.7, 0.2, 0.7], [0.5, 0.3, 0.65], [0.3, 0.7, 0.2], [0.35, 0.5, 0.6]]
dim = 5
n = 10000.0
n1 = int(n)
counter = [[0.0 for y in range(dim)] for x in range(dim)]
median = [0 for f in range(dim)]
quartile25 = [0 for f in range(dim)]
quartile75 = [0 for f in range(dim)]
average = [0 for f in range(dim)]
deviation = [0 for f in range(dim)]
r = [0 for f in range(dim)]
q = [0 for f in range(dim)]

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

# best = [4 for f in range(dim)]
best = [99 for i in range(dim)]
worst = [0 for i in range(dim)]
vec = [[] for b in range(dim)]

for x in range(n1):
    w = [0.0 for o in range(3)]
    while not w[2] < w[1] < w[0]:
        w[0] = random()
        w[1] = random() * (1.0 - w[0])
        w[2] = 1.0 - w[0] - w[1]
    for l in range(dim):
        q[l] = [a * b for a, b in zip(m[l], w)]
        r[l] = sum(q[l]), l
    r.sort(reverse=True)

    # Gives best and worst positions in ranking during all simulation.
    for v in range(dim):
        for num in range(dim):
            if r[num][1] == v:
                vec[v].append(num)
                if num < best[v]:
                    best[v] = num
                if num > worst[v]:
                    worst[v] = num

    # Gives the number of times each alternative fell in each ranking.
    for rank in range(dim):
        for alt in range(dim):
            if r[rank][1] == alt:
                counter[rank][alt] += 1.0

    # Write ranking and weights to file.
    files.write('{0:d} {1:d} {2:d} {3:d} {4:d} {5:f} {6:f} {7:f}\n'.format(r[0][1], r[1][1], r[2][1], r[3][1], r[4][1], w[0], w[1], w[2]))
# print best

# Calculates the median of every alternative.
for alt in range(dim):
    median[alt] = median_function(vec[alt])
    quartile25[alt] = median_function(vec[alt][:len(vec) / 2])
    quartile75[alt] = median_function(vec[alt][len(vec) / 2:])
    average[alt] = mean(vec[alt])
    deviation[alt] = std(vec[alt])
    out.write('{0:d} {1:f} {2:f} {3:f} {4:f} {5:f} {6:f} {7:f}\n'.format(alt, best[alt], quartile25[alt], median[alt], quartile75[alt], worst[alt], average[alt], deviation[alt]))

print best
print worst
print modes(counter, dim)
print median
print quartile25
print quartile75
print average
print deviation


print('1st place: Alt. 0 --> {0:.2f}%, Alt. 1 --> {1:.2f}%, Alt. 2 --> {2:.2f}%, Alt. 3 --> {3:.2f}%, Alt. 4 --> {4:.2f}%'.format(counter[0][0] * 100.0/n, counter[0][1] * 100.0/n, counter[0][2] * 100.0/n, counter[0][3] * 100.0/n, counter[0][4] * 100.0/n))
print('2nd place: Alt. 0 --> {0:.2f}%, Alt. 1 --> {1:.2f}%, Alt. 2 --> {2:.2f}%, Alt. 3 --> {3:.2f}%, Alt. 4 --> {4:.2f}%'.format(counter[1][0] * 100.0/n, counter[1][1] * 100.0/n, counter[1][2] * 100.0/n, counter[1][3] * 100.0/n, counter[1][4] * 100.0/n))
print('3rd place: Alt. 0 --> {0:.2f}%, Alt. 1 --> {1:.2f}%, Alt. 2 --> {2:.2f}%, Alt. 3 --> {3:.2f}%, Alt. 4 --> {4:.2f}%'.format(counter[2][0] * 100.0/n, counter[2][1] * 100.0/n, counter[2][2] * 100.0/n, counter[2][3] * 100.0/n, counter[2][4] * 100.0/n))
print('4th place: Alt. 0 --> {0:.2f}%, Alt. 1 --> {1:.2f}%, Alt. 2 --> {2:.2f}%, Alt. 3 --> {3:.2f}%, Alt. 4 --> {4:.2f}%'.format(counter[3][0] * 100.0/n, counter[3][1] * 100.0/n, counter[3][2] * 100.0/n, counter[3][3] * 100.0/n, counter[3][4] * 100.0/n))
print('5th place: Alt. 0 --> {0:.2f}%, Alt. 1 --> {1:.2f}%, Alt. 2 --> {2:.2f}%, Alt. 3 --> {3:.2f}%, Alt. 4 --> {4:.2f}%'.format(counter[4][0] * 100.0/n, counter[4][1] * 100.0/n, counter[4][2] * 100.0/n, counter[4][3] * 100.0/n, counter[4][4] * 100.0/n))

files.close()
out.close()

if __name__ == '__main__':
    pass