the_input = "ffayrhll"

inputs = []
for i in range(128):
    inputs.append([str(the_input),str(i)])

real_inputs = []
for i in inputs:
	real_inputs.append('-'.join(i))
    
ascii_inputs = []
for i in real_inputs:    
    ascii_inputs.append([ord(a) for a in i])
    
rows = []
for i in range(128):
    lengths = list(ascii_inputs[i])
    for i in [17, 31, 73, 47, 23]:
        lengths.append(i)
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
    
    import operator as op
    block_num = 0
    counter = 16
    dense = []
    
    for k in range(16):
        dense.append(reduce(op.xor, the_list[block_num:counter]))
        block_num +=16
        counter +=16

    hexes = ''.join([hex(v)[2:].zfill(2) for v in dense])
    print len(hexes)
    scale = 16 ## hexadecimal
    num_of_bits = 4
    temp = []
    for i in hexes:
        temp.append(bin(int(i, scale))[2:].zfill(num_of_bits))
    print len(temp)
    rows.append(''.join(temp))
    
counter = 0
for i in rows:
    print len(i)
    for j in i:
        if j == '1':
            counter +=1
print counter