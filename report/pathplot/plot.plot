reset
set terminal png size 1024,768
set xlabel "X"
set ylabel "Y"

set xrange [100:650]
set yrange [50:450]

set style data linespoints
set style line 1 lc rgb '#0060ad' lt 1 lw 1 pt 7 ps 0.5
#set key bottom Left inside
set key off


set title "Best Solution on tsp225, Search A"
set output '../images/paths_search_a.png'
plot 'pathdat/pathdat_a_14400.dat' using 2:3 # index 1 with linespoints ls 1

set title "Best Solution on tsp225, Search B"
set output '../images/paths_search_b.png'
plot 'pathdat/pathdat_b_14400.dat' using 2:3 # index 1 with linespoints ls 1

set title "Best Solution on tsp225, Search C"
set output '../images/paths_search_c.png'
plot 'pathdat/pathdat_c_14400.dat' using 2:3 # index 1 with linespoints ls 1

set title "Best Solution on tsp225, Search D"
set output '../images/paths_search_d.png'
plot 'pathdat/pathdat_d_14400.dat' using 2:3 # index 1 with linespoints ls 1
