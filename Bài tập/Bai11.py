
def modular_ex(a, b, m):
    if m == 1:
        return 0
    res = 1
    a = a % m # rút gọn cơ số trước nếu lớn hơn m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m 
        a = (a * a) % m #bình phương cơ số
        b //= 2 #dịch sang phải
    return res
def nto(n):
    if n < 2:
         return 0
    for i in range (2, int(n**0.5) + 1):
         if n % i == 0:
             return 0
         return 1


# Nhập dữ liệu từ bàn phím
p = int(input("Nhập số nguyên tố p: "))
q = int(input("Nhập số nguyên tố q: "))
m = int(input("Nhập thông điệp cần ký m: "))
d = int(input("Nhập khóa ký d: "))

if not nto(p) or not nto(q):
    print("p hoặc q không phải là số nguyên tố.")
    exit()

# Tính n = p * q
n = p * q

# Tạo chữ ký s = m^d mod n
s = modular_ex(m, d, n)

# In kết quả
print("Chữ ký số là:", s)
