# Parker Michaleson
# A01248939
# parker.michaelson@gmail.com
# Assignment #2

# This file contains three classes.

# The class State represents the state of a search at some node. It
# incorperates information such as the current search path, unvisited nodes,
# and the current cost of the path it represents. It also contains a reference
# to the TSPGraph object being searched and functions representing operators.

# The class WorstState is a subclass of State, and represents a state where no
# path exists and with an infinite cost. It is used as a convinience in the 
# search of the solution space.

# The class SolutionSearch contains functions for searching a problem 
# represented by TSPGraph:
#
#       search_a is a brute force search of the solution space.
#       search_b is an improved version of search_a, where exploration is
#           bounded by the current best length path.
#       search_c is an improved version of search_b, which attempts to explore
#           nodes closer to the current node before ones that are more distant.
#       search_d is an improved version of search_b, with a heureistic
#           instructing it at any step to try the node closest to the starting
#           node.
#



import time
from timer import Timer
from tspgraph import TSPGraph



class State:

    def __init__(self, graph, visited_list, visit_list, previous_state=None):
        self.graph = graph

        self.visited_list = visited_list[:]
        self.visit_list = visit_list[:]

        if previous_state == None:
            self.current_cost = 0
            for i in range(0, len(self.visited_list)-1):
                self.current_cost += graph.adjmatrix.get_adjvalue(visited_list[i], visited_list[i+1])
        else:
            self.current_cost = previous_state.current_cost
            self.current_cost += graph.adjmatrix.get_adjvalue(visited_list[-2], visited_list[-1])



    def visit_node(self, to_node):
        visited_list = self.visited_list[:]
        visit_list = self.visit_list[:]

        if to_node == 0 and len(visit_list) != 1:
            return WorstState()
        elif to_node in visit_list:
            visit_list.remove(to_node)
            visited_list.append(to_node)
            return State(self.graph, visited_list, visit_list)
        else:
            return WorstState()



    def is_solution(self):
        if len(self.visit_list) == 0 and self.visited_list[0] == self.visited_list[-1]:
            return True
        else:
            return False



class WorstState(State):

    def __init__(self):
        State.__init__(self, None, [], [])
        self.current_cost = float("inf")




class SolutionSearch:

    def __init__(self):
        # Time limit is given in seconds.
        self.timelimit = 1000



    # This function for diagnostic purposes only.
    def search(self, func, graph):
        with Timer() as t:
            s = func(g, t)
        print ""
        print func.__name__ + ":"
        print "Elapsed Time: %(secs)s s %(msecs)f ms" % {"secs": t.secs, "msecs": t.msecs}
        print map(lambda node: graph.idlookup[node], s.visited_list)
        print s.current_cost

    def generate_timedata(self, outfile_name):
        funclist = [self.search_a, self.search_b, self.search_c, self.search_d]
        
        outfile = open(outfile_name, 'w')

        for x in range(1, 14):
            for y in range (0, 4):
                graph = TSPGraph('tsp225.txt', x)
                reslist = []
                for func in funclist:
                    with Timer() as t:
                        s = func(graph, t)

                    reslist.append(t.secs)

                    print ""
                    print "# " + str(len(graph.nodelist)) + " nodes, " + func.__name__
                    print "# " + str([node for node in s.visited_list])
                    print "# " + str([graph.idlookup[node] for node in s.visited_list])
                    print "# " + str(s.current_cost)
                    print str(len(graph.nodelist)) + " " + str(t.secs) + " " + str(funclist.index(func))
                    print ""

                outfile.write(str(len(graph.nodelist)) + " " + ' '.join(map(lambda x: str(x), reslist)) + "\n")

        outfile.close()

    def generate_linedata(self, func, graph):
#  for x in range(1, 11):
#    for y in range (0, 4):
#        g = TSPGraph('tsp225.txt', x)

