def kt_lap(s):
    n = len(s)
    check = False
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            p = s[:i]
            k = n // i
            chuoi_moi = ""
            for _ in range(k):
                chuoi_moi += p
            if chuoi_moi == s:
                check = True
                break 
    if check:
        print("YES")
    else: print("NO")

s = input("Nhập chuỗi kí tự s: ")
kt_lap(s)
