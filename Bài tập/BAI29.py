def remove(s, t):
    n = len(s)
    m = len(t)

    if m == 0:
        return s

    list = []
    i = 0

    while i < n:
        #s[start : end] -> toán tử slice : tạo ra một chuỗi con kthu trc chỉ số end
        if i + m <= n and s[i : i + m] == t:
            i += m 
        else:
            list = list + [s[i]]
            i += 1
            
    chuoi_Kq = ""
    for char in list:
        chuoi_Kq += char
    return chuoi_Kq
s = input("Nhập chuỗi s: ")
t = input("Nhập chuỗi mẫu t: ")
res = remove(s, t)
print(res)



