f = open("day12.txt","r")
data = f.read().splitlines()
new_data = {}
for i in data:
    holder = []
    holder.append(i.split(" <-> "))
    new_data[int(holder[0][0])] = holder[0][1]
#def find_partners(x):
#    partners = []
#    for i in new_data[0].split(', '):
#        partners.append(int(i))
#        partners.append(find_partners(int(i)))

#Python not great at recursion...    
    
#Brute force until it converges
partners = []
for k in range(20):
    for j in range(len(data)):
        if j == 0 or j in partners:
            for i in new_data[j].split(', '):
                partners.append(int(i))          
    print len(set(partners))