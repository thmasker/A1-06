import hashlib

"""
Class Name: State
Description:  Defines a certain possible state of the problem
"""
class State:
    """
    Method name:    __init__
    Description:  Constructor
    Calling arguments:  - currentPosition: a specific node id
                        - nodesLeft: list of nodes left to go. Ordered by ascending order depending on its nodeid
    """
    def __init__(self, currentPosition, nodesRemaining):
        self.currentPosition = currentPosition
        self.nodesRemaining = nodesRemaining
        self.nodesRemaining.sort()
        self.md5checksum = hashlib.md5((str(self.currentPosition) + ",".join(str(self.nodesRemaining))).encode())

