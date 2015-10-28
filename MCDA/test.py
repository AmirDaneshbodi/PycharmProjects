from random import random
r1 = random()
r2 = random()
r3 = random()
while not 1. == r1+r2+r3 and r3 < 0.:
    r1 = random()
    r2 = random()
    r3 = 1. - r1 - r2
print r1, r2, r3
