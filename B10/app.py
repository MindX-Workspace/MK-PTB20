"""
    Đề bài: Tạo ra một ứng dụng cho phép người dùng đi chợ mua sắm. Ứng dụng có các chức năng sau:
        1. Xem được danh sách các sản phẩm
        2. Xem giỏ hàng đang có gì
        3. Thêm sản phẩm vào giỏ hàng
        4. Xoá sản phẩm khỏi giỏ hàng
        5. Thoát khỏi chương trình
"""

product_list = ["Quần", "Áo", "Giày", "Dép"]
cart = []

while True:
    print("1. Xem danh sách sản phẩm")
    print("2. Xem giỏ hàng")
    print("3. Thêm sản phẩm")
    print("4. Xoá sản phẩm")
    print("5. Thoát")

    choice = input("Nhập lựa chọn của bạn (1-5): ")
    # if choice == "1":