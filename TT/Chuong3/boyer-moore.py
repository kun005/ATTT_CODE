def Chuoi_xau(p):
    bad_char = [-1]*256
    for i in range(len(p)):
        bad_char[ord(p[i])] = i
    return bad_char

def boyer_moore(t, p):
    m = len(p)
    n = len(t)
    bad_char = Chuoi_xau(p)
    s = 0
    result = []
    while s <= n - m:
        j = m - 1
        while j >= 0 and p[j] == t[s + j]:
            j -= 1
        if j < 0:
            result.append(s)
            s += (m - bad_char[ord(t[s + m])] 
                    if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(t[s + j])])
    return result

#main 
if __name__ == "__main__":
    t = input("Nhập chuỗi văn bản (t): ")
    p = input("Nhập chuỗi mẫu (p): ")
    vitri = boyer_moore(t, p)
    print("Pattern xuất hiện tại các vị trí:", vitri)