import xml.etree.ElementTree as ET

"""
Class Name: Graph
Description:  Reads .graphml files and allows users obtain different graph information
"""
class Graph:
    """
    Method name:    __init__
    Description:  Constructor. Reads and stores relevant information about entered file
    Calling arguments:  graphml: path to any .graphml file
    Checked Exceptions: ElementTree.ParseError: thrown when the entered file is not a .graphml type
    """
    def __init__(self, graphml):
        self.file = graphml
        try:
            self.graph = ET.parse(self.file).getroot()
        except ET.ParseError as parserror:
            print('\n' + graphml + ' is not a \".graphml\" or is it corrupted')
            return

        self.ns = {'default': 'http://graphml.graphdrawing.org/xmlns'}  # ns = name space
        self.nodes = self.graph.findall('default:graph/default:node', self.ns)
        self.edges = self.graph.findall('default:graph/default:edge', self.ns)

    """
    Method name:    belongNode
    Description:  Analyze if the entered id belongs to a node in the graph
    Calling arguments:  nodeid: node to identify its belonging to the graph
    Return value: Boolean: true if nodeid exists on the graph; False otherwise
    """
    def belongNode(self, nodeid):
        for node in self.nodes:
            if nodeid == node.get('id'):
                return True

        return False

    """
    Method name:    positionNode
    Description:  finds the node geographical position on Earth
    Calling arguments:  nodeid: any graph's node
    Return value: Tuple containing latitude and longitude of node if it belongs to the graph. Error otherwise
    """
    def positionNode(self, nodeid):
        for node in self.nodes:
            if nodeid == node.get('id'):
                return node[1].text, node[0].text

        return '[ERROR] Node does not exist on the graph'

    """
    Method name:    adjacentNode
    Description:  Finds all adjacent nodes of a specified node in the graph
    Calling arguments:  nodeid: any graph's node
    Return value: List of Tuples: each tuple is an adjacent node found
    """
    def adjacentNode(self, nodeid):
        adjacencyList = []

        if self.belongNode(nodeid):
            for edge in self.edges:
                if edge.get('source') == nodeid:
                    adjacencyList.append((edge.get('source'), edge.get('target')))

                    for data in edge:
                        if data.get('key') == 'd13':
                            adjacencyList[-1] = adjacencyList[-1] + (data.text,)
                        elif data.get('key') == 'd14':
                            adjacencyList[-1] = adjacencyList[-1] + ('SinNombre',)
                        elif data.get('key') == 'd11':
                            adjacencyList[-1] = adjacencyList[-1] + (data.text,)
        else:
            adjacencyList = '[ERROR] Node does not exist on the node'

        return adjacencyList