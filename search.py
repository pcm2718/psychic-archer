from tspgraph import TSPGraph



class State:

    def __init__(self, graph, visited_list, visit_list):
        self.graph = graph

        self.visited_list = visited_list[:]
        self.visit_list = visit_list[:]

        # We could improve this by using the previous cost, will fix later.
        self.current_cost = 0
        for i in range(0, len(self.visited_list)-1):
            self.current_cost += graph.adjmatrix.get_adjvalue(visited_list[i], visited_list[i+1])



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



    def exhaustive_dhs(self, graph):
        nodelist = []
        for node in graph.nodelist:
            nodelist.append(node[0])

        return self.r_exhaustive_dhs(State(graph, [0], nodelist))

    # Should this be iterative?
    def r_exhaustive_dhs(self, state):
        if state.current_cost == float("inf") or state.is_solution():
            return state

        best = WorstState()
        results = []

        print state.visit_list

        for node in state.visit_list:
            next_state = state.visit_node(node)
            results.append(self.r_exhaustive_dhs(next_state))

        print state.visit_list
        print results

        for result in results:
            if best.current_cost > result.current_cost:
                best = result

        return best



g = TSPGraph()
s = SolutionSearch()
sol = s.exhaustive_dhs(g)
print sol.visited_list
print sol.current_cost
