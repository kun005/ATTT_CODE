def solve(s):
    n = len(s)
    
    dem = 0
    i = 0
    while i < n:
        if s[i] == '1':
            j = i + 1
            if  s[j] == '0':
                j = j
                while s[j] == '0':
                    j += 1

                if s[j] == '1':
                    dem += 1
                    i = j + 1
                else: #TH la 100a hoặc 100
                    i += 1
            else:#TH là 1a hoặc 11
                i += 1
        else:#TH kí tự hiện tại không phải 1
            i += 1
    return dem 

s = input("Nhập chuỗi ký tự:")
res = solve(s)
print(res)