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
        except ET.ParseError:
            print('\n' + graphml + ' is not a \".graphml\" or is it corrupted')
            raise SystemExit
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            raise SystemExit

        self.ns = {'default': 'http://graphml.graphdrawing.org/xmlns'}  # ns = name space
        self.keys = {} 

        for key in self.graph.findall('default:key', self.ns):      # Store edge keys
            if key.get('for') == 'edge':
                self.keys[key.get('attr.name')] = key.get('id')

        self.nodes = self.graph.findall('default:graph/default:node', self.ns)      # Store nodes
        self.edges = self.graph.findall('default:graph/default:edge', self.ns)      # Store edges

    """
    Method name:    belongNode
    Description:  Analyze if the entered id belongs to a node in the graph
    Calling arguments:  nodeid: node to identify its belonging to the graph
    Return value: Boolean: True if nodeid exists on the graph; False otherwise
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
        if self.belongNode(nodeid):
            for node in self.nodes:
                if nodeid == node.get('id'):
                    return float(node[1].text), float(node[0].text)
        else:
            raise ValueError

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
                    adjacencyList.append((edge.get('source'), edge.get('target'), 'SinNombre', 'NULL'))

                    for data in edge:
                        if data.get('key') == self.keys['name']:
                            lst = list(adjacencyList[-1])
                            lst[2] = data.text
                            adjacencyList[-1] = tuple(lst)
                        elif data.get('key') == self.keys['length']:
                            lst = list(adjacencyList[-1])
                            lst[3] = data.text
                            adjacencyList[-1] = tuple(lst)
        else:
            adjacencyList = '[ERROR] Node does not exist on the node'

        return adjacencyList
