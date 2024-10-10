"""
Kiểm tra số chẵn/lẻ

Viết một hàm kiem_tra_chan_le(n) để kiểm tra xem một số có phải là số chẵn hay lẻ.
Ví dụ: kiem_tra_chan_le(5) sẽ in ra "5 là số lẻ".
"""

def check(n):
    if n % 2 == 0:
        print(f"{n} là số chẵn")
    else:
        print(f"{n} là số lẻ")

check(5)