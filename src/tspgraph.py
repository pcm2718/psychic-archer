# Parker Michaelson
# A01248939
# parker.michaelson@gmail.com
# Assignment #2

# This file contains the TSPGraph class. TSPGraph is a class representing
# "static" information about the graph, information that does not change
# while a search is in progress. This includes a list of nodes and
# coordinates, an adjacency matrix for the nodes whose values are distances
# between adjacent nodes and a lookup table to correlate the number of a node
# in the source file with its internal representation. The class includes
# utility functions for constructing itself.



import math
import random
import re
from adjmatrix import AdjMatrix

import sys



class TSPGraph:

    def __init__(self):
        self.nodelist = []
        self.idlookup = []
        self.adjmatrix = None
        self.read_graph()
        self.generate_adjmatrix()



    def read_graph(self):
        for line in sys.stdin:
            # May restore index variable. This area kind of hacky.
            nodeid, xcoord, ycoord = list(map(float, line.split()))
            self.nodelist.append([len(self.nodelist), float(xcoord), float(ycoord)])
            self.idlookup.append(int(nodeid))



    def generate_adjmatrix(self):
        self.adjmatrix = AdjMatrix(len(self.nodelist))

        # Try to fix the redundant assignments later.
        for n in self.nodelist:
            for m in self.nodelist[n[0]:len(self.nodelist)]:
                if m == n:
                    self.adjmatrix.set_adjvalue(n[0], m[0], 0)
                else:
                    deltax = n[1] - m[1]
                    deltay = n[2] - m[2]
                    distance = math.sqrt(math.pow(deltax, 2) + math.pow(deltay, 2))
                    self.adjmatrix.set_adjvalue(n[0], m[0], distance)
