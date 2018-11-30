import src.Graph as G
import src.State as S
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
            print("\n[ERROR] Node '" + state.currentPosition + "' does not belong to the graph\n")
            raise SystemExit

        return successorsList

    """
    Method name:    belongNode
    Description:    Checks if the state is a feasible state on the current graph
    Calling arguments:  state: a certain state object
    Return value:   Boolean: True if state is feasible; False otherwise
    """
    def belongNode(self, state):
        return self.graph.belongNode(state.currentPosition)

    """
    Method name:    distance
    Description:    Calculates the straightline distance between two nodes
    Calling arguments:  - idNode1. Node of the graph
                        - idNode2. Node of the graph
    Return value:   dist. Distance between two nodes in units of earth_radius
    """
    def distance(self, idNode1, idNode2):
        try:
            (lng1, lat1) = self.graph.positionNode(idNode1)
            (lng2, lat2) = self.graph.positionNode(idNode2)
        except ValueError:
            raise SystemExit

        earth_radius = 6371009

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        d_phi = phi2 - phi1

        theta1 = math.radians(lng1)
        theta2 = math.radians(lng2)
        d_theta = theta2 - theta1

        h = math.sin(d_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_theta / 2) ** 2
        h = min(1.0, h)  # protect against floating point errors

        arc = 2 * math.asin(math.sqrt(h))

        # return distance in units of earth_radius
        dist = arc * earth_radius

        return dist
