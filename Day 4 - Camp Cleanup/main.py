from campcleanup import CampCleanup

f = open("input.txt", "r")
assignments = f.readlines()
f.close()

cc = CampCleanup()
cc.load(assignments)

results = cc.findFullyOverlappedAssignments()
print("Number of full overlaps: " + str(len(results)))

results = cc.findAnyOverlappedAssignments()
print("Number of full and partial overlaps: " + str(len(results)))
