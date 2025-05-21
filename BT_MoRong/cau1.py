import itertools

def liet_ke_hoan_vi(lst):
    hoan_vi = list(itertools.permutations(lst))
    print(f"Tất cả các hoán vị của {lst}:")
    for hv in hoan_vi:
        print(hv)
    return hoan_vi

danh_sach_goc = [1, 2, 3]
tat_ca_hoan_vi = liet_ke_hoan_vi(danh_sach_goc)
print(f"Tổng số hoán vị: {len(tat_ca_hoan_vi)}")