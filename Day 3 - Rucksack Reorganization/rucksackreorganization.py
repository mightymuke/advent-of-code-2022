import string

class RucksackItemType:
    def __init__(self, type):
        self.type = type

    def priority(self):
        return string.ascii_letters.find(self.type) + 1

class RucksackReorganization:
    def __init__(self):
        self.rucksacks = []

    def load(self, rucksacks):
        self.rucksacks = []
        for rucksack in rucksacks:
            self.rucksacks.append(rucksack)

    def findDuplicates(self):
        duplicates = []

        for rucksack in self.rucksacks:
            dupes = ""
            midpoint = len(rucksack) // 2
            compartment1 = rucksack[:midpoint]
            compartment2 = rucksack[midpoint:]

            for item in compartment1:
                if (item in compartment2) and (item not in dupes):
                    dupes += item

            duplicates.append(dupes)

        return duplicates

    def findGroupBadges(self):
        groupSize = 3
        groupBadges = []

        if (len(self.rucksacks) < 1):
            return groupBadges

        i = 0
        rucksackGroup = []
        for rucksack in self.rucksacks:
            i += 1
            rucksackGroup.append(rucksack)
            if (i % groupSize == 0):
                groupBadges.extend(self.findCommonItemInAllRucksacks(rucksackGroup))
                rucksackGroup = []

        # Should check if anything is in rucksackGroup and throw an error if there is
        return groupBadges

    def calculatePrioritySum(self, items):
        sum = 0
        for item in items:
            sum += RucksackItemType(item).priority()
        return sum

    def findCommonItemInAllRucksacks(self, rucksacks):
        if (len(rucksacks) < 1):
            return []

        # get unique list of potential candidates
        candidates = []
        for item in rucksacks[0]:
            if item not in candidates:
                candidates.append(item)

        # compare remaining candidates with contents of other rucksacks
        for rucksack in rucksacks[1:]:
            dupes = []
            for item in candidates:
                if item in rucksack:
                    dupes.append(item)
            candidates = dupes

        return candidates
