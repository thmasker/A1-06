import src.Graph as Graph
import src.State as State
import math

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
    Method name:
    Description:
    Calling arguments:
    Return value:
    """
    def successors(self, state):
        successorsList = []

        if self.belongNode(state):
            adjacencyList = self.graph.adjacentNode(state)
            for node in adjacencyList:
                newState = State(node[1], [])
                acci = "I'm at " + state.currentPosition + "and I go to " + newState.currentPosition
                costActi = self.calculateDistance(state.currentPosition, newState.currentPosition)
                successorsList.append([acci, newState, costActi])
        else:
            print(state + " does not belong to the graph\n")

    """
    Method name:    belongNode
    Description:    Checks if the state is a feasible state on the current graph
    Calling arguments:  state: a certain state object
    Return value:   Boolean: True if state is feasible; False otherwise
    """
    def belongNode(self, state):
        return self.graph.belongNode(state.currentPosition)

    """
    Method name:    calculateDistance
    Description:    Calculation of the straight line distance between two given nodes
    Calling arguments:  - origin: source node
                        - destination: target node
    Return value:   straight line distance between origin and destination
    """
    def calculateDistance(self, origin, destination):
        return math.sqrt(pow(self.graph.positionNode(origin.currentPosition)[0]
                             - self.graph.positionNode(destination.currentPosition)[0], 2)
                         + pow(self.graph.positionNode(origin.currentPosition)[1]
                                   - self.graph.positionNode(destination.currentPosition)[1], 2))
