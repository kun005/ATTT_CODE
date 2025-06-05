

def modular_ex(a, b, m):
    if m == 1:
        return 0
    res = 1
    a = a % m # rút gọn cơ số trước nếu lớn hơn m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m 
        a = (a * a) % m #bình phương cơ số
        b //= 2 #dịch bit sang phải
    return res

def nto(n):
    if n < 2:
         return 0
    for i in range (2, int(n**0.5) + 1):
         if n % i == 0:
             return 0
         return 1

def ucln(a,b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)

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


