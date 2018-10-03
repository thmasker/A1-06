import xml.etree.ElementTree as ET

class Graph:
    def __init__(self, graphml):
        self.file = graphml
        self.graph = ET.parse(self.file).getroot()

        self.ns = {'default': 'http://graphml.graphdrawing.org/xmlns'}  # ns = name space
        self.nodes = self.graph.findall('default:graph/default:node', self.ns)
        self.edges = self.graph.findall('default:graph/default:edge', self.ns)

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
                    adjacencyList.append((edge.get('source'), edge.get('target'),
                                          edge[1].text if edge[1].get('key') == 'd13' else 'SinNombre', edge[4].text))
        else:
            adjacencyList = '[ERROR] Node does not exist on the node'

        return adjacencyList

if __name__ == '__main__':
    anchuras = Graph('../data/Anchuras.graphml')
    print(anchuras.adjacentNode('4331489627'))