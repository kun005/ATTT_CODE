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


p, q = map(int, input("Nhap p va q: ").strip().split())
m = int(input("Nhap m: "))
if (p % 4 == 3) and (q % 4 == 3):
    n = p * q
    
c = modular_ex(m, 2, n)
print("Gia tri c la:", c)
    