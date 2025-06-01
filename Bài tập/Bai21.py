from TT.Chuong3.Brute_force import Vet_can

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