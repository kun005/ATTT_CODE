
import sys
sys.path.insert(0, './TT/Chuong2')
import TT3_C2
# LCG (Linear Congruential Generator): X(n + 1) = (a * Xn + c) mod m
def random(min, max, seed):
    a = 1664525
    c = c = 1013904223
    m = 2**32

    seed = (a * seed + c) % m #công thức
    rand = seed % (max - min + 1) + min
    return rand



def check_nto(n, t = 5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    for _ in range(t):
        seed = 123456
        a = random(2, n - 2, seed)
        if TT3_C2.modular_ex(a, n - 1, n) != 1:
            return False
    return True

def main():
    N = int(input("Nhập số lượng phần tử của mảng: "))
    arr = input("Nhập các phần tử của mảng: ")
    nums = list(map(int, arr.split()))
    kq = []
    da_xuat_hien = []

    for so in nums:
        if so not in da_xuat_hien:
            da_xuat_hien += [so]
            if check_nto(so):
                kq = kq + [so]

    print("Kết quả: ", *kq)

if __name__ == "__main__":
    main()