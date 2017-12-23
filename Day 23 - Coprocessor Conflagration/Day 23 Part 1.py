f = open("day23.txt","r")
instructions = [i.split(" ") for i in f.read().splitlines()]
#get all registers
register_names = ['a','b','c','d','e','f','g','h']
#create registers dictionary
registers = {}
for i in register_names:
    registers[i] = 0

j=0
c=0
Done = False
while not Done:
    print j
    try:
        i = instructions[j]
        if i[0] == 'set':
            try:
                registers[i[1]] = registers[i[2]]
                j+=1
            except KeyError:
                registers[i[1]] = int(i[2])
                j+=1
        elif i[0] == 'sub':
            try:
                registers[i[1]] -= registers[i[2]]
                j+=1
            except KeyError: 
                registers[i[1]] -= int(i[2])
                j+=1
        elif i[0] == 'mul':
            try:
                registers[i[1]] *= registers[i[2]]
                j+=1
                c+=1
            except KeyError: 
                registers[i[1]] *= int(i[2])
                j+=1
                c+=1
        elif i[0] == 'jnz':
            try:
                if int(i[1]) == 0:
                    j+=1
                    pass
                else:
                    try:
                        j += registers[i[2]]
                    except KeyError:
                        j += int(i[2])
            except ValueError:
                if registers[i[1]] == 0:
                    j+=1
                    pass
                else:
                    try:
                        j += registers[i[2]]
                    except KeyError:
                        j += int(i[2])
    except IndexError:
        print c
        break