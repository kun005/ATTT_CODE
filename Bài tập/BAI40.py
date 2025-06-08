
def check(s1, s2):
    m = len(s1)
    n = len(s2)
    
    if m > n:
        return False
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if s2[i + j] != s1[j]:
                break
            j += 1
        if j == m:
            return True
    return False

N = int(input("Nhap N: "))
words = [input() for _ in range(N)]

res = []
for i in range(N):
    # chuoi ktra
    c_ktra = words[i]
    for j in range(N):
        if i == j:
            continue
        #: chuoi so sanh
        c_sosanh = words[j]
        
        if check(c_ktra, c_sosanh):
            res += [c_ktra]
            break
if not res:
    print("None")
else:
    for i in range(len(res)):
        print(res[i], end = " ")
