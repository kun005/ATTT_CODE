def css(s):
    #1. đếm tần suất ký tự
    f = {} 
    for c_val in s:
        if c_val in f:
            f[c_val] += 1
        else:
            f[c_val] = 1
            
    t = 0
    for char in f:
        k_freq = f[char]
        # công thức tính số chuỗi con với tần suất k lần 
        t = t + (k_freq * (k_freq + 1)) // 2
        
    return t
s = input("Nhập chuỗi s: ")
print("kết quả:", css(s))

#để in tất cả các chuỗi con 
# def in_all(s):
#     print("Cac chuoi con hop le la: ")
#     kq = []
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             if s[i] == s[j]:
#                   nếu giống thì lấy chuỗi con từ i đến j 
#                 chuoi_con = s[i : j + 1]
#                 kq += [chuoi_con]
    
#     print(kq)           

# s = input("Nhap chuoi s:")
# in_all(s)
