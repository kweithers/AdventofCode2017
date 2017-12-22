import itertools as it
f = open("day22.txt","r")
grid = f.read().splitlines()
#sparse matrix by dictionary of keys
dok = {}
for a,b in it.product(range(len(grid)),range(len(grid))):
    if grid[a][b] == '#':
        dok[(a,b)] = 1
#movement functions
def turn_right(x):
    if x == 'n':
        x = 'e'
    elif x == 'e':
        x = 's'
    elif x == 's':
        x = 'w'
    elif x == 'w':
        x = 'n'
    return x
def turn_left(x):
    if x == 'n':
        x = 'w'
    elif x == 'w':
        x = 's'
    elif x == 's':
        x = 'e'
    elif x == 'e':
        x = 'n'
    return x
#initial values
i = 12
j = 12
direction = 'n'
infected = 0
for x in xrange(10000):
    #if infected, turn right; else, turn left
    if (i,j) in dok.keys():
        direction = turn_right(direction)
    else:
        direction = turn_left(direction)
    #if infected, clean it; else, infect it
    if (i,j) in dok.keys():
        del dok[(i,j)]
    else:
        dok[(i,j)] = 1
        infected +=1
    #move one
    if direction == 'n':
        i-=1
    elif direction == 's':
        i+=1
    elif direction == 'w':
        j-=1
    elif direction == 'e':
        j+=1
print infected     