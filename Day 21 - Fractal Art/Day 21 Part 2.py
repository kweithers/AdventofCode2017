import numpy as np
f = open("day21.txt","r")
rules = f.read().splitlines()
keys = []
values = []
for i in rules:
    the_key = np.array(i.split(' => ')[0].split('/'))
    the_val = np.array(i.split(' => ')[1].split('/'))
    final_key = []
    for i in range(len(the_key)):
        final_key.append(list(the_key[i]))
    final_val = []
    for i in range(len(the_val)):
        final_val.append(list(the_val[i]))
    keys.append(np.array(final_key))
    values.append(np.array(final_val))
grid = np.array([['.','#','.'],['.','.','#'],['#','#','#']])

def find_match(start):
    global keys
    #try all rotations
    for i in range(4):
        for j in range(len(keys)):
            if np.array_equal(start,keys[j]):
                return values[j]
        start = np.rot90(start)
    #flip x, then try all rotations
    start = np.flip(start,0)
    for i in range(4):
        for j in range(len(keys)):
            if np.array_equal(start,keys[j]):
                return values[j]
        start = np.rot90(start)
    start = np.flip(start,0)
    #flip y, then try all rotations
    start = np.flip(start,1)
    for i in range(4):
        for j in range(len(keys)):
            if np.array_equal(start,keys[j]):
                return values[j]
        start = np.rot90(start)
    start = np.flip(start,1)
    #flip on both axes, then try all rotations
    start = np.flip(start,0)
    start = np.flip(start,1)
    for i in range(4):
        for j in range(len(keys)):
            if np.array_equal(start,keys[j]):
                return values[j]
        start = np.rot90(start)

#split up a grid into its pieces, find their match, then combine into new grid
def make_new_grid(old_grid):
    the_size = len(old_grid)
    pieces = []
    if the_size % 2 == 0:
        for i in range(the_size/2):
            for j in range(the_size/2):
                holder = []
                for a in range(2):
                    for b in range(2):
                        holder.append(old_grid[2*i+a][2*j+b])
                pieces.append(np.reshape(holder,(2,2)))
    elif the_size % 3 == 0:
        for i in range(the_size/3):
            for j in range(the_size/3):
                holder = []
                for a in range(3):
                    for b in range(3):
                        holder.append(old_grid[3*i+a][3*j+b])
                pieces.append(np.reshape(holder,(3,3)))  
    new_pieces = []            
    for k in pieces:
        new_pieces.append(find_match(k))
    #combine into new grid..
    new_size = int(len(pieces)**.5)
    rows = []
    counter = 0
    for x in range(new_size):
        holder = []
        for y in range(new_size):
            holder.append(new_pieces[counter])
            counter +=1
        holder = np.hstack(holder)
        rows.append(holder)
    rows = np.vstack(rows)
    return rows
#18 iterations  
for i in range(18):
    grid = make_new_grid(grid)
#count ons
on = 0
for i in grid:
    for j in i:
        if j == '#':
            on +=1
print on