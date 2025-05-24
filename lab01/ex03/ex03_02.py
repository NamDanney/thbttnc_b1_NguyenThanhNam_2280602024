def dao_nguoc_list(lst):
    return lst[::-1]

# Nhập danh sách từ người dùng qua xâu ký tự
input_list = input("Nhập danh sách các số, các số ngăn cách nhau bằng dấu cách: ")
numbers = list(map(int, input_list.split(' ')))

# Sử dụng hàm và in kết quả
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi đảo ngược:", list_dao_nguoc)