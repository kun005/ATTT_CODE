

#ME: Modular Exponentiation (tính lũy thừa theo modulo)
# dựa vào định lý Fermat, nếu p là số nguyên tố và a là số nguyên không chia hết cho p thì a^(p-1) ≡ 1 (mod p)
# và giải thuật chia để trị 

#from ast import While

#Bình phương có lặp (a^b mod m)
def ME(a, b, m): #a là cơ số, b là số mũ, m là số chia
    if b == 0:
        return 1
    half = ME(a, b // 2, m) #  gọi đệ quy Tính a^(b//2) mod m
    res = (half * half) % m # # Nếu b là số chẵn, thì a^b = (a^(b//2))^2
    if b % 2 == 1:
        res = (res * a) % m # Nếu b là số lẻ, thì a^b = a * (a^(b//2))^2
    return res

# Bước 1: Nhập các tham số
p, g = map(int, input("Nhap gia tri p va g: ").strip().split())
a, b = map(int, input("Nhap gia tri a va b: ").strip().split())


# Tính toán các giá trị công khai
A = ME(g, a, p)
B = ME(g, b, p)

# Bước 3: Tính khóa chung
K_alice = ME(A, b, p) 
K_bob = ME(B, a, p)
if K_alice == K_bob:
        print("Khóa chung K là:", K_bob)
else: 
        print("Khong co khoa chung! ")

#có thể dùng vòng lặp để tính toán
#def modular_ex(a, b, m):
    #if m == 1:
       # return 0
    #res = 1
    #a = a % m
    #while b > 0:
        #if b % 2 == 1:
            #res = (res * a) % m
        #a = (a * a) % m
        #b = b // 2 chia cho 2
    #return res     
    