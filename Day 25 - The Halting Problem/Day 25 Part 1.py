from collections import defaultdict

state = 'a'
loc = 0
dok = defaultdict(int)

for x in xrange(12208951):
    if state == 'a':
        if dok[loc] == 0:
            dok[loc] = 1
            loc +=1
            state = 'b'
        else:
            dok[loc] = 0
            loc -=1
            state = 'e'
    elif state == 'b':
        if dok[loc] == 0:
            dok[loc] = 1
            loc -=1
            state = 'c'
        else:
            dok[loc] = 0 
            loc +=1
            state = 'a'
    elif state == 'c':
        if dok[loc] == 0:
            dok[loc] = 1
            loc -=1
            state = 'd'
        else:
            dok[loc] = 0
            loc +=1
            state = 'c'
    elif state == 'd':
        if dok[loc] == 0:
            dok[loc] = 1
            loc -=1
            state = 'e'
        else:
            dok[loc] = 0
            loc -=1
            state = 'f'
    elif state == 'e':
        if dok[loc] == 0:
            dok[loc] = 1
            loc -=1
            state = 'a'
        else:
            dok[loc] = 1
            loc -=1
            state = 'c'    
    elif state == 'f':
        if dok[loc] == 0:
            dok[loc] = 1
            loc -=1
            state = 'e'
        else:
            dok[loc] = 1
            loc +=1
            state = 'a'

