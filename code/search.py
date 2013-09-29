#import timeit
from timer import Timer
from tspgraph import TSPGraph



class State:

    def __init__(self, graph, visited_list, visit_list, previous_state=None):
        self.graph = graph

        self.visited_list = visited_list[:]
        self.visit_list = visit_list[:]

        # Might be able to elimiate first statement.
        if previous_state == None:
            # We could improve this by using the previous cost, will fix later.
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
        pass



    def search_a(self, graph):
        nodelist = []
        for node in graph.nodelist:
            nodelist.append(node[0])

        return self.r_search_a(State(graph, [0], nodelist))

    def r_search_a(self, state):
        if state.current_cost == float("inf") or state.is_solution():
            return state

        best = WorstState()

        for node in state.visit_list:
            next_state = state.visit_node(node)
            result = self.r_search_a(next_state)

            if best.current_cost > result.current_cost:
                best = result

        return best



    def search_b(self, graph):
        nodelist = []
        for node in graph.nodelist:
            nodelist.append(node[0])

        return self.r_search_b(State(graph, [0], nodelist), float("inf"))

    def r_search_b(self, state, bound):
        if state.current_cost >= bound:
            return WorstState()

        if state.current_cost == float("inf") or state.is_solution():
            return state


        best = WorstState()

        for node in state.visit_list:
            next_state = state.visit_node(node)
            result = self.r_search_b(next_state, bound)

            if best.current_cost > result.current_cost:
                bound = result.current_cost
                best = result

        return best


    
    # WARNING: search_c may not yet be functional, more testing will be required to evaluate
    # its functionality.
    def search_c(self, graph):
        nodelist = []
        for node in graph.nodelist:
            nodelist.append(node[0])

        return self.r_search_c(State(graph, [0], nodelist), float("inf"))

    def r_search_c(self, state, bound):
        if state.current_cost >= bound:
            return WorstState()

        if state.current_cost == float("inf") or state.is_solution():
            return state


        # This might break the code due to the duplicate start node.
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
            next_state = state.visit_node(node)
            result = self.r_search_c(next_state, bound)

            if best.current_cost > result.current_cost:
                bound = result.current_cost
                best = result

        return best



def search(func, graph):
    with Timer() as t:
        s = func(g)
    print ""
    print func.__name__ + ":"
    print "Elapsed Time: %(secs)s s %(msecs)f ms" % {"secs": t.secs, "msecs": t.msecs}
    print s.visited_list
    print s.current_cost



g = TSPGraph('tsp15.txt')
s = SolutionSearch()

search(s.search_a, g)
search(s.search_b, g)
# WARNING: search_c may not yet work
search(s.search_c, g)
