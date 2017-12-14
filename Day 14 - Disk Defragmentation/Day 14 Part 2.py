the_input = "ffayrhll"

inputs = []
for i in range(128):
    inputs.append([str(the_input),str(i)])

real_inputs = []
for i in inputs:
	real_inputs.append('-'.join(i))
    
ascii_inputs = []
for i in real_inputs:    
    ascii_inputs.append([ord(a) for a in i])
    
rows = []
for i in range(128):
    lengths = list(ascii_inputs[i])
    for i in [17, 31, 73, 47, 23]:
        lengths.append(i)
    skip_size = 0
    current_position = 0
    the_list = range(0,256)
    for k in range(64):
        for x in lengths:
            indices = range(current_position,current_position+x)
            new_indices = [a for a in (i % len(the_list) for i in indices)]
            reversed_string = []
            for i in new_indices:
                reversed_string.insert(0,the_list[i])
            for i in range(len(indices)):
                the_list[new_indices[i]] = reversed_string[i]
            current_position = (current_position + x + skip_size) % len(the_list)
            skip_size +=1
    
    import operator as op
    block_num = 0
    counter = 16
    dense = []
    
    for k in range(16):
        dense.append(reduce(op.xor, the_list[block_num:counter]))
        block_num +=16
        counter +=16

    hexes = ''.join([hex(v)[2:].zfill(2) for v in dense])
    print len(hexes)
    scale = 16 ## hexadecimal
    num_of_bits = 4
    temp = []
    for i in hexes:
        temp.append(bin(int(i, scale))[2:].zfill(num_of_bits))
    print len(temp)
    rows.append(''.join(temp))
    
the_grid = []    
for i in range(128):
    the_grid.append(list(rows[i]))
    
def find_neighbors(i,j,a_grid):
    #list of all neighboring tuples
    points = []
    #check all four adjacent squares
    if a_grid[i][j] == '1':
        for a,b in zip([0,0,1,-1],[1,-1,0,0]):
            #check if they are inside the grid
            if i+a in range(128) and j+b in range(128):
                if a_grid[i+a][b+j] == '1':
                    points.append((i+a,j+b))
        return points
    
neighbor_dict = {}
for x in range(128):
    for y in range(128):
        neighbor_dict[(x,y)] = find_neighbors(x,y,the_grid)
        
def find_group(a_dict,a_tuple):
    current_group = [a_tuple]
    unchanged = False
    while not unchanged:
        unchanged = True
        previous = len(list(current_group))
        for i in a_dict.keys():
                #if one of the keys points to a tuple already in the group,
                #include it in the group
                try:
                    for j in a_dict[i]:
                        if j in current_group:
                            current_group.append(i)     
                            current_group = list(set(current_group))
                #if the dictionary values is empty, pass
                except TypeError:
                    pass
        #get the new length of the group
        new = len(list(current_group))
        #if the group has not grown, we have the full group
        if previous != new:
            unchanged = False
    return current_group  
    
#find_group(neighbor_dict,(1,1))

import itertools
def find_num_groups(a_grid):
    groups = 0
    for i,j in itertools.product(range(128),range(128)):
        if a_grid[i][j] == '0':
            continue
        else:
            groups +=1
            new_group = find_group(neighbor_dict,(i,j))
            #'remove' all members of the new group from the grid
            for x in new_group:
                a_grid[x[0]][x[1]]= '0'
    print groups
    
find_num_groups(the_grid)         