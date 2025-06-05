
import sys
sys.path.insert(0, './TT/Chuong1')
import TT8_C1
# def Key(P, Q, a, b, p):
#     if P == (0, 0):
#         return Q
#     if Q == (0, 0):
#         return P
#     x1, y1 = P
#     x2, y2 = Q
#     if x1 == x2 and (y1 + y2) % p == 0:
#         return (0, 0)
#     if x1 == x2 and y1 == y2:
#         if y1 == 0:
#             return (0, 0)
#         tu = (3 * x1 * x1 + a) % p
#         mau = (2 * y1) % p
#     else:
#         if (x2 - x1) % p == 0:
#             return (0, 0)
#         tu = (y2 - y1) % p
#         mau = (x2 - x1) % p
#     Inv_mau = TT8_C1.Invert_Fp(mau, p)
#     y = (tu * Inv_mau) % p
#     x3 = (y * y - x1 - x2) % p
#     y3 = (y * (x1 - x3) - y1) % p
#     return (x3, y3)

# def mul_point(P, n, a, b, p):
#     # Double-and-add
#     R = (0, 0)  # Điểm vô cực
#     Q = P # Q sẽ nhân đôi sau mỗi vòng lặp 
#     while n > 0:
#         if n & 1:
#             R = Key(R, Q, a, b, p)  # R = R + Q, nếu bit cuối là 1
#         Q = Key(Q, Q, a, b, p)      #Q = 2Q
#         n //= 2
#     return R

# if __name__ == "__main__":
#     p = int(input("Nhập p: "))
#     a = int(input("Nhập a: "))
#     b = int(input("Nhâp b: "))
#     G = tuple(map(int, input("Nhập tọa độ điểm G: ").split()))
#     nA = int(input("Nhập khóa riêng nA: "))
#     if nA == 0:
#         print("0 0")
#     else:
#         PA = mul_point(G, nA, a, b, p)
#         print(PA)


# cần khoảng log2(n) bước, thay vì n bước cộng điểm 

 # C2 dùng vòng lặp để cộng dồn điểm 
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

 
 
def ecc_key(p, a, x1, y1, n):
    def add_point(x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            mau = 2 * y1 % p
            if mau == 0:
                raise ValueError("Lỗi")
            return (3 * x1**2 + a) * Invert_Fp(mau, p) % p
        else:
            mau = (x2 - x1) % p
            if mau == 0:
                raise ValueError("Lỗi")
            return (y2 - y1) * TT8_C1.Invert_Fp(mau, p) % p
    # khởi tạo điểm đầu tiên 
    x2, y2 = x1, y1
    for _ in range(n - 1):
        y = add_point(x1, y1, x2, y2)
        x3 = (y**2 - x1 - x2) % p
        y3 = (y * (x1 - x3) - y1) % p
        x2, y2 = x3, y3

    return x2, y2

if __name__ == "__main__":
    p = int(input("Enter p: "))
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    n = int(input("Enter n: "))

    try:
        result = ecc_key(p, a, x, y, n)
        print("Result:", result)
    except ValueError as e:
        print("Error:", e)
