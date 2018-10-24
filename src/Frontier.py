import blist
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
        self.queue = blist([])

    """
    Method name:    insert
    Description:    adds a new TreeNode to the frontier
    Calling arguments:  treeNode: TreeNode to insert in the frontier
    Required Files:
    Checked Exceptions:
    """
    def insert(self, treeNode):
        self.queue.append(treeNode)


    """
    Method name:    remove
    Description:    takes the first element in the frontier and removes from it
    Return value:
    """
    def remove(self):
        try:
            low = 0
            for i in range(len(self.queue)):
                if self.queue[i].f < self.queue[low].f:
                    low = i
            item = self.queue.pop(i)
            return item
        except IndexError:
            print()
            exit()

    """
    Method name:    isEmpty
    Description:    checks if the frontier is empty or not
    Return value:   True if frontier is empty; False otherwise
    Checked Exceptions:
    """
    def isEmpty(self):
        return len(self.queue) == blist([])
