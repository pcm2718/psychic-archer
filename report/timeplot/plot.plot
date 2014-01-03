reset
set terminal png size 1024,768
set xlabel "Data Set Size (n)"

set ylabel "Time (s)"
set xrange [6:15]
set yrange [0.01:100000]


#set title "Problem Size vs. Time"
set key off
set logscale y 10
set style data points

set title "Search A"
set output '../images/times_search_a.png'
plot 'tmp/times_search_a.dat' using 1:2 # title "Search A"

set title "Search B"
set output '../images/times_search_b.png'
plot 'tmp/times_search_b.dat' using 1:2 # title "Search B"

set title "Search C"
set output '../images/times_search_c.png'
plot 'tmp/times_search_c.dat' using 1:2 # title "Search C"

set title "Search D"
set output '../images/times_search_d.png'
plot 'tmp/times_search_d.dat' using 1:2 # title "Search D"


set title "Averages"
set style data linespoints
set key bottom Right inside
set output '../images/times_avgs.png'
plot 'tmp/avg_search_a.dat' using 1:2 title "Search A" , \
     'tmp/avg_search_b.dat' using 1:2 title "Search B" , \
     'tmp/avg_search_c.dat' using 1:2 title "Search C" , \
     'tmp/avg_search_d.dat' using 1:2 title "Search D"
