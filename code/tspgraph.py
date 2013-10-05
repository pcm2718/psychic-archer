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



class TSPGraph:

    def __init__(self, graphfile="tsp225.txt", nodecount=None):
        self.nodelist = []
        self.idlookup = []
        self.adjmatrix = None
        self.load_graph(graphfile, nodecount)
        self.generate_adjmatrix()



    def load_graph(self, filename, nodecount):
        with open(filename, 'r') as graphfile: 

            if graphfile == None:
                sys.exit("Graph File Non-Existent, ensure file exists.")
           
            linecount = 0
            for line in graphfile:
                matchobj = re.match(r"DIMENSION : (?P<linecount>\d+)", line)

                if matchobj != None:
                    linecount = int(matchobj.group('linecount'))
                    break
            graphfile.seek(0)

            self.adjmatrix = AdjMatrix(nodecount)

            startline = random.randint(0, linecount - nodecount)
            for i in range(0, 6 + startline):
                graphfile.next()

            for line in graphfile:
                matchobj = re.match(r"\s{0,2}(?P<nodeid>\d+) (?P<xcoord>\d+\.\d+) (?P<ycoord>\d+\.\d+)", line)

                if matchobj != None:
                    if int(matchobj.group('nodeid'))-startline-1 >= nodecount:
                        break
                    else:
                        self.add_node(int(matchobj.group('nodeid')), int(matchobj.group('nodeid'))-startline-1, matchobj.group('xcoord'), matchobj.group('ycoord'))



    def add_node(self, nodeid, nodeindex, xcoord, ycoord):
        self.nodelist.append([int(nodeindex), float(xcoord), float(ycoord)])
        self.idlookup.append(nodeid)



    def generate_adjmatrix(self):
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
