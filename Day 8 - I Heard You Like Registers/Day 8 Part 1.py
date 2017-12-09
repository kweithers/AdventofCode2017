f = open("day8.txt","r")
instructions = f.read().splitlines()
nodes = {}
for i in instructions:
    nodes[i.split()[0]] = 0
import operator as op
ops = {}
ops['<'] = op.lt
ops['>'] = op.gt
ops['<='] = op.le
ops['>='] = op.ge
ops['=='] = op.eq
ops['!='] = op.ne
add_sub = {}
add_sub['inc'] = op.add
add_sub['dec'] = op.sub
for x in instructions:
    i = x.split()
    if ops[i[5]](int(nodes[i[4]]),int(i[6])):
        nodes[i[0]] = add_sub[i[1]](int(nodes[i[0]]),int(i[2])) 
max(nodes.values())