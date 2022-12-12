from cratemover import CrateMover9000, CrateMover9001
from supplystacks import SupplyStacks

f = open("input.txt", "r")
rearrangementProcedure = f.readlines()
f.close()

ss = SupplyStacks(CrateMover9000())
ss.load(rearrangementProcedure)
results = ss.topOfStacks(ss.rearrangeStacks())
print("Top of stacks with CrateMover9000: " + results) # FZCMJCRHZ

ss = SupplyStacks(CrateMover9001())
ss.load(rearrangementProcedure)
results = ss.topOfStacks(ss.rearrangeStacks())
print("Top of stacks with CrateMover9001: " + results) # JSDHQMZGF
