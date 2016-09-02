unset key
set yrange [-10:4000]
set xrange [-10:5500]
do for [i=0:57]{
plot '30deg_layout.dat' u 1:2:3 every :::i::i w labels,-3907/412 * x + 3907, 3907/417*(5457 - x), 3907, 0
pause 0.5
}
do for [i=0:197]{
plot '360deg_0_layout.dat' u 1:2:3 every :::i::i w labels,-3907/412 * x + 3907, 3907/417*(5457 - x), 3907, 0
pause 0.5
}
do for [i=0:22]{
plot '3_30deg_layout.dat' u 1:2:3 every :::i::i w labels,-3907/412 * x + 3907, 3907/417*(5457 - x), 3907, 0
pause 0.5
}
