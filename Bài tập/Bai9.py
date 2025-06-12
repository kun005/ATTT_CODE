


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
    if b == 0:
        return 1
    half = modular_ex(a, b // 2, m)
    res = (half * half) % m
    if b % 2 == 1:
        res = (res * a) % m
    return res
def nto(n):
    if n < 2:
         return 0
    for i in range (2, int(n**0.5) + 1):
         if n % i == 0:
             return 0
         return 1
    
if __name__ == "__main__":
    p = int(input("Nhap so nguyen to p: "))
    g = int(input("Nhap phan tu nguyen thuy g: "))
    x = int(input("Nhap khoa rieng x: "))
    a, b = map(int, input("Nhap ban ma cua m, (a,b): ").split())
    if not nto(p) or x < 1 or x > p - 2:
        print("Du lieu khong hop le")
        exit()
    
    s = modular_ex(a, x, p)
    s1 = Invert_Fp(s, p)
    print("Nghich dao cua (a^x) mod p la :", s1)
    m = (b * s1) % p
    print("Gia tri cua m la:", m)
    
        