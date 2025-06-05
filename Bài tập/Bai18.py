
import sys 
sys.path.insert(0, './TT/Chuong2')
from TT5_C2 import miller_rabin


def main():
    N = int(input("Nhap so luong ptu cua mang: "))

    arr = input("Nhap cac ptu cua mang: ")
    nums = list(map(int, arr.split()))

    ket_qua = [] # tao mang luu kq
    check = [] # tạo 1 tập rỗng để ktra xem ptu đã xuất hiện hay chưa?
    
    for so in nums:
        if so not in check:
            check += [so]
            if miller_rabin(so):
                ket_qua += [so]
    print("Kết quả:", *ket_qua)
    
    
if __name__ =="__main__":
    main()
    