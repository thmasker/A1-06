import src.Graph as G
import src.State as S

"""
Class Name: StateSpace
Description:    Defines the current state space based on the given state
"""
class StateSpace:
    """
    Method name:    __init__
    Description:  Constructor
    Calling arguments:  graphml: path to any .graphml file
    """
    def __init__(self, graphml):
        self.graph = G.Graph(graphml)

    """
    Method name:    successors
    Description:    Calculates the successors of a given state
    Calling arguments:  state: a specific state
    Return value:   successorsList: list with all generated successors
    Checked Exceptions: ValueError: when removing the destination node from the nodesRemaining list,
                            if this node does not exist on it
    """
    def successors(self, state):
        successorsList = []

        if self.belongNode(state):
            adjacencyList = self.graph.adjacentNode(state.currentPosition)

            for node in adjacencyList:
                newNodesRemaining = state.nodesRemaining.copy()

                try:
                    newNodesRemaining.remove(node[1])
                except ValueError:
                   pass

                newState = S.State(node[1], newNodesRemaining)
                acci = "I'm at " + state.currentPosition + " and I go to " + newState.currentPosition
                costActi = node[3]
                successorsList.append((acci, newState, costActi))
        else:
            print(state + " does not belong to the graph\n")

        return successorsList

    """
    Method name:    belongNode
    Description:    Checks if the state is a feasible state on the current graph
    Calling arguments:  state: a certain state object
    Return value:   Boolean: True if state is feasible; False otherwise
    """
    def belongNode(self, state):
        return self.graph.belongNode(state.currentPosition)
