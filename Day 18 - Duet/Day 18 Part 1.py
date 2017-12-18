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
registers = {}
for i in register_names:
    registers[i] = 0

j=0
Done = False
while not Done:
    print j
    i = instructions[j]
    if i[0] == 'snd':
        try:
            last_sound = registers[i[1]]
            j+=1
        except KeyError:
            last_sound = int(i[1])
            j+=1
    elif i[0] == 'set':
        try:
            registers[i[1]] = registers[i[2]]
            j+=1
        except KeyError:
            registers[i[1]] = int(i[2])
            j+=1
    elif i[0] == 'add':
        try:
            registers[i[1]] += registers[i[2]]
            j+=1
        except KeyError: 
            registers[i[1]] += int(i[2])
            j+=1
    elif i[0] == 'mul':
        try:
            registers[i[1]] *= registers[i[2]]
            j+=1
        except KeyError: 
            registers[i[1]] *= int(i[2])
            j+=1
    elif i[0] == 'mod':
        try:
            registers[i[1]] %= registers[i[2]]
            j+=1
        except KeyError: 
            registers[i[1]] %= int(i[2])
            j+=1
    elif i[0] == 'rcv':
        if i[1] == 0:
            j+=1
            pass
        else:
            print last_sound
            Done = True
            break
    elif i[0] == 'jgz':
        try:
            if int(i[1]) <= 0:
                j+=1
                pass
            else:
                try:
                    j += registers[i[2]]
                except KeyError:
                    j += int(i[2])
        except ValueError:
            if registers[i[1]] <= 0:
                j+=1
                pass
            else:
                try:
                    j += registers[i[2]]
                except KeyError:
                    j += int(i[2])