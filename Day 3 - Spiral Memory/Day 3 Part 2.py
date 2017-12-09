import pandas as pd
import math
#import numpy as np

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
    
def sum_adj(the_grid,i,j,max_dim,origin):
    if i == origin and j == origin:
        return 1 
    the_sum = []
    for a in [i-1,i,i+1]:
        if a < 0 or a > max_dim:
            continue
        for b in [j-1,j,j+1]:
            if b < 0 or b > max_dim:
                continue
            if a == i and b == j:
                continue
            elif pd.isnull(the_grid.iloc[a,b]):
                continue 
            else:
                the_sum.append(the_grid.iloc[a,b])
    return(sum(the_sum))
        
def assign_values(the_grid,sum_grid):
    max_val = max(the_grid.index)
    #calculate the number of values to fill in each cycle      
    lengths = []
    len_counter = 1
    while len_counter <= max_val:
        lengths.append([len_counter,len_counter,len_counter+1,len_counter+1])
        len_counter = len_counter + 2
    
    #include one extra for the origin
    lengths[0][0] = lengths[0][0] + 1
    #include the final row at the bottom
    lengths.append([len_counter - 1,0,0,0])

    origin = int(max_val/2)
    i,j = (origin,origin)
    counter = 1
    for x in lengths:
        #go right
        for a in range(x[0]):
            sum_grid.iloc[i,j] = sum_adj(sum_grid,i,j,max_val,origin)
            the_grid.iloc[i,j] = counter
            counter = counter + 1
            j = j + 1
            if a == max(range(x[0])):
                i = i - 1
                j = j - 1
        #go up
        for b in range(x[1]):
            sum_grid.iloc[i,j] = sum_adj(sum_grid,i,j,max_val,origin)
            the_grid.iloc[i,j] = counter
            counter = counter + 1
            i = i - 1
            if b == max(range(x[1])):
                j = j - 1
                i = i + 1
        #go left
        for c in range(x[2]):
            sum_grid.iloc[i,j] = sum_adj(sum_grid,i,j,max_val,origin)
            the_grid.iloc[i,j] = counter
            counter = counter + 1
            j = j - 1
            if c == max(range(x[2])):
                i = i + 1
                j = j + 1
        #go down
        for d in range(x[3]):
            sum_grid.iloc[i,j] = sum_adj(sum_grid,i,j,max_val,origin)
            the_grid.iloc[i,j] = counter
            counter = counter + 1
            i = i + 1
            if d == max(range(x[3])):
                j = j + 1
                i = i - 1
        
    return the_grid, sum_grid 

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
    
def find_biggest(sum_grid,n):
    flat_list = [item for sublist in sum_grid.values for item in sublist]
    bigs = [x for x in flat_list if x > n]
    bigs.sort()
    print(bigs[0])
    

n = 289326
#n = 25
my_grid = make_grid(n)
my_sum_grid = make_grid(n)
my_grid , my_sum_grid = assign_values(my_grid,my_sum_grid)
calculate_distance(my_grid,n)
find_biggest(my_sum_grid,n)