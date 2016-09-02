out = open('wind.wnd', 'w')
for i in range(54):
    time1 = i * 30.0
    time2 = time1 + 0.1
    wind1 = 3.0 + (i - 1) * 0.5
    wind2 = wind1 + 0.5
    out.write('{0:f}\t{1:f}\t0.0\t0.0\t0.0\t0.0\t0.0\t0.0\n{2:f}\t{3:f}\t0.0\t0.0\t0.0\t0.0\t0.0\t0.0\n'.format(time1, wind1, time2, wind2))
out.close()