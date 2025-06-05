
#hàm euclid mở rộng
def extended_euclid(a,b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_euclid(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
# Hàm tìm nghịch đảo modular
def mod_inverse(a, p):
    gcd, x, y = extended_euclid(a, p)
    if gcd != 1:
        raise ValueError("NOT FOUND")
    return x % p

p = int(input("Nhap so nguyen to p: "))
a = int(input("Nhap so nguyen a: "))


res = mod_inverse(a, p)
print("Nghich dao cua a la:", res)


# def Invert_Fp(a,p):
#     u = a 
#     v = p
#     x1,x2 = 1, 0
#     while u != 1:
#         q = int(v/u)
#         r = v - q*u
#         x = x2 - q*x1
#         v = u
#         u = r
#         x2 = x1
#         x1 = x
#     if x1 < 0:
#         return x1 + p
#     return x1 % p
