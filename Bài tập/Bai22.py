


def last_occur(p):
    p_upper = p.upper()
    table = {} #khởi tạo tập rỗng lưu vị trí cuối cùng của từng ký tự
    for i, char in enumerate(p_upper):
        table[char] = i
    return table

def Boier_moore(txt, pat):
    n = len(txt)
    m = len(pat)

    if m == 0:
        return []
    if m > n:
        return [-1]

    txt_upper = txt.upper()
    pat_upper = pat.upper()
    
    bc_table = last_occur(pat) #cho biết vị trí cuối cùng mỗi ký tự xuất hiện trong pattern

    res = []
    s = 0 #tạo vị trí bắt đầu so khớp trong text 
    while s <= n - m:
        j = m - 1 
        while j >= 0 and pat_upper[j] == txt_upper[s + j]:
            j -= 1
        
        if j <= 0: #toàn bộ p khớp tại vt s
            res.append(s + 1)
            if s + m < n: 
                next_char = txt_upper[s + m] #ký tự trong chuỗi text đứng ngay sau đoạn pattern vừa khớp hoàn toàn tại vị trí s
                Kc = m - bc_table.get(next_char, -1)
                s += max(1, Kc)
            else:
                s += 1
        #có ký tự không khớp
        else: 
            bad_char = txt_upper[s + j]
            Kc1 = j - bc_table.get(bad_char, -1)
            s += max(1, Kc1)
            #sử dụng max đảm bảo luôn dịch ít nhất 1 bước
    if not res:
        return [-1]
    return res

t = input("Nhập chuỗi văn bản txt: ")
p = input("Nhập chuỗi mẫu: ")

ket_qua = Boier_moore(t, p)
print(*(ket_qua))