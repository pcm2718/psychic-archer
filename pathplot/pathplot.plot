reset
set terminal png size 1024,768
set xlabel "X"
set ylabel "Y"

set xrange [0:650]
set yrange [0:650]

set key reverse Left outside

set style line 1 lc rgb '#0060ad' lt 1 lw 1 pt 7 ps 0.5

set title "Shortest Path Across tsp225.txt, search_a"
set output 'search_a.png'
plot	'pathplot.dat'	index 0 with linespoints ls 1

set title "Shortest Path Across tsp225.txt, search_b"
set output 'search_b.png'
plot	'pathplot.dat'	index 1 with linespoints ls 1

set title "Shortest Path Across tsp225.txt, search_c"
set output 'search_c.png'
plot	'pathplot.dat'	index 2 with linespoints ls 1

set title "Shortest Path Across tsp225.txt, search_d"
set output 'search_d.png'
plot	'pathplot.dat'	index 3 with linespoints ls 1

