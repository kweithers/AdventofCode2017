f = open("day5.txt","r")
instructions = f.read().splitlines()
instructions = map(int,instructions)
place = 0
steps = 0
while place >= 0 and place < len(instructions):
    new_place = place + instructions[place]
    if instructions[place] >= 3: 
        instructions[place] = instructions[place] - 1
    else:
        instructions[place] = instructions[place] + 1
    place = new_place
    steps = steps + 1
print(steps)