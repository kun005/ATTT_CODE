#Trên đường cong elliptic E giả sử P=(x1, y1) và Q=(x2, y2) là hai điểm trên đường cong Ep(a,b), phép cộng được định nghĩa như sau:
#Nếu x2 =x1, y 2 = -y1 thì P + Q = O(0,0)
#Ngược lại P + Q = (x3, y3) 
#Các phép tính đều được tính trên modulo p, p là số nguyên tố.

import sys
sys.path.insert(0, './TT/Chuong1')
import TT8_C1

def add_points(P, Q, a, b, p):
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0:
        return (0, 0)
    if x1 == x2 and y1 == y2:
        tu = (3 * x1 * x1 + a) % p
        mau = (2 * y1) % p
    else:
        tu = (y2 - y1) % p
        mau = (x2 - x1) % p 

    inv_mau =TT8_C1.Invert_Fp(mau, p)
    y = (tu * inv_mau) % p 
    
    x3 = (y * y - x1 - x2) % p 
    y3 = (y * (x1 - x3) - y1) % p 
    return (x3, y3)


if __name__ == "__main__":
    p = int(input("Nhập số nguyên tố p: "))
    a = int(input("Nhập a: "))
    x1, y1 = map(int, input("Nhập tọa độ điểm P (x1, y1): ").split())
    x2, y2 = map(int, input("Nhập tọa độ điểm Q (x2, y2): ").split())
    res = add_points((x1, y1), (x2, y2), a, 0, p)
    if res == (0, 0):
        print("P + Q = O(0, 0)")
    else:
        print(f"P + Q = ({res[0]}, {res[1]})")