import sys 
sys.path.insert(0, './TT/Chuong2')
from TT5_C2 import miller_rabin

def main():
    try:
        a = int(input("Nhap gia tri a: "))
        b = int(input("Nhap gia tri b: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên.")
        return

    if not (2 <= a <= 10**4):
        print("Lỗi: a phải thỏa mãn điều kiện 2 <= a <= 10^4.")
        return

    if b < a:
        print("Lỗi: b phải lớn hơn hoặc bằng a.")
        return

    tong = 0
    for so in range(a, b + 1):
        if miller_rabin(so):
            tong += so

    print("Tổng các số nguyên tố trong đoạn [a, b]:", tong)

if __name__ == "__main__":
    main()
