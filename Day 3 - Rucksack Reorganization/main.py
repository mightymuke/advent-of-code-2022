from rucksackreorganization import RucksackReorganization

rucksacks = []

f = open("input.txt", "r")
rucksacks = f.readlines()
f.close()

rr = RucksackReorganization()
rr.load(rucksacks)

results = rr.calculatePrioritySum(rr.findDuplicates())
print("Duplicate item priority score: " + str(results))

results = rr.calculatePrioritySum(rr.findGroupBadges())
print("Group Badge priority score: " + str(results))
