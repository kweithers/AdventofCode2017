import pandas as pd
import math

def make_dim(n):
    x = int(math.ceil(math.sqrt(n)))
    if x % 2 == 0:
        x= x+1
    else:
        x = x
    return(range(int(x)))

def make_grid(n):
    the_dim = make_dim(n)
    df_grid = pd.DataFrame(index = the_dim,columns = the_dim)
    return(df_grid)
    
def assign_values(the_grid):
    max_val = max(the_grid.index)
    #calculate the number of values to fill in each cycle      
    lengths = []
    len_counter = max_val + 1
    while len_counter >= 1:
        if len_counter == 1:
            lengths.append([1,0,0,0])
            break
        lengths.append([len_counter,len_counter-1,len_counter-1,len_counter-2])
        len_counter = len_counter - 2
    counter = (max(the_grid.index)+1)**2
    i,j = (max_val,max_val)
    for x in lengths:
        #go left
        for a in range(x[0]):
            the_grid.iloc[i,j] = counter
            counter = counter - 1
            j = j - 1
            if a == max(range(x[0])):
                i = i - 1
                j = j + 1
        #go up
        for b in range(x[1]):
            the_grid.iloc[i,j] = counter        
            counter = counter - 1
            i = i - 1
            if b == max(range(x[1])):
                j = j + 1
                i = i + 1
        #go right
        for c in range(x[2]):
            the_grid.iloc[i,j] = counter        
            counter = counter - 1
            j = j + 1
            if c == max(range(x[2])):
                i = i + 1
                j = j - 1
        #go down
        for d in range(x[3]):
            the_grid.iloc[i,j] = counter        
            counter = counter - 1
            i = i + 1
            if d == max(range(x[3])):
                j = j - 1
                i = i - 1
    return(the_grid)
    print(the_grid)

def find_value(the_grid,n):
    for row in range(the_grid.shape[0]): 
         for col in range(the_grid.shape[1]):
             if the_grid.iloc[row,col] == n:
                 return [row,col]
                 break
             
def calculate_distance(the_grid,n):
    my_guy = find_value(the_grid,n)
    origin = find_value(the_grid,1)
    steps = abs(my_guy[0]-origin[0]) + abs((my_guy[1]-origin[1]))
    print(steps)

n = 289326
#n = 12
my_grid = make_grid(n)
my_grid = assign_values(my_grid)
calculate_distance(my_grid,n)