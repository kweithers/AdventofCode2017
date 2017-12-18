from numba import jit
@jit
def find_val():
    pos = 0
    final = 0
    for i in range(1,50000001):
        pos = (pos+354)%i+1
        if pos==1:
            final = i
    return final
print find_val()