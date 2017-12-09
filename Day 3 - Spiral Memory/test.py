my_list = []
for a in [1,2,3]:
    for b in [1,2,3]:
        if a == 2 and b == 2:
            continue
        my_list.append([a,b])
        
print(my_list)