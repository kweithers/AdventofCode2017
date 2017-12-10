lengths = [70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41]
the_lengths = str(lengths).translate(None,'[] ')
ascii_lengths =  [ord(a) for a in the_lengths]

for i in [17, 31, 73, 47, 23]:
    ascii_lengths.append(i)

lengths = list(ascii_lengths)
skip_size = 0
current_position = 0
the_list = range(0,256)
for k in range(64):
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
#print the_list

import operator as op
block_num = 0
counter = 16
dense = []

for k in range(16):
    dense.append(reduce(op.xor, the_list[block_num:counter]))
    block_num +=16
    counter +=16
    
print dense
print [hex(v)[2:] for v in dense]
print ''.join([hex(v)[2:] for v in dense])