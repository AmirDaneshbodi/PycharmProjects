unset key
set xrange [-2:2]
set yrange [-1:3]
plot 'rosenbrock.dat' every :::0::0 pt 7 lc rgb 'red'
pause -1
do for [i=1:1999]{
plot 'rosenbrock.dat' every :::i::i pt 7 lc rgb 'red'
pause 0.1
}
