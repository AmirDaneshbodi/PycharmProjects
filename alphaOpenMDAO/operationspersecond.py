from time import time, clock

def operations():
    start = time()
    start2 = clock()
    i = 0
    x = 0
    b = time() - start
    c = clock() - start2

    while c < 1.0:
        x += 1
        i += 1
        i += 1
        i += 1
        i += 1
        i += 1
        i += 1
        i += 1
        i += 1
        i += 1
        i += 1
        i += 1
        i += 1
        i += 1
        c = clock() - start2

    return x


if __name__ == '__main__':
    out = open('time2.dat', 'a')
    for x in range(10):
        out.write('{0:f}\n'.format(operations()))
        # print operations()
    out.close()
