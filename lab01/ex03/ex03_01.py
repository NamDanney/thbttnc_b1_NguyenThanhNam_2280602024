def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

# Nhập danh sách các số từ người dùng qua một xâu ký tự
input_list = input("Nhập danh sách các số, các số ngăn cách nhau bằng dấu cách: ")
numbers = list(map(int, input_list.split(' ')))

# Sử dụng hàm và in kết quả
tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong List là:", tong_chan)