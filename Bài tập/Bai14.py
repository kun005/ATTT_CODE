
def Invert_Fp(a,p):
    u = a 
    v = p
    x1,x2 = 1, 0
    while u != 1:
        q = int(v/u)
        r = v - q*u
        x = x2 - q*x1
        v = u
        u = r
        x2 = x1
        x1 = x
    if x1 < 0:
        return x1 + p
    return x1 % p

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


p =int(input("Nhap so nguyen to p: "))
A = int(input("Nhap ptu nguyen thuy A: "))
a = int(input("Nhap so nguyen a: "))
k = int(input("Nhap so ngau nhien k: "))
x =int(input("Nhap thong diep x: "))
if not nto(p):
    exit()
    
y = modular_ex(A, k, p) # Tính y = A^k mod p
t = Invert_Fp(k,(p - 1)) # Tính t = k^(-1) mod (p - 1)
g = (x - a * y) * t % (p - 1) # Tính g = (x - a * y) * t mod (p - 1)
if g < 0:
    g += (p - 1) 

print("Gia tri cua chu ky so sig(x) la:", (y, g))