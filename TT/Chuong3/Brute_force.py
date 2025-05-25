def Vet_can(T, P):
    n = len(T)  # độ dài chuỗi văn bản
    m = len(P)  # độ dài mẫu

    for i in range(n - m + 1):  # thử tất cả các vị trí có thể của P trong T
        match = 1
        for j in range(m):  # kiểm tra từng ký tự của P với T tại vị trí i
            if T[i + j] != P[j]:
                match = 0
                break  # không khớp -> dừng kiểm tra và thử vị trí tiếp theo
        if match:
            return i  # trả về vị trí đầu tiên tìm thấy P trong T

    return -1  # không tìm thấy



if __name__ == "__main__":
    T = input("Nhập chuỗi văn bản (T): ")
    P = input("Nhập chuỗi mẫu (P): ")
    result = Vet_can(T, P)
    if result != -1:
        print(f"Mẫu '{P}' xuất hiện tại vị trí: {result}")
    else:
        print(f"Mẫu '{P}' không được tìm thấy trong chuỗi văn bản.")