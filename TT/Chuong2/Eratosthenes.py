import math

n = 10000000
prime = [1] * (n + 1)  # Bước 1: Giả sử tất cả các số từ 0 đến n đều là số nguyên tố

def sang():
    # Bước 2: Sàng
    prime[0] = prime[1] = 0  # 0 và 1 không phải là số nguyên tố
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i] == 1:
            for j in range(i * i, n + 1, i):
                prime[j] = 0  # Loại bỏ các số không phải số nguyên tố

sang()

n = int(input("Nhập n: "))
for i in range(n + 1):
    if prime[i]:
        print(i, end=" ")
