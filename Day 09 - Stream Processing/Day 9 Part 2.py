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
garbage_data = [data[x] for x in range(len(data)) if data_counters[x] is True]

garbage_counter = 0
for i in range(len(garbage_data)):
    if ignore_character(garbage_data,i) is True:
        continue
    elif garbage_data[i] in ['!']:
        continue
    else:
        garbage_counter +=1 
true_close_counter = 0
for i in range(len(garbage_data)):
    if garbage_data[i] == '>' and ignore_character(garbage_data,i) is False:
        true_close_counter +=1
true_opens_closes = true_close_counter*2
print garbage_counter - true_opens_closes