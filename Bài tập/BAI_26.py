

k = int(input("Nhập độ dài tiền tố: "))
n = int(input("Nhập số lượng chuỗi: "))
arr = []

for i in range(n):
    s = input(f"Nhập chuỗi thứ {i + 1}: ")
    arr += [s]

str_check = input("Nhập chuỗi cần kiểm tra: ")

# :k -> cắt chuỗi 
prefix = str_check[:k] #lấy tiền tố có độ dài k đầu tiên của chuỗi

count = 0
for s in arr:
    if s[:k] == prefix:
        #s[:k]; lấy k ký tự đầu tiên của chuỗi s trong arr
        count += 1

print(count)
