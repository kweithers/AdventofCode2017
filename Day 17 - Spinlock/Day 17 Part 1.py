steps = 354
lock = [0]
current_position = 0
for i in range(1,2018):
    current_position +=steps
    current_position %=len(lock)
    current_position +=1
    lock.insert(current_position,i)  
print lock[lock.index(2017)+1]