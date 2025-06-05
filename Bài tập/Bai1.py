
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

#ucln
def UCLN(a, b):
    if b == 0:
        return a
    else:
        return UCLN(b, a % b)
def nto(n):
    if n < 2:
         return 0
    for i in range (2, int(n**0.5) + 1):
         if n % i == 0:
             return 0
         return 1

#Nhap 
p = int(input("Nhap so nguyen to p: "))
q = int(input("Nhap so nguyen to q: "))
e = int(input("Nhap so mu cong khai e: "))
if not nto(p) or not nto(q):
    print("Du lieu khong hop le")
n = p * q
phi = (p - 1) * (q - 1)
if e <= 1 or e >= phi or UCLN(e, phi) != 1:
    print("Lỗi: Không thỏa mã điều kiện")
    exit()
d = Invert_Fp(e, phi)

print("Số nguyên n là:", n)
print("Số mũ bí mật d là:", d)


#ví dụ : p=61, q=53, e=17
#n= 61*53= 3233
#phi= (61-1)*(53-1)=3120
#tìm d sao cho d * e mod phi = 1
#(d * 17) mod 3120 = 1