#        s.generate_timedata(s.search_a, g)
#        s.generate_timedata(s.search_b, g)
#        s.generate_timedata(s.search_c, g)
#        s.generate_timedata(s.search_d, g)

        with Timer() as t:
            s = func(g, t)
        print ""
        print "# " + str(len(graph.nodelist)) + " nodes, " + func.__name__
        print "# " + str([node for node in s.visited_list])
        print "# " + str([graph.idlookup[node] for node in s.visited_list])
        print "# " + str(s.current_cost)
        print str(len(graph.nodelist)) + " " + str(t.secs)
        print ""




    def search_a(self, graph, timer):
        nodelist = []
        for node in graph.nodelist:
            nodelist.append(node[0])

        return self.r_search_a(State(graph, [0], nodelist), timer)

    def r_search_a(self, state, timer):
        if state.current_cost == float("inf") or state.is_solution():
            return state

        best = WorstState()

        for node in state.visit_list:
            if time.time() - timer.start > self.timelimit:
                break

            next_state = state.visit_node(node)
            result = self.r_search_a(next_state, timer)

            if best.current_cost > result.current_cost:
                best = result

        return best



    def search_b(self, graph, timer):
        nodelist = []
        for node in graph.nodelist:
            nodelist.append(node[0])

        return self.r_search_b(State(graph, [0], nodelist), float("inf"), timer)

    def r_search_b(self, state, bound, timer):
        if state.current_cost >= bound:
            return WorstState()

        if state.current_cost == float("inf") or state.is_solution():
            return state


        best = WorstState()

        for node in state.visit_list:
            if time.time() - timer.start > self.timelimit:
                break

            next_state = state.visit_node(node)
            result = self.r_search_b(next_state, bound, timer)

            if best.current_cost > result.current_cost:
                bound = result.current_cost
                best = result

        return best


    
    def search_c(self, graph, timer):
        nodelist = []
        for node in graph.nodelist:
            nodelist.append(node[0])

        return self.r_search_c(State(graph, [0], nodelist), float("inf"), timer)

    def r_search_c(self, state, bound, timer):
        if state.current_cost >= bound:
            return WorstState()

        if state.current_cost == float("inf") or state.is_solution():
            return state


        current_node = state.visited_list[-1]
        sortlist = []
        for node in state.visit_list:
            sortlist.append([node, state.graph.adjmatrix.get_adjvalue(node, current_node)])
        sorted(sortlist, key = lambda sortitem : sortitem[1])
        state.visit_list = []
        for node in sortlist:
            state.visit_list.append(node[0])
       

        best = WorstState()

        for node in state.visit_list:
            if time.time() - timer.start > self.timelimit:
                break

            next_state = state.visit_node(node)
            result = self.r_search_c(next_state, bound, timer)

            if best.current_cost > result.current_cost:
                bound = result.current_cost
                best = result

        return best



    def search_d(self, graph, timer):
        nodelist = []
        for node in graph.nodelist:
            nodelist.append(node[0])

        return self.r_search_d(State(graph, [0], nodelist), float("inf"), timer)

    # This is the heuristic for search_d.
    def h_search_d(self, state, node, choice):
        return state.graph.adjmatrix.get_adjvalue(state.visited_list[0], choice)

    def r_search_d(self, state, bound, timer):
        if state.current_cost >= bound:
            return WorstState()

        if state.current_cost == float("inf") or state.is_solution():
            return state


        # Find the node the heuristic says to search next. Put them in a list.
        current_node = state.visited_list[-1]
        sortlist = []
        for choice in state.visit_list:
            sortlist.append([choice, self.h_search_d(state, current_node, choice)])
        sorted(sortlist, key = lambda sortitem : sortitem[1])
        state.visit_list = []
        for node in sortlist:
            state.visit_list.append(node[0])


        best = WorstState()

        for node in state.visit_list:
            if time.time() - timer.start > self.timelimit:
                break

            next_state = state.visit_node(node)
            result = self.r_search_d(next_state, bound, timer)

            if best.current_cost > result.current_cost:
                bound = result.current_cost
                best = result

        return best





s = SolutionSearch()
s.generate_timedata("timedata.dat")
