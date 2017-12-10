lengths = [70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41]
skip_size = 0
current_position = 0
the_list = range(0,256)
for x in lengths:
    indices = range(current_position,current_position+x)
    new_indices = [a for a in (i % len(the_list) for i in indices)]
    reversed_string = []
    for i in new_indices:
        reversed_string.insert(0,the_list[i])
    for i in range(len(indices)):
        the_list[new_indices[i]] = reversed_string[i]
    current_position = (current_position + x + skip_size) % len(the_list)
    skip_size +=1
print the_list