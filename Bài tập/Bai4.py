
def modular_ex(a, b, m):
    if m == 1:
       return 0
    res = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b = b // 2 #chia cho 2
    return res     
    
p, g = map(int, input("Nhap gia tri p va g: ").strip().split())
a, b = map(int, input("Nhap gia tri a va b: ").strip().split())

# Tính toán các giá trị công khai
A = modular_ex(g, a, p)
B = modular_ex(g, b, p)

# Bước 3: Tính khóa chung
K_alice = modular_ex(A, b, p) 
K_bob = modular_ex(B, a, p)
if K_alice == K_bob:
        print("Khóa chung K là:", K_bob)
else: 
        print("Khong co khoa chung! ")



#Bình phương có lặp (a^b mod m)
# def ME(a, b, m): #a là cơ số, b là số mũ, m là số chia
#     if b == 0:
#         return 1
#     half = ME(a, b // 2, m) #  gọi đệ quy Tính a^(b//2) mod m
#     res = (half * half) % m 
#     if b % 2 == 1:
#         res = (res * a) % m
#     return res