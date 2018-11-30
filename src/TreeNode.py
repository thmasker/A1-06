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
    def __init__(self, parent, state, pathcost, action, d, strategy, heuristic):
        self.parent = parent
        self.state = state
        self.pathcost = pathcost
        self.action = action
        self.d = d
        self.f = self.factory(strategy, heuristic)

    def factory(self, type, heuristic):
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
                    return min(self.state.distance(node.state.currentPosition, destNode) for destNode in node.state.nodesRemaining)
        elif type == 'a*':
            if not self.state.nodesRemaining:
                return node.pathcost
            else:
                if heuristic == 0:
                    return self.pathcost \
                            + min(self.state.distance(node.state.currentPosition, destNode) for destnode in self.state.nodesRemaining)
        elif type == 0:
            return 0

       
