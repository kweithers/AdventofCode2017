counter = 0
a = (116*16807) % 2147483647
b = (299*48271) % 2147483647
for i in range(5000000):
    while a % 4 != 0:
        a = (a*16807) % 2147483647 
    while b % 8 != 0:
        b = (b*48271) % 2147483647
    if bin(a)[2:][-16:].zfill(16) == bin(b)[2:][-16:].zfill(16):
        counter +=1 
    a = (a*16807) % 2147483647
    b = (b*48271) % 2147483647
print counter

# Using generators!

#def AG():
#  x = 116
#  while True:
#    x *= 16807
#    x %= 2147483647
#    if x % 4 == 0:
#      yield x
#
#def BG():
#  x = 299
#  while True:
#    x *= 48271
#    x %= 2147483647
#    if x % 8 == 0:
#      yield x
#
#A = AG()
#B = BG()
#matches = 0
#for i in xrange(5000000):
#  a = A.next()
#  b = B.next()
#  if bin(a)[2:][-16:].zfill(16) == bin(b)[2:][-16:].zfill(16):
#    matches += 1
#print matches