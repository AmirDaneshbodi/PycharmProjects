do for [i=2:1625]{
stats 'sobol.dat' u 4 every ::0::i
set print 'caca.dat' append
print i, STATS_mean, STATS_stddev
unset print
}

#plot "< paste sobol.dat caca.dat" u 9:12

