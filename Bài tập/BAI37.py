def solve(s, goal):
    m = len(s)
    n = len(goal)
    
    if m != n:
        return False
    for i in range (m):
        first = s[0]
        last = s[1:]
        s = last + first
        
        if s == goal:
            return True
    return False

s = input("Nhập chuỗi ký tự s: ")
goal = input("Nhập chuỗi ký tự goal: ")
res = solve(s, goal)

