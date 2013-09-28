import re



class TSPGraph:

    def __init__(self):
        self.nodelist = []
        self.load_graph('tsp25.txt')



    def load_graph(self, filename):
        with open(filename, 'r') as graphfile: 

            if graphfile == None:
                sys.exit("Graph File Non-Existent, ensure file exists.")

            for line in graphfile:
                matchobj = re.match(r"\s{0,2}(?P<nodeid>\d+) (?P<xcoord>\d+\.\d+) (?P<ycoord>\d+\.\d+)", line)

                if matchobj != None:
                    self.add_node(matchobj.group('nodeid'), matchobj.group('xcoord'), matchobj.group('ycoord'))



    def add_node(self, nodeid, xcoord, ycoord):
        self.nodelist.append([nodeid, xcoord, ycoord])



def main():
    t = TSPGraph()
    print t.nodelist



if __name__ == '__main__':
    main()
