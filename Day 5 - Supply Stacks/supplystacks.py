from abc import ABC, abstractmethod
from cratemover import CrateMover

class SupplyStacks:
    def __init__(self, crateMover):
        self.stacks = {}
        self.rearrangementProcedure = []
        self.crateMover = crateMover

    def load(self, rearrangementProcedure):
        self.stacks = {}
        self.rearrangementProcedure = []

        loadingStacks = True
        stackConfig = []
        procedureConfig = []
        for line in rearrangementProcedure:
            step = line.strip("\n")
            if step == "":
                loadingStacks = False
            elif loadingStacks:
                stackConfig.append(step)
            else:
                procedureConfig.append(step)

        self.stacks = self.parseInitialStacks(stackConfig)
        self.rearrangementProcedure = self.parseRearrangementProcedure(procedureConfig)

    def parseInitialStacks(self, configStacks):
        stacks = {}

        # Final line in config is stack indexes - " 1   2   3 "
        # We'll assume single digits for now
        configStackIndexes = configStacks[-1:][0]
        for configIndex in range(len(configStackIndexes)):
            if configStackIndexes[configIndex] != " ":
                # Found a stack - build it (in reverse) from the config
                stackIndex = int(configStackIndexes[configIndex])
                stacks[stackIndex] = []
                for stack in reversed(configStacks[:-1]):
                    if stack[configIndex] != " ":
                        stacks[stackIndex].append(stack[configIndex])

        return stacks

    def parseRearrangementProcedure(self, configProcedures):
        stackMoves = []

        # assuming each line in format "move x from y to z"
        for stackMove in configProcedures:
            items = stackMove.split(" ")

            stackMoves.append({
                "move": int(items[1]),
                "from": int(items[3]),
                "to": int(items[5])
            })

        return stackMoves

    def rearrangeStacks(self):
        return self.crateMover.moveCrates(self.stacks, self.rearrangementProcedure)

    def topOfStacks(self, stacks):
        tops = []
        for stackIndex in stacks:
            tops.append(stacks[stackIndex][-1:][0])
        return "".join(tops)
