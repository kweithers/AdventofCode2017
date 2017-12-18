f = open("day16.txt","r")
moves = f.read().split(',')

programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

for x in moves:
    if x[0] == 's':
        num_movers = int(x[1:])
        new_front = programs[-num_movers:]
        new_back = programs[0:(len(programs) - num_movers)]
        programs = new_front + new_back
        
    if x[0] == 'x':
        places = x[1:].split('/')
        
        a = programs[int(places[0])]
        b = programs[int(places[1])]
        
        programs[int(places[0])] = b
        programs[int(places[1])] = a
        
    if x[0] == 'p':
        grams = x[1:].split('/')
        
        a = programs.index(grams[0])
        b = programs.index(grams[1])
        
        programs[a] = grams[1]
        programs[b] = grams[0]

print ''.join(programs)