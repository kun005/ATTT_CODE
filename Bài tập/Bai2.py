#sử dụng hàm modular exponentiation để tính lũy thừa theo modulo tương tự như trong bài 4
import math 

def nto(n):
    if n < 2:
        return 0
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
        return 1

def ucln(a,b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)
 #Bình phương có lặp (a^b mod m)      
def modular_ex(a, b, m):
    if b == 0:
        return 1
    half = modular_ex(a, b // 2, m)
    res = (half * half) % m
    if b % 2 ==1:
        res  = (res * a) % m
    return res 

p = int(input("Nhap so nguyen to p: "))
q = int(input("Nhap so nguyen to q: "))
e = int(input("Nhap so mu cong khai e: "))
m = int(input("Nhap thong diep m: "))
if not nto(p) or not nto(q):
    print("Du lieu khong hop le")
    exit()
n = p * q
phi = (p-1) * (q-1)
if e <= 1 or e >= phi or ucln(e, phi) != 1:
    print("Lỗi: Không thỏa mã điều kiện")
    exit()
    
c = modular_ex(m, e, n)
print("Ket qua ma hoa c la:", c)


