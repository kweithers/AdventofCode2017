import itertools as it
f = open("day22.txt","r")
grid = f.read().splitlines()
#sparse matrix by dictionary of keys
infected = {}
for a,b in it.product(range(len(grid)),range(len(grid))):
    if grid[a][b] == '#':
        infected[(a,b)] = 1
weakened = {}
flagged = {}
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
def turn_around(x):
    if x == 'n':
        x = 's'
    elif x == 'w':
        x = 'e'
    elif x == 's':
        x = 'n'
    elif x == 'e':
        x = 'w'
    return x
#initial values
i = 12
j = 12
direction = 'n'
num_infected = 0
for x in xrange(10000000):
    #if infected, turn right
    if (i,j) in infected.keys():
        direction = turn_right(direction)
    #if weakened, continue 
    elif (i,j) in weakened.keys():
        pass
    #if flagged, reverse
    elif (i,j) in flagged.keys():
        direction = turn_around(direction)
    #if clean, turn left
    else:
        direction = turn_left(direction)
    
    #if weakened, become infected
    if (i,j) in weakened.keys():
        infected[(i,j)] = 1
        num_infected +=1
        del weakened[(i,j)]
    #if infected, become flagged
    elif (i,j) in infected.keys():
        flagged[(i,j)] = 1
        del infected[(i,j)]
    #if flagged, become clean
    elif (i,j) in flagged.keys():
        del flagged[(i,j)]        
    #if clean, become weakened
    else:
        weakened[(i,j)] = 1
    
    #move one
    if direction == 'n':
        i-=1
    elif direction == 's':
        i+=1
    elif direction == 'w':
        j-=1
    elif direction == 'e':
        j+=1
print num_infected     