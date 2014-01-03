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



from timer import Timer
from tspgraph import TSPGraph



class State:

    def __init__(self, graph, visited, tovisit, previous_state=None):
        self.visited = visited[:]
        self.tovisit = tovisit[:]

        # It might be worth it to replace some lists with arrays.
        #self.board = array.array('i', [ -2 for i in range(0, self.max_x*self.max_y) ])

        if previous_state == None:
            self.current_cost = sum([graph.adjmatrix.get_adjvalue(visited[i], visited[i+1]) for i in range(0, len(self.visited)-1)])
        else:
            self.current_cost = previous_state.current_cost + graph.adjmatrix.get_adjvalue(visited[-2], visited[-1])



    def visit(self, graph, node):
        visited = self.visited[:]
        tovisit = self.tovisit[:]

        if node == 0 and len(tovisit) != 1:
            return WorstState()
        elif node in tovisit:
            tovisit.remove(node)
            visited.append(node)
            return State(graph, visited, tovisit, self)
        else:
            return WorstState()



    def is_solution(self):
        # Note: may be able to shave off the second part of this test.
        # This would be done by allowing the algorithm to avoid picking obvious non-hamiltonians.
        if len(self.tovisit) == 0 and self.visited[0] == self.visited[-1]:
            return True
        return False



class WorstState(State):

    def __init__(self):
        State.__init__(self, None, [], [])
        self.current_cost = float("inf")




class Search:

    def search(graph, search, budget):
        searchhash = {
                'a' : Search.r_search_a ,
                'b' : Search.r_search_b ,
                'c' : Search.r_search_c ,
                'd' : Search.r_search_d ,
                }

        with Timer() as t:
            return searchhash[search](graph, State(graph, [0], [x[0] for x in graph.nodelist]), float("inf"), float(budget), t)

    def r_search_a(graph, state, bound, budget, timer):
        if timer.get_secs() > budget or state.current_cost == float("inf") or state.is_solution():
            return state

        best = WorstState()

        for node in state.tovisit:
            result = Search.r_search_a(graph, state.visit(graph, node), bound, budget, timer)

            if best.current_cost > result.current_cost:
                best = result

        return best



    def r_search_b(graph, state, bound, budget, timer):
        if timer.get_secs() > budget or state.current_cost >= bound or state.is_solution():
            return state


        best = WorstState()

        for node in state.tovisit:
            result = Search.r_search_b(graph, state.visit(graph, node), bound, budget, timer)

            if best.current_cost > result.current_cost:
                bound = result.current_cost
                best = result

        return best


    
    def r_search_c(graph, state, bound, budget, timer):
        if timer.get_secs() > budget or state.current_cost >= bound or state.is_solution():
            return state

        state.tovisit = [x[0] for x in sorted([[node, graph.adjmatrix.get_adjvalue(state.visited[-1], node)] for node in state.tovisit], key = lambda sortitem : sortitem[1])]

        best = WorstState()

        for node in state.tovisit:
            result = Search.r_search_c(graph, state.visit(graph, node), bound, budget, timer)

            if best.current_cost > result.current_cost:
                bound = result.current_cost
                best = result

        return best



    # This is the heuristic for search_d.
    def h_search_d(graph, state, node):
        return graph.adjmatrix.get_adjvalue(state.visited[0], node)

    def r_search_d(graph, state, bound, budget, timer):
        if state.current_cost >= bound:
            return WorstState()

        if state.current_cost == float("inf") or state.is_solution():
            return state

        # Find the node the heuristic says to search next. Put them in a list.
        state.tovisit = [x[0] for x in sorted([[node, Search.h_search_d(graph, state, node)] for node in state.tovisit], key = lambda sortitem : sortitem[1])]

        best = WorstState()

        for node in state.tovisit:
            result = Search.r_search_d(graph, state.visit(graph, node), bound, budget, timer)

            if best.current_cost > result.current_cost:
                bound = result.current_cost
                best = result

        return best
