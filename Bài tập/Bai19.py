
def random(min, max, seed):
    a = 1664525
    c = 1013904223
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
        b //= 2 #dịch sang phải
    return res

def Tach(n):
    cout = 0
    while n % 2 == 0:
        cout += 1
        n //= 2
    return cout, n

def miller_rabin(n, t=10):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    s, r = Tach(n - 1)
    for _ in range(t):
        seed = 12345
        a = random(2, n - 2, seed)
        y = modular_ex(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= (s - 1) and y != (n - 1):
                y = modular_ex(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True

def main():
    a = int(input("Nhap gia tri a: "))
    b = int(input("Nhap gia tri b: "))

    if not (2 <= a <= 10**4):
        print("Lỗi: a phải thỏa mãn điều kiện 2 <= a <= 10^4.")
        return

    tong = 0
    for so in range(a, b + 1):
        if miller_rabin(so):
            tong += so

    print("Tổng các số nguyên tố trong đoạn [a, b]:", tong)

if __name__ == "__main__":
    main()
