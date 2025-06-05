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

def fermat(n, t, a_list):
    for i in range(t):
        a = a_list[i]
        r = modular_ex(a, n - 1, n)
        if r != 1:
            return i + 1 # trả về vị trí phát hiện hợp số
    return -1  

def main():
    n = int(input("Nhập số nguyên dương n: "))
    t = int(input("Nhập số lần lặp t: "))
    print(f"Nhập {t} giá trị của a:")
    a_list = [int(input(f"a[{i}]: ")) for i in range(t)]

    res = fermat(n, t, a_list)
    print(res)

main()

            