clear
reset
set key off
set border 3

# Each bar is half the (visual) width of its x-range.
set boxwidth 0.5 absolute
set style fill solid 1.0 noborder

bin_width = 1;

bin_number(x) = floor(x/bin_width)

rounded(x) = bin_width * (bin_number(x))

plot 'weights_sensitivity.dat' using (rounded($1)):(1): smooth frequency w labels
pause -1
