import random
import sys
sys.path.insert(0, './TT/Chuong2')
import TT3_C2
from random import randint

def fermat(n,t):
    for i in range(t):
       a = random.randint(2, n - 2)
       r = TT3_C2.modular_ex(a, n - 1, n)
       if r != 1:
           return "Hop so"
    return "So nguyen to"

# if __name__ == "__main__":
#     n = int(input("Nhap so nguyen duong n: "))
#     t = int(input("Nhap so lan lap t: "))
#     res = fermat(n, t)
#     print(res)
    
    