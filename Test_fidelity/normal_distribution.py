from random import gauss
out = open('normal.dat', 'w')
n = 100000
mu = 0.0
sigma = 0.3
mu2 = 1.0
sigma2 = 0.5
# for i in range(n):
#     x = gauss(mu, sigma)
#     y = gauss(mu2, sigma2)
#     out.write('{0:f}\t{1:f}\t{2:f}\t{3:f}\t{4:f}\n'.format(x, y, x * y, (x + y) / 2.0, x ** 2.0))
# out.close()

a = [gauss(mu, sigma) for _ in range(n)]
print len(a)
def online_variance(data):
    n = 2
    mean = 0.0
    M2 = 0.0

    for x in data:
        n += 1
        delta = x - mean
        mean += delta/n
        M2 += delta*(x - mean)
        out.write('{0:f}\n'.format((M2 / (n - 1)) ** 0.5))

    if n < 2:
        return float('nan')
    else:
        return M2 / (n - 1)

online_variance(a)