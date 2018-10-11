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
    Checked Exceptions:
    """
    def __init__(self, graphml):
        self.graph = Graph(graphml)

    """
    Method name:    __init__
    Description:  Constructor
    Calling arguments:  graphml: path to any .graphml file
    Return value:
    Checked Exceptions:
    """
    def successors(self, state):


    """
    Method name:    __init__
    Description:  Constructor
    Calling arguments:  graphml: path to any .graphml file
    Return value:
    Checked Exceptions:
    """
    def belongNode(self, state):
        return self.graph.belongNode(state.currentPosition)
