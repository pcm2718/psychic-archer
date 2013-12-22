# Parker Michaleson
# A01248939
# parker.michaelson@gmail.com
# Assignment #2

# This file contains the AdjMatrix class. AdjMatrix is a class representing an
# adjacency matrix, and includes functions for setting and getting the
# adjacency value of two nodes.



class AdjMatrix:

    def __init__(self, nodecount):
        self.nodecount = nodecount
        self.matrix = [0 for i in range(0, nodecount*nodecount)]



    def set_adjvalue(self, m, n, adjvalue):
        if m >= self.nodecount or n >= self.nodecount:
            raise ValueError("Invalid node access.")

        self.matrix[self.nodecount*m + n] = adjvalue
        self.matrix[self.nodecount*n + m] = adjvalue



    def get_adjvalue(self, m, n):
        if m >= self.nodecount or n >= self.nodecount:
            raise ValueError("Invalid node access.")

        return self.matrix[self.nodecount*n + m]



    def __str__(self):
        retstr  = "\n\n",
        retstr += "["

        for i in range(0, self.nodecount):
            for j in range(0, self.nodecount):
                retstr += '{:>6,.2f}'.format(self.matrix[self.nodecount*i + j]),
                retstr += ',',
            retstr += "\n",

        retstr += "]"
        retstr += "\n\n",

