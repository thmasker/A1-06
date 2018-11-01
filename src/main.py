import src.Search as S

max_depth = 0
inc_depth = 0
pruning = False

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

    isPruning = input('Do you want to use pruning? (y/n) ')

    if isPruning == 'y':
        pruning = True
    elif isPruning == 'n':
        pruning = False
    else:
        print("[ValueError] Not valid type. Must be \"y\" or \"n\"")
        raise SystemExit

    jsonPath = input("Enter the path to the .json file: ")

    S.Search(jsonPath, max_depth, inc_depth, pruning)
