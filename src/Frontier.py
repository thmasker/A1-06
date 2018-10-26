from blist import blist
import psutil

"""
Class Name: Frontier
Description:  Implementation of a tree frontier list
"""
class Frontier:
    """
    Method name:    __init__
    Description:  Constructor. It creates an empty frontier
    """
    def __init__(self):
        self.frontier = blist([])

    """
    Method name:    insert
    Description:    adds a new TreeNode to the frontier
    Calling arguments:  treeNode: TreeNode to insert in the frontier
    Checked Exceptions: MemoryError: if used memory is more than a 75 %, program must stop
                            its execution
    """
    def insert(self, treeNode):
        if psutil.swap_memory()[3] >= 80:
            print("Not enough space in memory")
            raise MemoryError
        else:
            self.frontier.insert(treeNode.f, treeNode)

    """
    Method name:    remove
    Description:    takes the first element in the frontier and removes from it
    Return value:   Element removed from the frontier
    """
    def remove(self):
        try:
            return self.frontier.pop(0)
        except IndexError as index_error:
            print(index_error)
            raise SystemExit

    """
    Method name:    isEmpty
    Description:    checks if the frontier is empty or not
    Return value:   True if frontier is empty; False otherwise
    """
    def isEmpty(self):
        if not self.frontier:
            return True
        else:
            return False
