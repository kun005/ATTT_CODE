def invert(a, p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = v // u
        r = v - q * u
        x = x2 - q * x1
        
        v = u
        u = r
        x2 = x1
        x1 = x
    return (x1 % p + p) % p
def solve():
    k = int(input("Nhap so phuong trinh: "))
    a_list = [0] * k
    n_list = [0] * k
    for i in range(k):
        a_list[i], n_list[i] = map(int, input().split())
        
    #tính N = n1 * n2 *... *nk
    N = 1
    for i in range(k):
        N *= n_list[i]
    #tinh sum
    sum = 0
    for i in range(k):
        a_i = a_list[i]
        n_i = n_list[i]
        
        Ni = N // n_i 
        Mi = invert(Ni, n_i)
        sum += a_i * Ni * Mi 
    x = sum % N
    print(x)
    
if __name__ == "__main__":
    solve()
    