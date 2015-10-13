unset key
set xrange [-1000:7000]
set yrange [-1000:5000]
do for [i=0:999]{
#plot 'np200_layout_jensen.dat' u 2:3 every :::i::i pt 7 lc rgb 'red'
plot 'np200_random_layout_jensen.dat' u 2:3 every :::i::i pt 7 lc rgb 'red'
pause -1
}
