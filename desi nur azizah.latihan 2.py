import  math
print("1. menghitung keliling lingkaran")
print("2. menghitung luas lingkaran")
pilihan = int(input("masukan pilihan (1/2): "))
r = float(input("masukan jari-jari lingkaran: "))
if pilihan == 1:
    keliling = 2 * math.pi * r
    print("keliling lingkaran =", keliling)
elif pilihan == 2:
    luas = math.pi * r * r
    print("luas lingkaran =", luas)
else:
    print("pilihan tidak valid")