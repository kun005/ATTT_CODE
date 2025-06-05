#tính nghịch đảo modulo
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd , x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
def Invert_Fp(a, b):
    gcd, x, y = extended_gcd(a, b)
    if gcd != 1:
        raise ValueError("Nghịch đảo không tồn tại")
    return x % b


#Viết theo trong slide
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
