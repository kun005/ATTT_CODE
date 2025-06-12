def solve(Q, pattern):
    list_upper = ""
    for char in Q:
        if 'A' <= char <= 'Z':
            list_upper += char
    
    return list_upper == pattern

N = int(input())
queries = [input() for _ in range(N)]
pattern = input()
for q in queries:
    res = solve(q, pattern)
    if res:
        print('true')
    else: 
        print('false')
    