f = open("day7.txt","r")
programs = f.read().translate(None,'->(),').splitlines()
the_dict = {}
weight_dict = {}
for i in programs:
    the_values = []
    for j in range(len(i.split())):
        if j == 0:
            the_key = i.split()[j]
        elif j == 1:
            the_weight = i.split()[j]
        else:
            the_values.append(i.split()[j])
    the_dict[the_key] = the_values
    weight_dict[the_key] = int(the_weight)

# get the total weight of a node (including its weight and the weight of all nodes above it)
def get_total_weight(x):
    weight = []
    weight.append(weight_dict[x])
    for i in the_dict[x]:
        weight.append(get_total_weight(i))  
    return sum(weight)

total_weight_dict = {}
for i in list(the_dict.keys()):
    total_weight_dict[i] = get_total_weight(i)
    
for i in list(the_dict.keys()):
    above_weights = []
    above_above_weights = []
    for j in the_dict[i]:
        above_weights.append(total_weight_dict[j])
        holder = []
        for k in the_dict[j]:
            holder.append(total_weight_dict[k])
        above_above_weights.append(all(x==holder[0] for x in holder))   
    if len(set(above_weights)) > 1 and all(above_above_weights):
        print(i)
        break

print above_weights
print the_dict[i]
#'marnqj' <<- this guys weight needs to change
# needs total to be = 1815

#view nodes above
the_dict['marnqj']
#weight of the nodes above: 135
total_weight_dict['upair'] 
# number of nodes above: 4
len(the_dict['marnqj'])

print(1815 - 135*4)
#answer = 1275