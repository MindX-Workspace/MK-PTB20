"""
Tính giai thừa

Viết một hàm giai_thua(n) tính giai thừa của số nguyên dương n.
Ví dụ: giai_thua(5) sẽ trả về 120.
"""

def giai_thua(n):
    if n < 0:
        return "Không tồn tại giai thừa cho số âm"
    elif n == 0 or n == 1:
        return 1
    else:
        giai_thua_result = 1
        for i in range(2, n + 1):
            giai_thua_result *= i
        return giai_thua_result

# Ví dụ sử dụng
result = giai_thua(5)
print(f"Giai thừa của 5 là: {result}")
