f = open("day19.txt","r")
maze = f.read().splitlines()

def move_one():
    global i,j,maze,direction
    #check all four directions
    if direction == 's':
        i+=1
    elif direction == 'n':
        i-=1
    elif direction == 'w':
        j-=1
    elif direction == 'e':
        j+=1
            
def new_direction():
    global i,j,maze,Done,direction
    #check all four directions
    if maze[i+1][j] != ' ' and direction != 'n':
        i+=1
        direction = 's'
    elif maze[i-1][j] != ' ' and direction != 's':
        i-=1
        direction = 'n'
    elif maze[i][j-1] != ' ' and direction != 'e':
        j-=1
        direction = 'w'
    elif maze[i][j+1] != ' ' and direction != 'w':
        j+=1
        direction = 'e'

#starting coordinates and direction
i = 0
j = 103
direction = 's'
Done = False
letters = []
steps = 0
while not Done: 
    steps +=1
    #record a letter, if there is one
    if maze[i][j] not in ['-','|','+']:
        letters.append(maze[i][j])
        #stopping letter
        if maze[i][j] == 'Y':
            break
    if maze[i][j] != '+':
        move_one()
    else:
        new_direction()
    #print i,j
    #print maze[i][j]
    
print ''.join(letters)
print steps
