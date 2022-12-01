f = open("input.txt", "r")

elves = []
currCalories = 0

for line in f:
    if(line == "\n"):
        elves.append(currCalories)
        currCalories = 0
    else:
        currCalories += int(line)

print(max(elves))