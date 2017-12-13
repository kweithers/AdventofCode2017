f = open("day12.txt","r")
data = f.read().splitlines()
new_data = {}
for i in data:
    holder = []
    holder.append(i.split(" <-> "))
    new_data[int(holder[0][0])] = holder[0][1]

groups = 0
#Brute force until it converges
while bool(new_data) is True:
    partners = []
    for k in range(50):
        for j in new_data.keys():
            if j == new_data.keys()[0] or j in partners:
                for i in new_data[j].split(', '):
                    partners.append(int(i))
        #print len(set(partners))
    for a in set(partners):
        new_data.pop(a)
    groups +=1
    print groups

print groups        