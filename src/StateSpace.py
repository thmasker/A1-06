import src.Graph as Graph

"""
Class Name: StateSpace
Description:    Defines the current state space based on the given state
"""
class StateSpace:
    """
    Method name:    __init__
    Description:  Constructor
    Calling arguments:  graphml: path to any .graphml file
    Checked Exceptions: : thrown when the entered file is not a .graphml type
    """
    def __init__(self, graphml):
        self.graph = Graph(graphml)

    def successors(self, state):

    def belongNode(self, state):
        return self.graph.belongNode(state.currentPosition)