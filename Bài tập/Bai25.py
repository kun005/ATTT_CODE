def check(mau, chuoi_ktra):
    m = len(mau)
    n = len(chuoi_ktra)
    if m != n: return False
    map1 = {} # kí tự mẫu -> ký tự hành vi'
    map2 = {} # kí tự hành vi -> kí tự mẫu
    
    for i in range(len(mau)):
        ktu_mau = mau[i]
        ktu_hvi = chuoi_ktra[i]
        if ktu_mau in map1:
            if map1[ktu_mau] != ktu_hvi:
                return False
        elif ktu_hvi in map2:
            return False
        else:
            map1[ktu_mau] = ktu_hvi
            map2[ktu_hvi] = ktu_mau
    return True

N = int(input("Nhập số lượng các hành vi trong CSDL: "))
ds_hanh_vi = []
for _ in range(N):
    hanh_vi = input()
    ds_hanh_vi += [hanh_vi]
    
mau_can_tim = input("Chuỗi ký tự đại diện cho mẫu hành vi: ")
res =[]
for hanh_vi in ds_hanh_vi:
    if check(mau_can_tim, hanh_vi):
        res += [hanh_vi]
for kq in res:
    print(kq, end=" ")
  
        