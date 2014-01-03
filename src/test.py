from tspgraph import TSPGraph
from search import Search

import cProfile
import sys

graph = TSPGraph()
res = Search.search(graph, sys.argv[1], sys.argv[2])
print(res.current_cost, '!', [graph.idlookup[x] for x in res.visited])
#cProfile.run("Search.search(graph, sys.argv[1], sys.argv[2])") #, "profile.dat")
