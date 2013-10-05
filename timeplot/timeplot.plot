reset
set terminal png size 1024,768
set xlabel "Data Set Size (n)"

set ylabel "Time (s)"
set xrange [0:15]
set yrange [0.000001:10000]


set title "Problem Size vs. Time"
set key reverse Left outside
set logscale y 10
set output 'timeplot.png'
set style data linespoints
plot "timeplot.dat" using 1:2 lt 1 lw 2 title 'search_a' , \
     "timeplot.dat" using 1:3 lt 2 lw 2 title 'search_b' , \
     "timeplot.dat" using 1:4 lt 3 lw 2 title 'search_c' , \
     "timeplot.dat" using 1:5 lt 4 lw 2 title 'search_d' , \
     "timeplot.dat" using 1:2 with points title "", \
     "timeplot.dat" using 1:3 with points title "", \
     "timeplot.dat" using 1:4 with points title "", \
     "timeplot.dat" using 1:5 with points title ""