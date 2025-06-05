
def last_occur(p):
    table = {} #khởi tạo tập rỗng lưu vị trí cuối cùng của từng ký tự
    for i in range(len(p)):
        char = p[i] #luu ky tu tai chi so i
        table[char] = i
    return table

def Boier_moore(txt, pat):
    n = len(txt)
    m = len(pat)

    if m == 0:
        return []
    if m > n:
        return [-1]
    
    bc_table = last_occur(pat) #cho biết vị trí cuối cùng mỗi ký tự xuất hiện trong pattern
    res = []
    s = 0 #tạo vị trí bắt đầu so khớp trong text 
    while s <= n - m:
        j = m - 1 
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        
        if j < 0: #toàn bộ p khớp tại vt s
            res += [s + 1]
            if s + m < n: 
                next_char = txt[s + m] #ký tự trong chuỗi text đứng ngay sau đoạn pattern vừa khớp hoàn toàn tại vị trí s
                if next_char in bc_table:
                    val = bc_table[next_char]
                else:
                    val = - 1
                kc = m - val
                s += max(1, kc)
            else:
                s += 1
        #có ký tự không khớp
        else: 
            bad_char = txt[s + j]
            if bad_char in bc_table:
                val = bc_table[bad_char]
            else:
                val = - 1
            kc1 = j - val
            s += max(1, kc1)
    if not res:
        return [-1]
    return res

t = input("Nhập chuỗi văn bản txt: ")
p = input("Nhập chuỗi mẫu: ")

ket_qua = Boier_moore(t, p)
print(*(ket_qua))