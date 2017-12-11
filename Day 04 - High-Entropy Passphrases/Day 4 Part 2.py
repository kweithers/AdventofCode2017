def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l)))

f = open("day4.txt","r")
passwords = f.read().splitlines()
counter = 0
for i in passwords:  
    letters=[]
    for j in i.split():
        letters.append(sorted(j))
        
    set_letters = sort_and_deduplicate(letters)
    
    if len(set_letters) == len(letters):
        counter = counter + 1
print(counter)