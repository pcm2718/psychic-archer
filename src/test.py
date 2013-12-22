from tspgraph import TSPGraph
from search import Search

import cProfile
import sys

graph = TSPGraph(sys.argv[1], int(sys.argv[2]))
search = Search()

profile.run("search.search_a(graph, 60)", "profile.dat")

# Uncomment this to generate the n vs time plots.
# Run gnuplot with timeplot.plot in the timeplot folder to generate plots.
#s.generate_timedata("../timeplot/timeplot.dat")

# Uncomment this to generate shortest path plots.
# Run gnuplot with pathplot.plot in the pathplot folder to generate plots.
#s.generate_linedata("../pathplot/pathplot.dat")
