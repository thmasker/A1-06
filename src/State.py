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
        self.mergesortNodes(self.nodesRemaining, 0, len(self.nodesRemaining) - 1)
        self.md5checksum = hashlib.md5((str(self.currentPosition) + ",".join(str(self.nodesRemaining))).encode())

    """
    Method name:    mergesortNodes
    Description of the Method:  sorts the list passed as input following ascendent numerical order
    Calling arguments:  - nodesList: list of node ids to order
                        - leftIndex: nodesList starting position of the sublist to order
                        - rightIndex: nodesList last position of the sublist to order
    """
    def mergesortNodes(self, nodesList, leftIndex, rightIndex):
        if leftIndex < rightIndex:
            middleIndex = (leftIndex + rightIndex) // 2
            self.mergesortNodes(nodesList, leftIndex, middleIndex)
            self.mergesortNodes(nodesList, middleIndex+1, rightIndex)
            self.mergeNodes(nodesList, leftIndex, middleIndex, rightIndex)

    """
    Method name:    mergeNodes
    Description of the Method:  sorts the list passed as input following ascendent numerical order
    Calling arguments:  - nodesList: list of node ids to order
                        - leftIndex: nodesList starting position of the sublist to order
                        - middleIndex: nodesList middle position of the sublist to order
                        - rightIndex: nodesList last position of the sublist to order
    """
    def mergeNodes(self, nodesList, leftIndex, middleIndex, rightIndex):
        k = leftIndex
        tempLeft, tempRight = [0] * (middleIndex - leftIndex + 1), [0] * (rightIndex - middleIndex)

        for i in range(0, middleIndex - leftIndex + 1):
            tempLeft[i] = nodesList[leftIndex + i]

        for j in range(0, rightIndex - middleIndex):
            tempRight[j] = nodesList[middleIndex + 1 + j]

        i, j = 0, 0

        while (i < len(tempLeft)) and (j < len(tempRight)):
            if tempLeft[i] <= tempRight[j]:
                nodesList[k] = tempLeft[i]
                i += 1
            else:
                nodesList[k] = tempRight[j]
                j += 1

            k += 1

        while i < len(tempLeft):
            nodesList[k] = tempLeft[i]
            i += 1
            k += 1

        while j < len(tempRight):
            nodesList[k] = tempRight[j]
            j += 1
            k += 1
