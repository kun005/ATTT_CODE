def solve(sentence, searchWord):
    words = sentence.split(' ')
    match = False
    for i in range(len(words)):
        tmp = words[i]
        if len(searchWord) <= len(tmp):
            prefix = tmp[0 : len(searchWord)]
            if prefix == searchWord:
                print(i + 1)
                match = True
                break #key 
    if not match:        
        return -1


s = input("Nhap chuoi cac tu: ")
sw = input("Nhap tu searchWord: ")
res = solve(s, sw)
