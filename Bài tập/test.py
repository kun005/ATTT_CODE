import sys
sys.path.insert(0, './TT/Chuong1')
import TT8_C1

def ecc_key(p, a, x1, y1, n):
    def add_point(x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            mau = 2 * y1 % p
            if mau == 0:
                raise ValueError("Lỗi: 2 * y1 is zero modulo p.")
            return (3 * x1**2 + a) * TT8_C1.Invert_Fp(mau, p) % p
        else:
            mau = (x2 - x1) % p
            if mau == 0:
                raise ValueError("Lỗi: x2 - x1 is zero modulo p.")
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