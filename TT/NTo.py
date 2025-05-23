import math
def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def print_prime(n):                 #hàm in ra các số nguyên tố có n chữ số
    start = 10**(n-1)                   # Starts from 10^(n-1)
    end = 10**n                         # Ends at 10^n )
    print(f"Các số nguyên tố có {n} chữ số là:")
    found_primes = 0      #bắt đầu gán = 0
    for i in range(start, end):
        if is_prime(i):
            print(i, end=" ")    #end=" "-> sau khi in xong số i, không xuống dòng, mà chỉ in thêm một khoảng trắng
            found_primes = 1
    if not found_primes:
        print(f"Không tìm thấy số nguyên tố nào có {n} chữ số trong khoảng này.")
    else:
        print() 

# Main 
n = int(input("Nhap so chu so cua so nguyen to tròn doan [2,10]: "))

while n < 2 or n > 10:
    n = int(input("Nhap lai n, 2 <= n <= 10: "))

print_prime(n)                      #Gọi hàm in ra các số nguyên tố có n chữ số

