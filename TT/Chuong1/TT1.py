# # cộng trừ bội chính xác 
# def cong_boi(a, b, W, t):
#     c_plus = [0] * t
#     e = 0
#     Max = 2 ** W
#     for i in range(t -1, -1, -1): #duyệt đến giá trị i =0
#         c_plus[i] = (a[i] + b[i] + e)
#         if c_plus[i] >= Max:
#             c_plus[i] -= Max
#             e = 1
#         else:
#             e = 0
#         return [e, c_plus]

# def Tru_boi(a, b, W, t):
#     c_minus = [0] * t
#     e = 0
#     Max = 2 ** W
#     for i in range(t - 1, -1, -1):
#         c_minus[i] = a[i] - b[i] - e
#         if c_minus[i] <  0:
#             c_minus[i] += Max
#             e = 1
#         else:
#             e = 0
#     return [e, c_minus]

def Nhap_so(W, t, ten_so):
    MAX = 2**W
    print(f"Nhập số {ten_so} gồm {t} từ:")
    so = []
    for i in range(t):
        while True:
            try:
                val = int(input("{ten_so}[{i}] = "))
                if 0 <= val < MAX:
                    so.append(val)
                    break
                else:
                    print(f"Giá trị phải trong khoảng [0, {MAX - 1}]")
            except:
                print("Vui lòng nhập số nguyên hợp lệ.")
    return so

def Cong_boi(a, b, W, t):
    c_plus = [0]*t
    e = 0
    MAX = 2**W
    for i in range(t-1, -1, -1):
        c_plus[i] = a[i] + b[i] + e
        if c_plus[i] >= MAX:
            c_plus[i] -= MAX
            e = 1
        else:
            e = 0
    return [e, c_plus]

def Tru_boi(a, b, W, t):
    c_hieu = [0]*t
    e = 0
    MAX = 2**W
    for i in range(t-1, -1, -1):
        c_hieu[i] = a[i] - b[i] - e
        if c_hieu[i] < 0:
            c_hieu[i] += MAX
            e = 1
        else:
            e = 0
    return [e, c_hieu]

if __name__ == "__main__":
    W = int(input("Nhập độ dài từ W: "))
    t = int(input("Nhập số lượng từ t: "))

    a = Nhap_so(W, t, "a")
    b = Nhap_so(W, t, "b")

    e, kq_cong = Cong_boi(a, b, W, t)
    print("Kết quả cộng: {kq_cong}, e = {e_cong}")

    e, kq_tru = Tru_boi(a, b, W, t)
    print("Kết quả trừ: {kq_tru}, e = {e_tru}")
