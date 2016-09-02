from math import floor


def func(index, base):
    result = 0
    f = 1
    i = index
    while i > 0:
        f = f / base
        result += f * (i % base)
        i = floor(i / base)
    return result

print func(999, 2.0)