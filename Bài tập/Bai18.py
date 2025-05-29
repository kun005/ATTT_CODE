
import sys 
sys.path.insert(0, './TT/Chuong2')
from TT5_C2 import miller_rabin


def main():
    N = int(input("Nhap so luong ptu cua mang: "))
    if N < 0:
        print("N phai la so nguyen duong.")
        return
    arr = input("Nhap cac ptu cua mang: ")
    nums = list(map(int, arr.split()))
    
    if len(nums) != N:
        print("So luong ptu khong khop voi N.")
        return 
    if any(x <= 0 for x in nums):
        print("Lỗi: tất cả các ptu trong mảng phải là số nguyên duong. ")
        return 
    ket_qua = [] # tao mang luu kq
    check = set() # tạo 1 tập rỗng để ktra xem ptu đã xuất hiện hay chưa?
    
    for so in nums:
        if so not in check:
            check.add(so)
            if miller_rabin(so):
                ket_qua.append(so)
    print("Kết quả:", *ket_qua)
    
    
if __name__ =="__main__":
    main()
    