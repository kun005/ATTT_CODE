# def random(min, max, seed):
#     a = 1664525
#     c = 1013904223
#     m = 2**32
    
#     seed = (a * seed + c) % m
#     rand = seed % (max - min + 1) + min
#     return rand

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

def miller_rabin(n, r, a, j_max):
    s, r = Tach(n - 1)  # Sử dụng hàm Tach để tách n - 1 thành 2^s * r
    y = modular_ex(a, r, n)
    if j_max > s - 1:
        return "Too many steps"
    if y == 1 or y == n - 1:
        return y
    for j in range(1, s):
        y = modular_ex(y, 2, n)
        if y == 1:
            return y
        if j == j_max:
            return y
        if y == n - 1:
            return y
    return None

def main():
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    a = int(input("Enter a: "))
    j_max = int(input("Enter j_max: "))

    result = miller_rabin(n, r, a, j_max)
    print(result)
if __name__ == "__main__":
    main()