

import math 
import sys
sys.path.insert(0, '.\TT\Chuong2')
sys.path.insert(1, '.\TT\Chuong1')
import TT8_C1
import TT3_C2

def nto(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
        return 1


p =int(input("Nhap so nguyen to p: "))
A = int(input("Nhap ptu nguyen thuy A: "))
a = int(input("Nhap so nguyen a: "))
k = int(input("Nhap so ngau nhien k: "))
x =int(input("Nhap thong diep x: "))
if not nto(p):
    exit()
    
y = TT3_C2.modular_ex(A, k, p) # Tính y = A^k mod p
t = TT8_C1.Invert_Fp(k,(p - 1)) # Tính t = k^(-1) mod (p - 1)
g = (x - a * y) * t % (p - 1) # Tính g = (x - a * y) * t mod (p - 1)
if g < 0:
    g += (p - 1) 

print("Gia tri cua chu ky so sig(x) la:", (y, g))