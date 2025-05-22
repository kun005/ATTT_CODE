import math 
def nto(n):
    if n < 2:
        return 0
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
             return 0
        return 1

def modular_ex(a, b, m):
    if b == 0:
        return 1
    half = modular_ex(a, b // 2, m)
    res = (half * half) % m
    if b % 2 == 1:
        res = (res * a) % m
    return res

p = int(input("Nhap so nguyen to p: "))
g = int(input("Nhap phan tu nguyen thuy g: "))
k = int(input("Nhap khoa ngau nhien k: "))
y = int(input("Nhap khoa cong khai y: "))
m = int(input("Nhap thong diep m: "))
if not nto(p) or k < 1 or k > p - 2:
    print("Du lieu khong hop le")
    exit()

#tinh toan
a = modular_ex(g, k, p)
b = (modular_ex(y, k, p) * m ) % p #Khi nhân chúng lại (m*y^k), kết quả có thể vượt ra ngoài phạm vi [0,p−1]. Phép % p đảm bảo rằng giá trị cuối cùng của b sẽ là một số nguyên nằm trong khoảng [0,p−1].

print("Gia tri cua a la:", a)
print("Gia tri cua b la:", b)


