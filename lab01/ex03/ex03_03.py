def tao_tuple_tu_list(lst):
    return tuple(lst)

# Nhập danh sách từ người dùng qua xâu ký tự
input_list = input("Nhập danh sách các số, các số ngăn cách nhau bằng dấu cách: ")
numbers = list(map(int, input_list.split(' ')))

# Tạo tuple từ list
my_tuple = tao_tuple_tu_list(numbers)

print("List:", numbers)
print("Tuple từ List:", my_tuple)