


def extended_gcd(a, b):
    if b == 0: return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
def mod_inverse(a, p):
    gcd, x, y = extended_gcd(a,p)
    if gcd != 1:
        raise ValueError("nghich dao khong ton tai")
    else:
        return x % p
    
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
    print("Gia tri cua s la:", s)
    s1= mod_inverse(s, p)
    print("Nghich dao cua (a^x) mod p la :", s1)
    m = (b * s1) % p
    print("Gia tri cua m la:", m)
    
        