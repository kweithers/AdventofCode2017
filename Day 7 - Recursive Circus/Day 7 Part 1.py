f = open("day7.txt","r")
programs = f.read().translate(None,'->()1234567890,').splitlines()
the_dict = {}
for i in programs:
    the_values = []
    for j in range(len(i.split())):
        if j == 0:
            the_key = i.split()[j]
        else:
            the_values.append(i.split()[j])
    the_dict[the_key] = the_values 
x = list(the_dict.keys())[0]
while True:
    got_updated = False
    for i in list(the_dict.keys()):
        if x in list(the_dict[i]):
            x = i
            got_updated = True
            break
    if got_updated == False:
        break
    print 'updated base to: {}'.format(x)
print 'The base is {}'.format(x)    