import math

# Hàm tính tổng hai phân số và rút gọn
def tinh_tong_phan_so(a, b, c, d):
    # Tính tử và mẫu của phân số tổng
    tu_tong = a * d + b * c
    mau_tong = b * d
    
    # Rút gọn phân số bằng cách tìm UCLN của tử và mẫu
    ucln = math.gcd(tu_tong, mau_tong)
    
    # Rút gọn tử và mẫu
    tu_rut_gon = tu_tong // ucln
    mau_rut_gon = mau_tong // ucln
    
    return tu_rut_gon, mau_rut_gon

# Nhập vào 4 số nguyên
a = int(input("Nhập tử số phân số thứ nhất: "))
b = int(input("Nhập mẫu số phân số thứ nhất: "))
c = int(input("Nhập tử số phân số thứ hai: "))
d = int(input("Nhập mẫu số phân số thứ hai: "))

# Kiểm tra mẫu số khác 0
if b == 0 or d == 0:
    print("Mẫu số không thể bằng 0.")
else:
    # Tính tổng và rút gọn
    tu, mau = tinh_tong_phan_so(a, b, c, d)
    
    # Xuất kết quả
    print(f"Tổng hai phân số sau khi rút gọn là: {tu}/{mau}")
