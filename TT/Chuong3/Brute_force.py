def Vet_can(T, P):
    n = len(T)  
    m = len(P)  

    for i in range(n - m + 1):  
        match = 1
        for j in range(m):  # kiểm tra từng ký tự của P với T tại vị trí i
            if T[i + j] != P[j]:
                match = 0
                break  # không khớp -> dừng kiểm tra và thử vị trí tiếp theo
        if match == 1:
            return i  # trả về vị trí đầu tiên tìm thấy P trong T

    return -1  



# if __name__ == "__main__": 
#     T = input("Nhập chuỗi văn bản (T): ")
#     P = input("Nhập chuỗi mẫu (P): ")
#     result = Vet_can(T, P)
#     if result != -1:
#         print(f"Mẫu '{P}' xuất hiện tại vị trí: {result}")
#     else:
#         print (-1)
        