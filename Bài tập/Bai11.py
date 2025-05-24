import math
import sys
sys.path.insert(0, './TT/Chuong2')  # Đảm bảo đường dẫn đúng
import TT3_C2  

def nto(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
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
s = TT3_C2.modular_ex(m, d, n)

# In kết quả
print("Chữ ký số là:", s)
