
#tạo hàm phụ lưu các nguyên âm 
def vowel(char):
    if char in ['a', 'e', 'i', 'o', 'u']:
        return char
    
    
def solve(s):
    n = len(s)
    memo = {}
    def bad(index, v_cout, c_cout):
    # TH1: vi pham dk BAD
        if v_cout > 5 or c_cout > 3: 
            return True #Bad
        
    # TH2: đã duyệt hết chuỗi nhưng không vi phạm 
        if index == n:
            return False #GOOD

        state = (index, v_cout, c_cout)
        if state in memo:
            return memo[state]
        
        curent_char = s[index]
        res = False
        if curent_char == '?':
            #check '?' la nguyen am
            if bad(index + 1, v_cout + 1, 0):
                res = True
            if not res:
                if bad(index + 1, 0, c_cout + 1):
                    res = True
        else:
            #ký tự là chữ cái cố định
            if vowel(curent_char):
                if bad(index + 1, v_cout + 1, 0):
                    res = True
            else: #là phụ âm
                if bad(index + 1, 0, c_cout + 1):
                    res = True
        memo[state] = res
        return res
    
    if bad(0, 0, 0):
        return "BAD"
    else:
        return "GOOD"
    
if __name__ == "__main__":
    s = input("Nhap chuoi ky tu S: ")
    kq = solve(s)
    print(kq)