f = open("day4.txt","r")
passwords = f.read().splitlines()
counter = 0
for i in passwords:
    if len(set(i.split())) == len(i.split()):
        counter = counter + 1
print(counter)