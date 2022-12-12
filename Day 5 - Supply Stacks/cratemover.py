from abc import ABC, abstractmethod

class CrateMover(ABC):

    @abstractmethod
    def moveCrates(self, stacks, procedure):
        pass

class CrateMover9000(CrateMover):
    def __init__(self):
        pass

    def moveCrates(self, stacks, procedure):
        updatedStacks = stacks.copy()

        for crateMove in procedure:
            for _ in range(crateMove["move"]):
                item = updatedStacks[crateMove["from"]].pop()
                updatedStacks[crateMove["to"]].append(item)

        return updatedStacks

class CrateMover9001(CrateMover):
    def __init__(self):
        pass

    def moveCrates(self, stacks, procedure):
        updatedStacks = stacks.copy()

        for crateMove in procedure:
            fromStack = crateMove["from"]
            toStack = crateMove["to"]

            updatedStacks[toStack].extend(updatedStacks[fromStack][crateMove["move"]*-1:])
            updatedStacks[fromStack] = updatedStacks[fromStack][:len(updatedStacks[fromStack])-crateMove["move"]]

        return updatedStacks
