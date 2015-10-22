inputfile = open('cp_hornsrev.dat', 'r')
cp = []
for line in inputfile:
    columns = line.split()
    cp.append(float(columns[1]))

for w in range(23):
    print w + 3.0, 0.0005 * 1.225 * 40 ** 2.0 * 3.141592 * cp[w] * (float(w) + 3.0)  ** 3.0