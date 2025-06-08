# Hàm kiểm tra xem prefix có phải là tiền tố của từ khác không
def check_pre(prefix, word, words, index):
    #xử lý 2 TH đặc biệt
    for j in range(len(words)):
        if j == index:
            continue
        other = words[j]
        if len(other) < len(prefix):
            continue
        
        match = True
        #so sánh từng ký tự của prefix với phần đầu của từ khác
        for k in range(len(prefix)):
            if prefix[k] != other[k]:
                match = False
                break
        if match:
            #prefix không còn là duy nhất
            return False
    return True

n = int(input("Nhập n: "))
words = ["" for _ in range(n)]

for i in range(n):
    words[i] = input()

# Khởi tạo kết quả là một danh sách rỗng có sẵn độ dài
result = [""] * n

# Tìm tiền tố ngắn nhất duy nhất cho mỗi từ
for i in range(n):
    word = words[i]
    #độ dài của prefix
    for length in range(1, len(word) + 1):
        prefix = ""
        for p in range(length):
            prefix += word[p]
        if check_pre(prefix, word, words, i):
            result[i] = prefix
            break

# In kết quả 
output = ""
for i in range(n):
    output += result[i]
    if i != n - 1:
        output += " "
print(output)
