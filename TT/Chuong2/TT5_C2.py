        
    
from TT3_C2 import modular_ex
def random(min, max, seed):
    a = 1664525
    c = 1013904223
    m = 2**32
    
    seed = (a * seed + c) % m
    rand = seed % (max - min + 1) + min
    return rand

def Tach(n):
    cout = 0
    while n % 2 == 0:
        cout += 1
        n //= 2
    return cout, n

def miller_rabin(n, t=10):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    s, r = Tach(n - 1)
    for _ in range(t):
        seed = 12345
        a = random(2, n - 2, seed)
        y = modular_ex(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= (s - 1) and y != (n - 1):
                y = modular_ex(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True