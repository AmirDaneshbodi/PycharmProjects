from numpy import array, std, average
from scipy.stats.stats import pearsonr
from numpy import corrcoef
from matplotlib.mlab import PCA

a = [[] for _ in range(5)]

with open("data_pca.dat", "r") as inp:
    for line in inp:
        col = line.split()
        a[0].append(float(col[0]))
        a[1].append(float(col[1]))
        a[2].append(float(col[2]))
        a[3].append(float(col[3]))
        a[4].append(float(col[4]))

data = array(a).transpose()
n = len(data[0])

s = [0 for _ in range(n)]
av = [0 for _ in range(n)]
b = [[0 for _ in range(len(a[0]))] for _ in range(n)]

for i in range(n):
    s[i] = std(a[i])
    av[i] = average(a[i])

for i in range(n):
    for j in range(len(a[0])):
        b[i][j] = (a[i][j] - av[i]) / s[i]

mat1 = [[0 for _ in range(n)] for _ in range(n)]
mat2 = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        mat1[i][j] = corrcoef(a[i], a[j])[0]
        mat2[i][j] = pearsonr(a[i], a[j])[0]

s = [[str(e) for e in row] for row in mat1]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print "\n======= PEARSON CORRELATION COEFFICIENT SCIPY===========\n"
print '\n'.join(table)
s = [[str(e) for e in row] for row in mat2]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]

print
print "======= PEARSON CORRELATION COEFFICIENT NUMPY ===========\n"
print '\n'.join(table)
results = PCA(data)
print
print "======= EIGENVALUES ===========\n"
eigen = results.s / 100.0 * 5.0
print eigen
print
print "======= PERCENTAGE OF VARIANCE ===========\n"
perc = results.fracs * 100.0
print perc
with open("percentage.dat", "w") as outperc:
    k = 0
    for i in perc:
        k += 1
        outperc.write("{1:d} {0:f} {2:f}\n".format(i, k, eigen[k-1]))
print
print "======= CUMULATIVE PERCENTAGE ===========\n"
cumul = []
suma = 0.0
for i in perc:
    suma += i
    cumul.append(suma)
print cumul
print
print "======= WEIGHTS OF PRINCIPAL COMPONENTS ===========\n"
print -results.Wt
print
print "======= PRINCIPAL COMPONENTS ===========\n"
z = [[0 for _ in range(len(data))] for _ in range(n)]
for i in range(n):
    for k in range(len(data)):
        sum2 = 0.0
        for j in range(n):
            sum2 += -results.Wt[i][j] * b[j][k]
        z[i][k] = sum2
print z
print
PCA1 = [[0 for _ in range(n)] for _ in range(n)]
print "======= CORRELATION BETWEEN VARIABLES AND PRINCIPAL COMPONENTS ===========\n"
for l in range(n):
    for j in range(n):
        PCA1[l][j] = pearsonr(b[j], z[l])[0]
    print PCA1[l]
print

print "======= VALUES OF COMMUNALITY ===========\n"
for i in range(5):
    print PCA1[0][i] ** 2.0 + PCA1[1][i] ** 2.0


# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# x = []
# y = []
# z = []
# for item in results.Y:
#     x.append(item[0])
#     y.append(item[1])
#     z.append(item[2])
#
# plt.close('all')  # close all latent plotting windows
# fig1 = plt.figure()  # Make a plotting figure
# ax = Axes3D(fig1)  # use the plotting figure to create a Axis3D object.
# pltData = [x, y, z]
# ax.scatter(pltData[0], pltData[1], pltData[2], 'bo')  # make a scatter plot of blue dots from the data
#
# # make simple, bare axis lines through space:
# xAxisLine = (
# (min(pltData[0]), max(pltData[0])), (0, 0), (0, 0))  # 2 points make the x-axis line at the data extrema along x-axis
# ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'r')  # make a red line for the x-axis.
# yAxisLine = (
# (0, 0), (min(pltData[1]), max(pltData[1])), (0, 0))  # 2 points make the y-axis line at the data extrema along y-axis
# ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'r')  # make a red line for the y-axis.
# zAxisLine = (
# (0, 0), (0, 0), (min(pltData[2]), max(pltData[2])))  # 2 points make the z-axis line at the data extrema along z-axis
# ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'r')  # make a red line for the z-axis.
#
# # label the axes
# ax.set_xlabel("x-axis label")
# ax.set_ylabel("y-axis label")
# ax.set_zlabel("y-axis label")
# ax.set_title("The title of the plot")
# plt.show()  # show the plot