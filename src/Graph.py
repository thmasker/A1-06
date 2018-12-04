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
        self.nodes = {}
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

        nodes = self.graph.findall('default:graph/default:node', self.ns)      # Store nodes
        edges = self.graph.findall('default:graph/default:edge', self.ns)      # Store edges

        for node in nodes:
            self.nodes[node.get('id')] = {}
            self.nodes[node.get('id')]['adjacencyList'] = []
            self.nodes[node.get('id')]['latitude'] = node[0].text
            self.nodes[node.get('id')]['longitude'] = node[1].text

        for edge in edges:
            self.nodes[edge.get('source')]['adjacencyList']\
                .append((edge.get('source'), edge.get('target'), 'SinNombre', 'NULL'))

            for data in edge:
                if data.get('key') == self.keys['name']:
                    lst = list(self.nodes[edge.get('source')]['adjacencyList'][-1])
                    lst[2] = data.text
                    self.nodes[edge.get('source')]['adjacencyList'][-1] = tuple(lst)
                elif data.get('key') == self.keys['length']:
                    lst = list(self.nodes[edge.get('source')]['adjacencyList'][-1])
                    lst[3] = data.text
                    self.nodes[edge.get('source')]['adjacencyList'][-1] = tuple(lst)

    """
    Method name:    belongNode
    Description:  Analyze if the entered id belongs to a node in the graph
    Calling arguments:  nodeid: node to identify its belonging to the graph
    Return value: Boolean: True if nodeid exists on the graph; False otherwise
    """
    def belongNode(self, nodeid):
        if nodeid in self.nodes:
            return True
        else:
            return False

    """
    Method name:    positionNode
    Description:  finds the node geographical position on Earth
    Calling arguments:  nodeid: any graph's node
    Return value: Tuple containing latitude and longitude of node if it belongs to the graph. Error otherwise
    """
    def positionNode(self, nodeid):
        if self.belongNode(nodeid):
            return float(self.nodes[nodeid]['longitude']), float(self.nodes[nodeid]['latitude'])
        else:
            print("\n[ERROR] Node '" + nodeid + "' does not exist on the graph")
            raise ValueError

    """
    Method name:    adjacentNode
    Description:  Finds all adjacent nodes of a specified node in the graph
    Calling arguments:  nodeid: any graph's node
    Return value: List of Tuples: each tuple is an adjacent node found
    """
    def adjacentNode(self, nodeid):
        if self.belongNode(nodeid):
            return self.nodes[nodeid]['adjacencyList']
        else:
            print("\n[ERROR] Node '" + nodeid + "' does not exist on the graph")
            raise SystemExit
