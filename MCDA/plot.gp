# To plot which alternative is the First in ranking according to 2 first criteria
plot 'sensitivity.dat' u 6:7:($2==0?$1:1/0) pt 7 t 'Site 1', 'sensitivity.dat' u 6:7:($2==1?$1:1/0) pt 7 ps 1 t 'Site 2', 'sensitivity.dat' u 6:7:($2==2?$1:1/0) pt 7 ps 1 t 'Site 3', 'sensitivity.dat' u 6:7:($2==3?$1:1/0) pt 7 ps 1 t 'Site 4', 'sensitivity.dat' u 6:7:($2==4?$1:1/0) pt 7 ps 1 t 'Site 5'
pause -1

plot 'sensitivity.dat' u 6:7:($1==1?$1:1/0) pt 7 t '1st place', 'sensitivity.dat' u 6:7:($2==1?$1:1/0) pt 7 ps 1 t '2nd place', 'sensitivity.dat' u 6:7:($3==1?$1:1/0) pt 7 ps 1 t '3rd place', 'sensitivity.dat' u 6:7:($4==1?$1:1/0) pt 7 ps 1 t '4th place', 'sensitivity.dat' u 6:7:($5==1?$1:1/0) pt 7 ps 1 t '5th place'


# To plot the average ranking with minimum and maximum values.
set size ratio 0.5
unset key
set xrange [-1:61]
set yrange [0:60]
plot 'TDA_alternatives_statistics.dat' u 1:7:2:6 w yerrorbars pt 7, '' u 4 w p lc rgb 'dark-green' # with median 4 for skewness and avoid incluence of extreme values, x, y, low y, high y

$ Plot with standard variation only as whiskerbars
unset key
plot 'TDA_alternatives_statistics.dat' u 1:7:8 w yerrorbars

# Plot with quantiles. BEST PLOT OF ALL.
set term wxt
unset key
set style fill solid
plot 'TDA_alternatives_statistics.dat' using 1:3:2:6:5 with candlesticks whiskerbars lc rgb 'dark-red', '' u 1:4:4:4:4 w candlesticks lc rgb 'light-blue' lw 3

# Data columns: X Min 1stQuartile Median 3rdQuartile Max BoxWidth Titles

#green
#dark-green
#light-green
#yellow
#dark-yellow
#red
#dark-red
#light-red
#black
#blue
#dark-blue
#light-blue
#orange
#dark-orange
#violet
#dark-violet
#light-violet
#gray
#light-gray
#dark-grey
#greenyellow
#brown
#gold
#silver
#pink
#magenta
