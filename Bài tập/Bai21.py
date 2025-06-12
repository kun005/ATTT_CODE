def Vet_can(T, P):
    n = len(T)  
    m = len(P)  

    for i in range(n - m + 1):  
        match = 1
        for j in range(m):  # kiểm tra từng ký tự của P với T tại vị trí i
            if T[i + j] != P[j]:
                match = 0
                break  # không khớp -> dừng kiểm tra và thử vị trí tiếp theo
        if match:
            return i  # trả về vị trí đầu tiên tìm thấy P trong T
    return -1  

def sovle(A, B):
    n = len(A)
    m = len(B)

    Kq_A = "" #chuỗi kết quả 
    count = 0 # số lần lặp lại A

    while len(Kq_A) < m:
        Kq_A += A
        count += 1

    #check xem B có phải chuỗi con?
    if Vet_can(Kq_A, B) != -1:
        return count
    
    Kq_A += A
    count += 1
    #xử lý TH B bắt đầu ở cuối lần lặp thứ count, và kthúc ở đầu lần lặp thứ count + 1
    if Vet_can(Kq_A, B) != -1:
        return count
    return -1

if __name__ == "__main__":
    A = input("Nhập chuỗi A: ")
    B = input("Nhập chuỗi B: ")
    result = sovle(A, B)
    print(result)