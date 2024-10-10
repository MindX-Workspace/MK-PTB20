"""
Kiểm tra số nguyên tố

Viết một hàm kiem_tra_nguyen_to(n) để kiểm tra xem một số có phải là số nguyên tố hay không.
Ví dụ: kiem_tra_nguyen_to(7) sẽ trả về True vì 7 là số nguyên tố.
"""

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True 
n = int(input("Nhập một số: "))
if kiem_tra_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
