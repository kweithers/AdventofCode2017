f = open("day11.txt","r")
data = f.read().split(',')
directions = ['n','ne','se','s','sw','nw']
counts = []
for x in directions:
    counts.append(data.count(x))
#count moves that cancel out: ne/sw, n/s, nw/se
ne_sw = counts[directions.index('ne')] - counts[directions.index('sw')]
n_s = counts[directions.index('n')] - counts[directions.index('s')]
nw_se = counts[directions.index('nw')] - counts[directions.index('se')]
#ne 366
#s 29
#se 284
north = 366
east = 366 + 284
south = 29 + 284
final_ns = north-south
final_ew = east
#steps = 0
#while final_ns > 0 and final_east > 0:
#    #take a step
#    final_ns -= 1
#    final_east -= 1
#    steps += 1
#while final_east > 0:
#    #take a step
#    final_east -=1
#    steps +=1
#print(steps)

#one liner..
print max(final_ns,final_ew)