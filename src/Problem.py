import json
import State
import StateSpace

class Problem:

    def __init__(self, jsonPath):
        with open(jsonPath, "r") as rstate:
            rdata = json.load(rstate)
        
        self.StateSpace = StateSpace(rdata["graphmlfile"])
        self.InitState = State(rdata["IntSt"]["node"], rdata["IntSt"]["listNodes"])

    def isGoal(self, state):
        if not state.nodesRemaining:
            return True
        return False



Problem("input.json")
