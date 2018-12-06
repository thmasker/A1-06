"""
Class Name: TreeNode
Class description:  This class simulates a specific node which belongs to a Tree
"""
class TreeNode:

    """
    Method name:    __init__
    Description of the Method:  Constructor
    Calling arguments:  - parent: TreeNode which precedes the new one
                        - state: current state
                        - pathcost: cost of the path from the initial node to the current one
                        - d: depth of the node
    """
    def __init__(self, parent, state, pathcost, action, d, strategy=0, heuristic=0, cb_distance=None):
        self.parent = parent
        self.state = state
        self.pathcost = pathcost
        self.action = action
        self.d = d
        self.f = self.factory(strategy, heuristic, cb_distance)

    """
    Method name:    factory
    Description:    Calculates the value of f depending of the strategy and heuristic chosen
    Calling arguments:  - strategy: strategy selected
                        - heuristic: heuristic selected
                        - cb_distance: callback to function distance from the Class StateSpace
    Return value:   It returns the f value to assign to the created TreeNode
    """
    def factory(self, strategy, heuristic, cb_distance):
        if strategy == 'bfs':
            return self.d
        elif (strategy == 'dfs') or (strategy == 'dls') or (strategy == 'ids'):
            return -self.d
        elif strategy == 'ucs':
            return self.pathcost
        elif strategy == 'gs':
            if not self.state.nodesRemaining:
                return 0
            else:
                if heuristic == 0:
                    return min(
                        cb_distance(self.state.currentPosition, destNode) for destNode in self.state.nodesRemaining)
                elif heuristic == 1:
                    return min(cb_distance(self.state.currentPosition, destNode) for destNode in self.state.nodesRemaining) \
                           + self.calcHeuristic1(cb_distance)
        elif strategy == 'a*':
            if not self.state.nodesRemaining:
                return self.pathcost
            else:
                if heuristic == 0:
                    return self.pathcost \
                           + min(cb_distance(self.state.currentPosition, destNode) for destNode in self.state.nodesRemaining)
                elif heuristic == 1:
                    return self.pathcost \
                           + min(cb_distance(self.state.currentPosition, destNode) for destNode in self.state.nodesRemaining) \
                           + self.calcHeuristic1(cb_distance)
        elif strategy == 0:
            return 0

    """
    Method name:    calcHeuristic1
    Description:    This method calculates part of the Heuristic1
    Calling arguments:  cb_distance: distance method of Class StateSpace
    Return value:   distance: sum of all minimum distances from each remainingNode to the rest of them
    """
    def calcHeuristic1(self, cb_distance):
        distance = 0

        for node1 in self.state.nodesRemaining:
            distances = []

            for node2 in self.state.nodesRemaining:
                if node1 != node2:
                    distances.append(cb_distance(node1, node2))

            distance += min(distances) if distances else 0

        return distance
