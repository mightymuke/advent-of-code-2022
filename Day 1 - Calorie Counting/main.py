from elfcaloriecounter import ElfCalorieCounter

elfdata = []

f = open("elf-calories.txt", "r")
elfdata = f.readlines()
f.close()

cc = ElfCalorieCounter()
cc.load(elfdata)

print("Elf with most is: " + str(cc.topCalories(1)[0]))
print("Top three elves are: " + str(cc.topCalories(3)))
print("Sum of top three elves is: " + str(sum(cc.topCalories(3))))
