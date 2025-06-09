def solve(s):
    n = len(s)
    #độ dài tối đa của tiền tố và hậu tố
    max_len = n // 2
    res = 0
    for L in range(max_len, 0, -1):
        prefix = s[0 : L]
        suffix = s[n - L : n]
        if prefix == suffix:
            res = L
            break
    return res
s = input("Nhập chuỗi s: ")
kq = solve(s)
print(kq)
        
        