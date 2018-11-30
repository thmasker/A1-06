import random

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
    def __init__(self, parent, state, pathcost, action, d, strategy = 0, heuristic = 0, cb_distance = None):
        self.parent = parent
        self.state = state
        self.pathcost = pathcost
        self.action = action
        self.d = d
        self.f = self.factory(strategy, heuristic, cb_distance)

    def factory(self, type, heuristic, cb_distance):
        if type == 'bfs':
            return self.d
        elif (type == 'dfs') or (type == 'dls') or (type == 'ids'):
            return -self.d
        elif type == 'ucs':
            return self.pathcost
        elif type == 'gs':
            if not self.state.nodesRemaining:
                return 0
            else:
                if heuristic == 0:
                    return min(cb_distance(self.state.currentPosition, destNode) for destNode in self.state.nodesRemaining)
        elif type == 'a*':
            if not self.state.nodesRemaining:
                return self.pathcost
            else:
                if heuristic == 0:
                    return self.pathcost \
                            + min(cb_distance(self.state.currentPosition, destNode) for destNode in self.state.nodesRemaining)
        elif type == 0:
            return 0

       
