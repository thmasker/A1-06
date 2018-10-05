import src.Graph as G

"""
Description:    Allows the user to test src.Graph three methods
Checked Exceptions: - FileNotFoundError: thrown if entered file does not exist
                    - TypeError: thrown if node entered is not a number
"""
if __name__ == '__main__':
    graphml = input('Enter full path of \".graphml\" file: ')
    try:
        mygraph = G.Graph(graphml)
    except FileNotFoundError as fnf_error:
        print(fnf_error)

    while True:
        nodeid = input('Write down the node id you want to test: ')
        try:
            int(nodeid)
        except TypeError:
            print(nodeid + 'is not a valid node id')
        else:
            print('Is this node on the graph? ' + str(mygraph.belongNode(nodeid)))
            print('Position (latitude and longitude): ' + str(mygraph.positionNode(nodeid)))
            print('Adjacency list: ' + str(mygraph.adjacentNode(nodeid)))
            break
