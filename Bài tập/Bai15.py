
def rand_(min, max, seed):
    a = 1664525 #hệ số nhân
    c = 1013904223 #hằng số cộng
    m = 2**32 

    seed = (a * seed + c) % m
    rand = seed % (max - min + 1) + min
    return rand


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

def fermat(n,t):
    for i in range(t):
        seed = 123456
        a = rand_(2, n - 2, seed)
        r = modular_ex(a, n - 1, n)
        if r != 1:
           return "Hop so"
    return "So nguyen to"

def tong(a, b, t):
    cout = 0
    for i in range(a, b + 1):
        if fermat(i, t) == "So nguyen to":
            cout += i
    return cout

if __name__ == "__main__":
    n = int(input("Nhập số nguyên dương n: "))
    t = int(input("Nhập số lần lặp t: "))
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    
    if 2 <= a < b <= 10**4:
        print("Tong cac so nguyen to trong doan la:", tong(a, b, t))
    else:
        print(0)

# trong bài ko yêu cầu nhập n, nên chọn n >=5, t chọn ngẫu nhiên từ 1 đến 10 