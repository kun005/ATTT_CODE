import random
import sys
sys.path.insert(0, './TT/Chuong2')
import TT3_C2


def check_nto(n, t = 5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    for _ in range(t):
        a = random.randint(2, n - 2)
        if TT3_C2.modular_ex(a, n - 1, n) != 1:
            return False
    return True

def main():
    try:
        N = int(input("Nhập số lượng phần tử của mảng: "))
        if N <= 0:
            print("Lỗi: N phải là số nguyên dương.")
            return

        arr = input("Nhập các phần tử của mảng: ")
        nums = list(map(int, arr.split()))
        
        if len(nums) != N:
            print(f"Lỗi: Số lượng phần tử không khớp với N (N={N})")
            return

        if any(x <= 0 for x in nums): #kiểm tra xem có tồn tại ptu tm đk 
            print("Lỗi: Tất cả các phần tử trong mảng phải là số nguyên dương.")
            return

        ket_qua = []
        da_xuat_hien = set() # tạo 1 tập rỗng 

        for so in nums:
            if so not in da_xuat_hien:
                da_xuat_hien.add(so)
                if check_nto(so):
                    ket_qua.append(so)

        print("Kết quả: ", *ket_qua)

    except ValueError:
        print("Lỗi: Giá trị nhập vào phải là số nguyên.")
    except Exception as e:
        print(f"Đã xảy ra lỗi không xác định: {e}")

if __name__ == "__main__":
    main()