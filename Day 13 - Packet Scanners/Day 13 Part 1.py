f = open("day13.txt","r")
data = f.read().splitlines()
levels = {}
for i in data:
    levels[int(i.split(': ')[0])] = int(i.split(': ')[1])

def find_place(the_range,the_depth):
    going_down = True
    place = 1
    for i in range(the_range):
        if going_down == True:
            place +=1
            if place == the_depth:
                going_down = False
        else:
            place -=1
            if place == 1:
                going_down = True
    return place

counter = 0
for i in levels.keys():
    if find_place(i,levels[i]) == 1:
        counter += i*levels[i]
        
print counter