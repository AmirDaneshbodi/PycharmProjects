out = open('plotwind.dat', 'w')
with open('Kaimal.u') as inf:
    i = 0
    time = []
    centre = []
    wind1 = []
    wind2 = []
    wind3 = []
    wind4 = []
    wind5 = []

    for line in inf:
        parts = line.split()  # split line into parts
        if i > 11:
            if (i - 12) % 7 == 0:
                time.append(parts[0])
                centre.append(parts[1])
            elif (i - 13) % 7 == 0:
                # wind1.append(parts)
                out.write('{0:s}\t{1:s}\t{2:s}\t{3:s}\t{4:s}\n'.format(parts[0], parts[1], parts[2], parts[3], parts[4]))
                # out.write(line)
            elif (i - 14) % 7 == 0:
                # wind2.append(parts)
                out.write('{0:s}\t{1:s}\t{2:s}\t{3:s}\t{4:s}\n'.format(parts[0], parts[1], parts[2], parts[3], parts[4]))
            elif (i - 15) % 7 == 0:
                # wind3.append(parts)
                out.write('{0:s}\t{1:s}\t{2:s}\t{3:s}\t{4:s}\n'.format(parts[0], parts[1], parts[2], parts[3], parts[4]))
            elif (i - 16) % 7 == 0:
                # wind4.append(parts)
                out.write('{0:s}\t{1:s}\t{2:s}\t{3:s}\t{4:s}\n'.format(parts[0], parts[1], parts[2], parts[3], parts[4]))
            elif (i - 17) % 7 == 0:
                # wind5.append(parts)
                out.write('{0:s}\t{1:s}\t{2:s}\t{3:s}\t{4:s}\n'.format(parts[0], parts[1], parts[2], parts[3], parts[4]))
            else:
                out.write('\n\n')
        i += 1
out.close()