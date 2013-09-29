import math
import re
from adjmatrix import AdjMatrix



class TSPGraph:

    def __init__(self, graphfile="tsp25.txt"):
        self.nodelist = []
        self.adjmatrix = None
        self.load_graph(graphfile)
        self.generate_adjmatrix()



    def load_graph(self, filename):
        with open(filename, 'r') as graphfile: 

            if graphfile == None:
                sys.exit("Graph File Non-Existent, ensure file exists.")
                
            for line in graphfile:
                matchobj = re.match(r"DIMENSION : (?P<nodecount>\d+)", line)

                if matchobj != None:
                    self.adjmatrix = AdjMatrix(int(matchobj.group('nodecount')))
                    break

            for line in graphfile:
                matchobj = re.match(r"\s{0,2}(?P<nodeid>\d+) (?P<xcoord>\d+\.\d+) (?P<ycoord>\d+\.\d+)", line)

                if matchobj != None:
                    self.add_node(int(matchobj.group('nodeid'))-1, matchobj.group('xcoord'), matchobj.group('ycoord'))



    def add_node(self, nodeid, xcoord, ycoord):
        self.nodelist.append([int(nodeid), float(xcoord), float(ycoord)])



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



def main():
    t = TSPGraph()
    print t.nodelist
    t.adjmatrix.print_adjmatrix()



if __name__ == '__main__':
    main()
