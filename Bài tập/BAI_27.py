


def last_occur(y):
    y_upper = y.upper()
    table = {} #khởi tạo tập rỗng lưu vị trí cuối cùng của từng ký tự
    for i, char in enumerate(y_upper):
        table[char] = i
    return table

def Boier_moore(X, Y):
    n = len(X)
    m = len(Y)

    if m == 0:
        return []
    if m > n:
        return [-1]

    X_upper = X.upper()
    Y_upper = Y.upper()
    
    bc_table = last_occur(Y) #cho biết vị trí cuối cùng mỗi ký tự xuất hiện trong Y

    res = []
    s = 0 #tạo vị trí bắt đầu so khớp trong X
    while s <= n - m:
        j = m - 1 
        while j >= 0 and Y_upper[j] == X_upper[s + j]:
            j -= 1
        
        if j < 0: #toàn bộ p khớp tại vt s
            res.append(s + 1)
            if s + m < n: 
                next_char = X_upper[s + m] #ký tự trong chuỗi text đứng ngay sau đoạn vừa khớp hoàn toàn tại vị trí s
                Kc = m - bc_table.get(next_char, -1)
                s += max(1, Kc)
            else:
                s += 1
        #có ký tự không khớp
        else: 
            bad_char = X_upper[s + j]
            Kc1 = j - bc_table.get(bad_char, -1)
            s += max(1, Kc1)
            #sử dụng max đảm bảo luôn dịch ít nhất 1 bước
    if not res:
        return -1
    return res[-1] #vị trí xuất hiện cuối cùng của X trong Y

x = input("Nhập xâu ký tự X: ")
y = input("Nhập xâu ký tự Y: ")

ket_qua = Boier_moore(x, y)
print((ket_qua))