import sys
sys.path.insert(0, './TT/Chuong2')
import TT3_C2
import random


def fermat(n, t, a_list):
    for i in range(t):
        a = a_list[i]
        r = TT3_C2.modular_ex(a, n - 1, n)
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

            