# # __author__ = 'sebasanper'
# #
# # from math import ceil, floor, log
# # import multiprocessing
# # # Decimal to Binary string
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
# # # Binary to decimal integer
# # def bin2dec(bina):
# #     n = len(bina)
# #     res = 0
# #     for i in range(1, n + 1):
# #         res += int(bina[i - 1]) * 2 ** (n - i)
# #     return res
# #
# # def encode(i, n):
# #     j = int(ceil(i / float(n) * (2 ** log(n, 2))))
# #     jb = dec2bin(j)
# #     return jb
# #
# # def decode(jb, n):
# #     hd = bin2dec(jb)
# #     h = int(floor(hd / float(2 ** log(n, 2)) * float(n)))
# #     return h
# #
# # if __name__ == '__main__':
# #     # n = 3907
# #     # for i in range(1, n + 1):
# #     #     print decode(encode(i, n), n)
# #     #
# #     # print encode(3900, 3907)
# #     # print decode('111100111100', 3907)
# #     print multiprocessing.cpu_count()
# #     from joblib import Parallel, delayed
# #     import multiprocessing
# #     import time
# #     start_time = time.time()
# #
# #     def processInput(i):
# #         return i ** 2.0
# #     results = Parallel(n_jobs=8)(delayed(processInput)(i) for i in range(10))
# #     print results
# #     print("--- %s seconds ---" % (time.time() - start_time))
# from math import ceil, floor, log
#
# def dec2bin(dec):
#     i = 1
#     s = 0
#     while dec > 0:
#         rem = dec % 2
#         s += i * rem
#         dec /= 2
#         i *= 10
#     return str(s)
#
# def encode(i, n):
#     j = int(i / float(n) / (2 ** (log(n, 2)) - 1))
#     jb = dec2bin(j)
#     return jb
#
# print encode(3300, 3907)
script = open('plot.gp', 'w')
for i in range(100):
    script.write('plot \'positions\'.dat\' every :::{}::{} ls 20 lc rgb \'blue\'\npause -1\n')