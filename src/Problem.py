import json
import src.State as S
import src.StateSpace as SP

"""
Class Name: Problem
Description:    Class defining the problem to solve
"""
class Problem:
    """
    Method name:    __init__
    Description:    Constructor
    Calling arguments:  jsonPath: path to the json file to read
    Checked Exceptions: FileNotFoundError: checks if the .json file exists or not
    """
    def __init__(self, jsonPath):
        try:
            with open(jsonPath, "r") as rstate:
                rdata = json.load(rstate)
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            raise SystemExit
        except json.decoder.JSONDecodeError:
            print(jsonPath + " is not a .json file")
            raise SystemExit

        self.StateSpace = SP.StateSpace(rdata["graphmlfile"])
        self.InitState = S.State(rdata["IntSt"]["node"], rdata["IntSt"]["listNodes"])

    """
    Method name:    isGoal
    Description:    checks if the problem is already solved
    Calling arguments:  state: current state
    Return value:   True if problem is solved; False otherwise
    """
    def isGoal(self, state):
        if len(state.nodesRemaining) == 1:
            if state.nodesRemaining[0] == self.InitState.currentPosition:
                return True

        if not state.nodesRemaining:
            return True
        else:
            return False
