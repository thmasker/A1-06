import src.Search as S

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

    strategy = input("Select the strategy to apply (bfs, dfs, dls, ids, ucs): ")

    if (strategy != 'bfs') or (strategy != 'dfs') or (strategy != 'dls') or (strategy != 'ids') or (strategy != 'ucs'):
        print("[ValueError] Not valid strategy. Must be \"bfs\", \"dfs\", \"dls\", \"ids\" or \"ucs\"")
        raise SystemExit

    jsonPath = input("Enter the path to the .json file: ")

    searching = S.Search(jsonPath, strategy, max_depth, inc_depth, pruning)

    if not searching.solution:
        print("No solution found")
    else:
        file = open("solution.txt", "w+")

        for node in searching.solution:
            file.write(node.action + "\n")

        file.write("The cost of the path is " + searching.solution[-1].cost + "\n")
        file.write("The solution was found at depth " + searching.solution[-1].d + "\n")

        file.close()

        print("Solution found!! You can see it at \"solution.txt\"")
