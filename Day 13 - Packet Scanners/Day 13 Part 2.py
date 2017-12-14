f = open("day13.txt","r")
data = f.read().splitlines()
levels = {}
for i in data:
    levels[int(i.split(': ')[0])] = int(i.split(': ')[1])

#def find_place(the_range,the_depth):
#    going_down = True
#    place = 1
#    for i in range(the_range):
#        if going_down == True:
#            place +=1
#            if place == the_depth:
#                going_down = False
#        else:
#            place -=1
#            if place == 1:
#                going_down = True
#    return place
#
Done = False
waiting_time = 0
while not Done:
    Done = True
    for i in levels.keys():
#        if find_place(i+waiting_time,levels[i]) == 1:
         if (i+waiting_time) % (2*levels[i] - 2) == 0:
            waiting_time +=1
            Done = False
            break
print waiting_time
