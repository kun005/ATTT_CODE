def hoanvi(s, p):
    m = len(s)
    n = len(p)
    
    if n > m:
        return []
    # khoi tao bang tan suat 
    p_freq = {}
    s_freq = {}
    
    for i in range(n):
        ktP = p[i]
        if ktP in p_freq:
            p_freq[ktP] += 1
        else:
            p_freq[ktP] = 1
    for i in range(n):    
        ktS = s[i]
        if ktS in s_freq:
            s_freq[ktS] += 1
        else:
            s_freq[ktS] = 1
        
    res = []
    #so sanh 
    if p_freq == s_freq:
        res += [0]
        
    for i in range(n, m):
        new = s[i]
        if new in s_freq:
            s_freq[new] += 1
        else:
            s_freq[new] = 1
        
        #loại bỏ ký tự cũ ( bên trái) ra khỏi s_freq
        old = s[i - n]
        s_freq[old] -= 1
        if s_freq[old] == 0:
            del s_freq[old]
        if p_freq == s_freq:
            start = i - n + 1
            res += [start]
    return res

s = input("Nhập chuỗi S: ")
p = input("Nhập chuỗi mẫu P: ")

kq = hoanvi(s, p)
print(*kq)
    