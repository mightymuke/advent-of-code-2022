class CampCleanup:
    def __init__(self):
        self.assignmentPairs = []

    def load(self, assignmentPairs):
        self.assignmentPairs = []
        for assignmentPair in assignmentPairs:
            self.assignmentPairs.append(self.parse(assignmentPair))

    def parse(self, assignmentPair):
        assignments = []
        sectionGroups = assignmentPair.split(",")
        if len(sectionGroups) == 2: # Only need to handle pairs for now
            for sectionGroup in sectionGroups:
                assignments.append(self.explode(sectionGroup))
        return assignments

    def explode(self, sections):
        explodedSections = []
        bounds = sections.split("-")
        for section in range(int(bounds[0]), int(bounds[1]) + 1):
            explodedSections.append(str(section))
        return explodedSections

    def findFullyOverlappedAssignments(self):
        overlaps = []
        for assignment in self.assignmentPairs:
            elf1Assignment = "," + ",".join(assignment[0]) + ","
            elf2Assignment = "," + ",".join(assignment[1]) + ","
            if elf1Assignment.find(elf2Assignment) >= 0 or elf2Assignment.find(elf1Assignment) >= 0:
                overlaps.append(assignment)
        return overlaps

    def findAnyOverlappedAssignments(self):
        overlaps = []
        for assignment in self.assignmentPairs:
            for section in assignment[0]:
                if section in assignment[1]:
                    overlaps.append(assignment)
                    break
        return overlaps
