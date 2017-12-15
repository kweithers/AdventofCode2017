counter = 0
a = (116*16807) % 2147483647
b = (299*48271) % 2147483647
for i in range(40000000):
    bin_a = bin(a)[2:][-16:].zfill(16)
    bin_b = bin(b)[2:][-16:].zfill(16)
    if bin_a == bin_b:
        counter +=1 
    a = (a*16807) % 2147483647
    b = (b*48271) % 2147483647
print counter