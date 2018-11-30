import src.Search as S
import os
import timeit
import datetime
import gpxpy.gpx

if __name__ == '__main__':
    try:
        max_depth = int(input('Write down the maximum depth desired: '))
    except ValueError:
        print("[ValueError] Not valid type. Must be an integer")
        raise SystemExit

    try:
        inc_depth = int(input('Write down the increment of depth desired: '))
    except ValueError:
        print("[ValueError] Not valid type. Must be an integer")
        raise SystemExit

    pruning = input('Do you want to use pruning? (y/n) ')

    if pruning == 'y':
        pruning = True
    elif pruning == 'n':
        pruning = False
    else:
        print("[ValueError] Not valid type. Must be \"y\" or \"n\"")
        raise SystemExit

    strategy = input("Select the strategy to apply (bfs, dfs, dls, ids, ucs, gs, a*): ")

    if (strategy != 'bfs') and (strategy != 'dfs') and (strategy != 'dls') and (strategy != 'ids')\
            and (strategy != 'ucs') and (strategy != 'gs') and (strategy != 'a*'):
        print("[ValueError] Not valid strategy. Must be \"bfs\", \"dfs\", \"dls\", \"ids\", \"ucs\", \"gs\" or \"a*\"")
        raise SystemExit

    heuristic = int(input("Select the heuristic to use (0, 1): "))

    if (heuristic != 0) and (heuristic != 1):
        print("[ValueError] Not valid heuristic")
        raise SystemExit

    jsonPath = input("Enter the path to the .json file: ")

    start = timeit.default_timer()
    searching = S.Search(jsonPath, strategy, max_depth, inc_depth, pruning, heuristic)
    timespent = timeit.default_timer() - start
    print("Execution time: " + str(timespent))

    if not searching.solution:
        print("\nNo solution found")
    else:
        file = open("solution.txt", "w+")
        gpxFile = open("solution.gpx", "w+")
        gpx = gpxpy.gpx.GPX()

        gpx_track = gpxpy.gpx.GPXTrack()
        gpx.tracks.append(gpx_track)

        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)

        for node in searching.solution[0]:
            if node.parent is None:
                file.write("Initial Node: " + node.state.currentPosition + "\nI have to visit "
                           + str(node.state.nodesRemaining) + "\n")
            else:
                file.write("\n" + node.action + "\nI have to visit " + str(node.state.nodesRemaining) + "\n")

            gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(
                searching.problem.StateSpace.graph.positionNode(node.state.currentPosition)[1],
                searching.problem.StateSpace.graph.positionNode(node.state.currentPosition)[0],
                elevation=0, time=datetime.datetime.now(), name=node.state.currentPosition))

        file.write("\nTotal nodes generated: " + str(searching.solution[1]) + "\n")
        file.write("The cost of the path is " + str(searching.solution[0][-1].pathcost) + "\n")
        file.write("The solution was found at depth " + str(searching.solution[0][-1].d) + "\n")
        file.write("The solution was found in " + str(timespent) + " seconds")

        file.close()

        gpxFile.write(gpx.to_xml())

        print("\nSolution found!! You can see it at " + os.path.abspath("../solution.txt"))
