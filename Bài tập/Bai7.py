import math
def nto(n):
    if n < 2:
         return 0
    for i in range (2, int(math.sqrt(n)) + 1):
         if n % i == 0:
             return 0
         return 1

#Bình phương có lặp (a^b mod m)
def modular(a, b, m):
    if b == 0:
        return 1
    half = modular(a, b // 2, m)
    res = (half * half) % m
    if b % 2 == 1:
        res = (res *a ) % m
    return res 
    
p = int(input("Nhap so nguyen to p: "))
g = int(input("Nhap phan tu nguyen thuy g: "))
x = int(input("Nhap khoa rieng x: "))

if not nto(p) or x < 1 or x > p -2:
    print("Du lieu khong hop le")
    exit()

y = modular(g, x, p)
print("Khoa cong khai y la:", y)


  