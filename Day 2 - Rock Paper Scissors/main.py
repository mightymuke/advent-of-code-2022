from rockpaperscissors import RockPaperScissors

playbook = []

f = open("input.txt", "r")
playbook = f.readlines()
f.close()

rps = RockPaperScissors()
rps.load(playbook)

results = rps.playStrategyOne()
print("Player 1 score (strategy one): " + str(results[0]))
print("Player 2 score (strategy one): " + str(results[1]))

results = rps.playStrategyTwo()
print("Player 1 score (strategy two): " + str(results[0]))
print("Player 2 score (strategy two): " + str(results[1]))
