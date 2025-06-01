import sys
sys.path.insert(0, './TT/Chuong2')
from TT3_C2 import modular_ex

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