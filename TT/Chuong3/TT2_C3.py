


from TT0_C3 import tach_chuoi

def last_occur(ABC,p):
    ABC = ABC.upper()
    p = p.upper()
    lst_ABC = tach_chuoi(ABC)
    lst_p = tach_chuoi(p)
    dic_ABC = {i:-1 for i in ABC}
    for i in lst_ABC:
        for j in range(len(lst_p)-1,-1,-1):
            if lst_p[j]==i:
                dic_ABC[i] = j
                break
    return dic_ABC

def boier_moore(ABC,m,p):
    lst_ABC = last_occur(ABC,p)
    lst_m = tach_chuoi(m.upper())
    lst_p = tach_chuoi(p.upper())
    i = len(lst_p) - 1
    while i < len(lst_m):
        for j in range(len(lst_p)-1,-2,-1):
            if lst_m[i] != lst_p[j]:
                i = i + len(lst_p) - min(j,1+lst_ABC[lst_m[i]])
                break
            else:
                i = i-1
                if j == 0:
                    return i+1
    return "Khong tim ra"

print(boier_moore("abcd","abacaabadcabacabaabb","abad"))

        