import xml.etree.ElementTree as ET

class Graph:
    def __init__(self, graphml):
        self.file = graphml
        self.graph = ET.parse(self.file).getroot()

        self.ns = { 'default': 'http://graphml.graphdrawing.org/xmlns' } # ns = name space

        self.nodes = self.graph.findall('default:graph/default:node', self.ns)


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


    #def adjacentNode(nodeid):

if __name__ == '__main__':
    anchuras = Graph('../data/Anchuras.graphml')

