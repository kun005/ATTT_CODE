
#DÙng đệ quy
#Bình phương có lặp (a^b mod m)
# def ME(a, b, m): 
#     if b == 0:
#         return 1
#     half = ME(a, b // 2, m) #  gọi đệ quy Tính a^(b//2) mod m
#     res = (half * half) % m # # Nếu b là số chẵn, thì a^b = (a^(b//2))^2
#     if b % 2 == 1:
#         res = (res * a) % m # Nếu b là số lẻ, thì a^b = a * (a^(b//2))^2
#     return res


#dùng vòng lặp

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
