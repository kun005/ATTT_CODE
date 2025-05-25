import math
import sys
sys.path.insert(0, r'.\TT\Chuong1')
import TT8_C1
#ucln
def UCLN(a, b):
    if b == 0:
        return a
    else:
        return UCLN(b, a % b)

#check so nguyento
def nto(n):
    if n < 2: 
        return 0
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            return 0
    return 1

# Ham euclid mở rộng
# def extended_gcd(a, b):
#     if b == 0:
#         return a, 1, 0 # gcd, x, y
#     else:
#         gcd, x1, y1 = extended_gcd(b, a % b) # là kết quả của b*x1 + (a % b)*y1 = gcd
#         #x1 là hệ số của b, y1 là hệ số của a%b ở bước trước
#         x = y1 
#         y = x1 - (a // b) * y1 
#         return gcd, x, y

# #Hàm tìm nghịch đảo modular
# def mod_inverse(e, phi):
#     gcd, x, y = extended_gcd(e, phi) #gọi hàm extended_gcd-> trả về 3 giá trị
#     #gcd:UCLN của e và phi, x và y là các hệ số của pt: e*x + phi*y = gcd
#     if gcd != 1:
#         raise ValueError("Nghịch đảo không tồn tại")
#     return x % phi

#Nhap 
p = int(input("Nhap so nguyen to p: "))
q = int(input("Nhap so nguyen to q: "))
e = int(input("Nhap so mu cong khai e: "))
if not nto(p) or not nto(q):
    print("Du lieu khong hop le")
    exit()
n = p * q
phi = (p - 1) * (q - 1)
if e <= 1 or e >= phi or UCLN(e, phi) != 1:
    print("Lỗi: Không thỏa mã điều kiện")
    exit()
d = TT8_C1.Invert_Fp(e, phi)

print("Số nguyên n là:", n)
print("Số mũ bí mật d là:", d)


#ví dụ : p=61, q=53, e=17
#n= 61*53= 3233
#phi= (61-1)*(53-1)=3120
#tìm d sao cho d * e mod phi = 1
#(d * 17) mod 3120 = 1