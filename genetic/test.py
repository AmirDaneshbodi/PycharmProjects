# # # __author__ = 'sebasanper'
# # #
# # # from math import ceil, floor, log
# # # import multiprocessing
# # # # Decimal to Binary string
# # # def dec2bin(dec):
# # #     i = 1
# # #     s = 0
# # #     while dec > 0:
# # #         rem = dec % 2
# # #         s += i * rem
# # #         dec /= 2
# # #         i *= 10
# # #     return str(s)
# # #
# # # # Binary to decimal integer
# # # def bin2dec(bina):
# # #     n = len(bina)
# # #     res = 0
# # #     for i in range(1, n + 1):
# # #         res += int(bina[i - 1]) * 2 ** (n - i)
# # #     return res
# # #
# # # def encode(i, n):
# # #     j = int(ceil(i / float(n) * (2 ** log(n, 2))))
# # #     jb = dec2bin(j)
# # #     return jb
# # #
# # # def decode(jb, n):
# # #     hd = bin2dec(jb)
# # #     h = int(floor(hd / float(2 ** log(n, 2)) * float(n)))
# # #     return h
# # #
# # # if __name__ == '__main__':
# # #     # n = 3907
# # #     # for i in range(1, n + 1):
# # #     #     print decode(encode(i, n), n)
# # #     #
# # #     # print encode(3900, 3907)
# # #     # print decode('111100111100', 3907)
# # #     print multiprocessing.cpu_count()
# # #     from joblib import Parallel, delayed
# # #     import multiprocessing
# # #     import time
# # #     start_time = time.time()
# # #
# # #     def processInput(i):
# # #         return i ** 2.0
# # #     results = Parallel(n_jobs=8)(delayed(processInput)(i) for i in range(10))
# # #     print results
# # #     print("--- %s seconds ---" % (time.time() - start_time))
# # from math import ceil, floor, log
# #
# # def dec2bin(dec):
# #     i = 1
# #     s = 0
# #     while dec > 0:
# #         rem = dec % 2
# #         s += i * rem
# #         dec /= 2
# #         i *= 10
# #     return str(s)
# #
# # def encode(i, n):
# #     j = int(i / float(n) / (2 ** (log(n, 2)) - 1))
# #     jb = dec2bin(j)
# #     return jb
# #
# # print encode(3300, 3907)
# # script = open('plot.gp', 'w')
# # for i in range(100):
# #     script.write('plot \'positions.dat\' every :::{0:d}::{0:d} ls 20 lc rgb \'blue\'\npause -1\n'.format(i))
# from random import randint
# from wake import distance
# from joblib import Parallel, delayed
# from jensen_simple import Jensen as fitness
#
# layout = open('rand_data.dat', 'r')
# res = open('result.dat', 'w')
# a = [[0.0, 0.0] for x in range(80)]
# i = 0
# for line in layout:
#     columns = line.split()
#     a[i][0] = (float(columns[0]))
#     a[i][1] = (float(columns[1]))
#     i += 1
# layout.close()
#
# def gen_turbine(min_x, max_x, min_y, max_y):
#     a = [float(randint(min_x, max_x)), float(randint(min_y, max_y))]
#     while a[1] < - 3907.0 / 412.0 * float(a[0]) + 3907.0:
#         a[0] = float(randint(min_x, max_x))
#         a[1] = float(randint(min_y, max_y))
#     while a[1] > 3907.0 / 417.0 * (5457.0 - float(a[0])):
#         a[0] = float(randint(min_x, max_x))
#         a[1] = float(randint(min_y, max_y))
#     return a
#
# def find_distance(nt, a, diam, min_x, max_x, min_y, max_y):
#     n = 0
#     while n == 0:
#         n = 1
#         for i in range(nt):
#             for j in range(nt):
#                 if i != j and distance(a[i][0], a[i][1], a[j][0], a[j][1]) < diam:
#                     print a[j], a[i]
#                     print 'pass'
#                     a[j] = gen_turbine(min_x, max_x, min_y, max_y)
#                     print a[j], a[i]
#                     print '\n'
#                     n = 0
#     return a
#
# b = Parallel(n_jobs=8)(delayed(find_distance)(80, a, 80., 0., 5457., 0., 3907.) for x in range(1))  # Parallel verification of minimum distance between distance to 1D
# # b = find_distance(80, a, 80., 0., 5457., 0., 3907.)
# for x in range(80):
#     res.write('{0:f}\t{1:f}\n'.format(b[0][x][0], b[0][x][1]))
#
# fit = Parallel(n_jobs=8)(delayed(fitness)(b[0], 80) for i in range(1))  # Parallel evaluation of fitness of all individuals
#
# print fit
#
# res.close()

def func(a):
    a[0] = a[1] + 20
    return a

print func([10, 4])