import xml.etree.ElementTree as ET

class Graph:
    def __init__(self, graphml):
        self.file = graphml
        self.graph = ET.parse(self.file).getroot()

        self.ns = {'default': 'http://graphml.graphdrawing.org/xmlns'}  # ns = name space
        self.keys = {} 

        for key in self.graph.findall('default:key', self.ns):      # Store edge keys
            if key.get('for') == 'edge':
                self.keys[key.get('attr.name')] = key.get('id')

        self.nodes = self.graph.findall('default:graph/default:node', self.ns)      # Store nodes
        self.edges = self.graph.findall('default:graph/default:edge', self.ns)      # Store edges

    def belongNode(self, nodeid):
        for node in self.nodes:
            if nodeid == node.get('id'):
                return True

        return False

    def positionNode(self, nodeid):
        for node in self.nodes:
            if nodeid == node.get('id'):
                return node[1].text, node[0].text

        return '[ERROR] Node does not exist on the graph'

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

if __name__ == '__main__':
    anchuras = Graph('data/Ciudad Real.graphml')
    print(anchuras.adjacentNode('1386521977'))
