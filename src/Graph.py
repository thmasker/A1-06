import xml.etree.ElementTree as ET

class Graph:
    def __init__(self, graphml):
        self.file = graphml
        self.graph = ET.parse(self.file).getroot()

        self.ns = { 'default': 'http://graphml.graphdrawing.org/xmlns' } # ns = name space

        self.nodes = self.graph.findall('default:graph/default:node', self.ns)


    def BelongNode(self, nodeid):
        isNode = False

        for node in self.nodes:
            if nodeid == node.get('id'):
                isNode = True
                break

        return isNode



    #def positionNode(nodeid):


    #def adjacentNode(nodeid):

if __name__ == '__main__':
    anchuras = Graph('data/Anchuras.graphml')
    anchuras.BelongNode('4928063639')
