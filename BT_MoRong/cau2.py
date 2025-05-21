import re

def tong_cac_so_trong_chuoi(chuoi_vao):

    cac_so = re.findall(r'-?\d+', chuoi_vao)
    
    cac_so = [int(so) for so in cac_so]
    
    # Tính tổng
    tong_duong = sum(so for so in cac_so if so > 0)
    tong_am = sum(so for so in cac_so if so < 0)
    
    return tong_duong, tong_am

chuoi_kiem_tra = "-100#^sdfkj8902w3ir021@swf-20"
ket_qua_duong, ket_qua_am = tong_cac_so_trong_chuoi(chuoi_kiem_tra)

print(f"Chuỗi ban đầu là \"{chuoi_kiem_tra}\"")
print(f"Kết quả: Giá trị dương: {ket_qua_duong}. Giá trị âm: {ket_qua_am}.")