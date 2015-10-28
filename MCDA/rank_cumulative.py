input = open('TDA_percentages.dat', 'r')
output = open('cumulative.dat', 'w')
cumulative = [0.0 for x in range(60)]
for line in input:
    columns = line.split()
    for rank in range(60):
        if int(columns[0]) == rank:
            cumulative[int(columns[1])] += float(columns[2])
            output.write('{0:d} {1:d} {2:f}\n'.format(rank, int(columns[1]), cumulative[int(columns[1])]))

out = open('cumulative.gp', 'w')
out.write('set term wxt\n')
out.write('set xlabel \'Rank\'\n')
out.write('set ylabel \'Cumulative %\'\n')
out.write("plot \"<awk '{if($2==0){print $1,$3}}' cumulative.dat\" w lp t 'Alt. 0'")
for x in range(1, 60):  # Plots weights (time vs accuracy) per alternative for one particular ranking. Change $2== for desired ranking. and file
    out.write(", \"<awk '{if($2=="+str(x)+"){print $1,$3}}' cumulative.dat\" w lp t 'Alt. "+str(x)+"'")
out.write('\npause -1')
out.close()

