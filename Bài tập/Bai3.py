import sys
sys.path.insert(0, '.\TT\Chuong2')
import TT3_C2

p, q = map(int, input("Nhap p va q: ").strip().split())
m = int(input("Nhap m: "))
if (p % 4 == 3) and (q % 4 == 3):
    n = p * q
    
c =  TT3_C2.modular_ex(m, 2, n)
print("Gia tri c la:", c)
    