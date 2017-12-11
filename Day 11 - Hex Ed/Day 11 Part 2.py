f = open("day11.txt","r")
data = f.read().split(',')
cardinals = ['ns','ew']
cardinal_counts= [0,0]
new_max = 0
for x in data:
    if x in ['n','ne','nw']:
        cardinal_counts[0] +=1
    if x in ['s','se','sw']:
        cardinal_counts[0] -=1
    if x in ['ne','se']:
        cardinal_counts[1] +=1
    if x in ['nw','sw']:
        cardinal_counts[1] -=1
    new_max = max(new_max,max(cardinal_counts[0],cardinal_counts[1]))
print new_max