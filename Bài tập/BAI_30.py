def css(s):
    f = {} 
    for c_val in s:
        if c_val in f:
            f[c_val] = f[c_val] + 1
        else:
            f[c_val] = 1
            
    t = 0
    for k_char in f:
        k_freq = f[k_char]
        t = t + (k_freq * (k_freq + 1)) // 2
        
    return t
s = input("Nhập chuỗi s: ")
print("kết quả:", css(s))
