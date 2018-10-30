max_depth = 0
inc_depth = 0
pruning = False

"""
Class Name: Search
Description:    Class containing the searching algorithms
"""
class Search:
    """
        Method name:    __init__
        Description:  
    """
    def __init__(self):
        try:
            max_depth = int(input('Write down the maximum depth desired: '))
        except ValueError:
            print("Not valid type. Must be an integer")
            raise SystemExit

        try:
            inc_depth = int(input('Write down the increment of depth desired: '))
        except ValueError:
            print("Not valid type. Must be an integer")
            raise SystemExit

        isPruning = input('Do you want to use pruning? (y/n) ')

        if isPruning == 'y':
            pruning = True
        elif isPruning == 'n':
            pruning = False
        else:
            print("Not valid type. Must be \"y\" or \"n\"")
            raise SystemExit
