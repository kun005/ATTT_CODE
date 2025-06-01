# def Chuoi_xau(p):
#     bad_char = [-1]*256
#     for i in range(len(p)):
#         bad_char[ord(p[i])] = i
#     return bad_char

# def boyer_moore(t, p):
#     m = len(p)
#     n = len(t)
#     res = []
    
#     if m == 0: return []
#     if m > n: return []
    
    
#     bad_char = Chuoi_xau(p)
#     s = 0
#     res = []
#     while s <= n - m:
#         j = m - 1
#         while j >= 0 and p[j] == t[s + j]:
#             j -= 1
#         if j < 0:
#             res.append(s)
#             s += (m - bad_char[ord(t[s + m])] 
#                     if s + m < n else 1)
#         else:
#             s += max(1, j - bad_char[ord(t[s + j])])
#     return res

# #main 
# if __name__ == "__main__":
#     t = input("Nhập chuỗi văn bản (t): ")
#     p = input("Nhập chuỗi mẫu (p): ")
#     vitri = boyer_moore(t, p)
#     if vitri:
#         print("Pattern xuất hiện tại vị trí:", vitri)
#     else:
#         print("Mau '{p}' khong duoc tim thay trong van ban. ")


import string
from TT0_C3 import tach_chuoi

def last_occur(ABC,p):
    ABC = ABC.upper()
    p = p.upper()
    lst_ABC = tach_chuoi(ABC)
    lst_p = tach_chuoi(p)
    dic_ABC = {i:-1 for i in ABC}
    for i in lst_ABC:
        for j in range(len(lst_p)-1,-1,-1):
            if lst_p[j]==i:
                dic_ABC[i] = j
                break
    return dic_ABC

def boier_moore(ABC,m,p):
    lst_ABC = last_occur(ABC,p)
    lst_m = tach_chuoi(m.upper())
    lst_p = tach_chuoi(p.upper())
    i = len(lst_p) - 1
    while i < len(lst_m):
        for j in range(len(lst_p)-1,-2,-1):
            if lst_m[i] != lst_p[j]:
                i = i + len(lst_p) - min(j,1+lst_ABC[lst_m[i]])
                break
            else:
                i = i-1
                if j == 0:
                    return i+1
    return "Khong tim ra"

print(boier_moore("abcd","abacaabadcabacabaabb","abad"))

        