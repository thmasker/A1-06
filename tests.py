import src.Graph as G
import timeit

"""
Description:    Allows the user to test src.Graph three methods
Checked Exceptions: - FileNotFoundError: thrown if entered file does not exist
                    - TypeError: thrown if node entered is not a number
"""
if __name__ == '__main__':
    graphml = input('Enter full path of \".graphml\" file: ')
    try:
        start = timeit.default_timer()
        mygraph = G.Graph(graphml)
        print("Graph file loaded in: ", (timeit.default_timer() - start), " seconds")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        raise SystemExit

    while True:
        nodeid = input('Write down the node id you want to test: ')
        try:
            int(nodeid)
        except TypeError:
            print(nodeid + 'is not a valid node id')
        else:
            print('Is this node on the graph? ' + str(mygraph.belongNode(nodeid)))
            print('Position (latitude and longitude): ' + str(mygraph.positionNode(nodeid)))

            starts = timeit.default_timer()
            print('Adjacency list: ' + str(mygraph.adjacentNode(nodeid)))
            end = timeit.default_timer() - starts
            print("\nAdjacency list loaded in: ", end, " seconds")
            break
