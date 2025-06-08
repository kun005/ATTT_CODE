


def last_occur(y):
    table = {} #khởi tạo tập rỗng lưu vị trí cuối cùng của từng ký tự
    for i in range(len(y)):
        char = y[i] #luu ky tu tai chi so i
        table[char] = i
    return table

def Boier_moore(X, Y):
    n = len(X)
    m = len(Y)

    if m == 0:
        return []
    if m > n:
        return [-1]
    
    bc_table = last_occur(Y) #cho biết vị trí cuối cùng mỗi ký tự xuất hiện trong Y

    res = []
    s = 0 #tạo vị trí bắt đầu so khớp trong X
    while s <= n - m:
        j = m - 1 
        while j >= 0 and Y[j] == X[s + j]:
            j -= 1
        
        if j < 0: #toàn bộ p khớp tại vt s
            res += [s + 1]
            if s + m < n: 
                next_char = X[s + m] #ký tự trong chuỗi text đứng ngay sau đoạn vừa khớp hoàn toàn tại vị trí s
                if next_char in bc_table:
                    val = bc_table[next_char]
                else: 
                    val = -1
                kc = m - val
                s += max(1, kc)
            else:
                s += 1
        #có ký tự không khớp
        else: 
            bad_char = X[s + j]
            if bad_char in bc_table:
                val = bc_table[bad_char]
            else:
                val = -1
            Kc1 = j - val
            s += max(1, Kc1)
            #sử dụng max đảm bảo luôn dịch ít nhất 1 bước
    if not res:
        return -1
    return res[-1] #vị trí xuất hiện cuối cùng của X trong Y

x = input("Nhập xâu ký tự X: ")
y = input("Nhập xâu ký tự Y: ")

ket_qua = Boier_moore(x, y)
print((ket_qua))