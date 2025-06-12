def solve(S, word):
    m = len(S)
    n = len(word)
    if n > m:
        return False
    for i in range(m - n + 1):
        doan_cat = S[i : i + n]
        if doan_cat == word:
            return True
    return False

s = input("Nhap chuoi sequence: ")
word = input("Nhap tu world: ")
k = 0
next_word = word
while solve(s, next_word):
    k += 1
    next_word += word

print(k)

    