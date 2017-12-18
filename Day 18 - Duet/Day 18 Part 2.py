f = open("day18.txt","r")
instructions = [i.split(" ") for i in f.read().splitlines()]
#get all registers
register_names = []
for i in instructions:
    register_names.append(i[1])
register_names = set(register_names)
#remove 1
register_names.remove('1')

last_sound = 4
#create registers dictionary
registers0 = {}
registers1 = {}
for i in register_names:
    registers0[i] = 0
    registers1[i] = 0
registers1['p'] = 1

j=0
k=0
zero_waiting = False
one_waiting = False
zero_queue = []
one_queue = []
one_sends_value = 0
while not (zero_waiting and one_waiting):
    #program 0
    #print j
    i = instructions[j]
    if i[0] == 'snd':
        try:
            one_queue.append(registers0[i[1]])
            j+=1
        except KeyError:
            one_queue.append(int(i[1]))
            j+=1
    elif i[0] == 'set':
        try:
            registers0[i[1]] = registers0[i[2]]
            j+=1
        except KeyError:
            registers0[i[1]] = int(i[2])
            j+=1
    elif i[0] == 'add':
        try:
            registers0[i[1]] += registers0[i[2]]
            j+=1
        except KeyError: 
            registers0[i[1]] += int(i[2])
            j+=1
    elif i[0] == 'mul':
        try:
            registers0[i[1]] *= registers0[i[2]]
            j+=1
        except KeyError: 
            registers0[i[1]] *= int(i[2])
            j+=1
    elif i[0] == 'mod':
        try:
            registers0[i[1]] %= registers0[i[2]]
            j+=1
        except KeyError: 
            registers0[i[1]] %= int(i[2])
            j+=1
    elif i[0] == 'rcv':
        if len(zero_queue) > 0:
            registers0[i[1]] = zero_queue.pop(0)
            j+=1
            zero_waiting = False
        else:
            zero_waiting = True
    elif i[0] == 'jgz':
        try:
            if int(i[1]) <= 0:
                j+=1
                pass
            else:
                try:
                    j += registers0[i[2]]
                except KeyError:
                    j += int(i[2])
        except ValueError:
            if registers0[i[1]] <= 0:
                j+=1
                pass
            else:
                try:
                    j += registers0[i[2]]
                except KeyError:
                    j += int(i[2])
                    
                    
    ###################################################
    #program 1
    #print j
    i = instructions[k]
    if i[0] == 'snd':
        try:
            zero_queue.append(registers1[i[1]])
            k+=1
            one_sends_value +=1
        except KeyError:
            zero_queue.append(int(i[1]))
            k+=1
            one_sends_value +=1
    elif i[0] == 'set':
        try:
            registers1[i[1]] = registers1[i[2]]
            k+=1
        except KeyError:
            registers1[i[1]] = int(i[2])
            k+=1
    elif i[0] == 'add':
        try:
            registers1[i[1]] += registers1[i[2]]
            k+=1
        except KeyError: 
            registers1[i[1]] += int(i[2])
            k+=1
    elif i[0] == 'mul':
        try:
            registers1[i[1]] *= registers1[i[2]]
            k+=1
        except KeyError: 
            registers1[i[1]] *= int(i[2])
            k+=1
    elif i[0] == 'mod':
        try:
            registers1[i[1]] %= registers1[i[2]]
            k+=1
        except KeyError: 
            registers1[i[1]] %= int(i[2])
            k+=1
    elif i[0] == 'rcv':
        if len(one_queue) > 0:
            registers1[i[1]] = one_queue.pop(0)
            k+=1
            one_waiting = False
        else:
            one_waiting = True
    elif i[0] == 'jgz':
        try:
            if int(i[1]) <= 0:
                k+=1
                pass
            else:
                try:
                    k += registers1[i[2]]
                except KeyError:
                    k += int(i[2])
        except ValueError:
            if registers1[i[1]] <= 0:
                k+=1
                pass
            else:
                try:
                    k += registers1[i[2]]
                except KeyError:
                    k += int(i[2])
print one_sends_value