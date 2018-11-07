import src.Problem as P
import src.Frontier as F
import src.TreeNode as TN
from blist import blist

"""
Class Name: Search
Description:    Class containing the searching algorithms
"""
class Search:
    """
    Method name:    __init__
    Description:    creates the problem and initiates searching algorithms
    """
    def __init__(self, jsonPath, strategy, max_depth, inc_depth, pruning):
        self.problem = P.Problem(jsonPath)
        if strategy == 'ids':
            self.solution = self.search(self.problem, strategy, max_depth, inc_depth, pruning)
        else:
            self.solution = self.search(self.problem, strategy, max_depth, max_depth, pruning)

    """
    Method name:    search
    Description:    starts the searching procedures
    Calling arguments:  - problem. Problem to solve
                        - strategy. Strategy which algorithms must follow to solve the problem
                        - max_depth. Maximum depth algorithms are allowed to reach before stopping
                        - inc_depth. Increment to perform every time a search is done
                        - pruning. Indicates if we must take into account repeated states in the frontier
    Return value:   solution. Solution found. If the algorithm did not find solution it returns None
    """
    def search(self, problem, strategy, max_depth, inc_depth, pruning):
        current_depth = inc_depth
        solution = None

        while not solution and (current_depth <= max_depth):
            solution = self.fenced_search(problem, strategy, max_depth, pruning)
            current_depth += inc_depth

        return solution

    """
    Method name:    fenced_search
    Description:    This method performs the algorithms itself
    Calling arguments:  - problem. Problem to solve
                        - strategy. Strategy which algorithms must follow to solve the problem
                        - max_depth. Maximum depth algorithms are allowed to reach before stopping
                        - pruning. Indicates if we must take into account repeated states in the frontier
    Return value:   solution. Solution found. If the algorithm did not find solution it returns False
    """
    def fenced_search(self, problem, strategy, max_depth, pruning):
        frontier = F.Frontier()

        initial_node = TN.TreeNode(None, self.problem.InitState, 0, None, 0)
        initial_node.f = 0

        # With pruning we should prove initial node is not in the frontier before inserting
        frontier.insert(initial_node)

        solution = False

        while not solution and not frontier.isEmpty():
            current_node = frontier.remove()

            if problem.isGoal(current_node.state):
                solution = True
            else:
                successorsList = problem.StateSpace.successors(current_node.state)
                treenodesList = self.createTreeNodes(successorsList, current_node, max_depth, strategy)

                # With pruning we should prove every node in treenodesList is not in the frontier before inserting,
                #   also take into account if it is in the list, the f value...
                for node in treenodesList:
                    frontier.insert(node)

        if solution:
            return self.createSolution(current_node)
        else:
            return False

    """
    Method name:    createTreeNodes
    Description:    This method generate the children nodes of current_node entered
    Calling arguments:  - successorsList. List of successors states from the current state
                        - current_node. Current node the algorithm is in.
                        - max_depth. Maximum depth at which the algorithm must stop
                        - strategy. Strategy to follow to generate nodes.
    Return value:   treeNodesList. List of all children nodes generated
    """
    def createTreeNodes(self, successorsList, current_node, max_depth, strategy):
        treeNodesList = blist([])

        if current_node.d < max_depth:
            for successor in successorsList:
                node = TN.TreeNode(current_node, successor[1], current_node.pathcost + successor[2], successor[0],
                                  current_node.d + 1)

                if strategy == 'bfs':
                    node.f = node.d
                elif (strategy == 'dfs') or (strategy == 'dls') or (strategy == 'dls'):
                    node.f = -node.d
                elif strategy == 'ucs':
                    node.f = node.pathcost

                treeNodesList.append(node)

        return treeNodesList

    """
    Method name:    createSolution
    Description:    Creates a list with all the treeNodes which make the solution found
    Calling arguments:  current_node. Goal node of the problem.
    Return value:   solution. List with the path to follow from the initial state to the goal state
    """
    def createSolution(self, current_node):
        solution = blist([])

        while current_node.parent is not None:
            solution.append(current_node)
            current_node = current_node.parent

        return solution.reverse()
