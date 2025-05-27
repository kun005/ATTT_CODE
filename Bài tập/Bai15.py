import sys 
sys.path.insert(0, './TT/Chuong2')
import TT4_C2
import random

def tong(a, b, t):
    cout = 0
    for i in range(a, b + 1):
        if TT4_C2.fermat(i, t) == "So nguyen to":
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
# 