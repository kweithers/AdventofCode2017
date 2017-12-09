f = open("day9.txt","r")
data = f.read()

def ignore_character(x,i):
    if x[i-1] == '!' and ignore_character(x,i-1) is False:
        return True
    else:
        return False
    
def define_garbage(x):
    counters = []
    garbage_flag = False
    for i in range(len(x)):
        if garbage_flag is False:
            if x[i] != '<':
                counters.append(False)
                continue
            else:
                garbage_flag = True
                counters.append(True)
        else: 
            if x[i] == '>' and ignore_character(x,i) is False:
                counters.append(True)
                garbage_flag = False
            else:
                counters.append(True)
                
    return(counters)

data_counters = define_garbage(data)
clean_data = [data[x] for x in range(len(data)) if data_counters[x] is False]

scores = []
num_open = 0
num_closed = 0
for i in clean_data:
    if i == '{':
        num_open +=1
    if i == '}':
        scores.append(num_open - num_closed)
        num_closed +=1 

print sum(scores)