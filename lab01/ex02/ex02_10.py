def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
intput_string = input("Nhập vào một chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(intput_string))