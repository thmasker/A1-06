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
    def __init__(self, parent, state, pathcost, action, d):
        self.parent = parent
        self.state = state
        self.pathcost = pathcost
        self.action = action
        self.d = d
        self.f = random.randint(1, 10000)
