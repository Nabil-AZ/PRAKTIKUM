bulan = int(input("masukkan bulan (1-12): "))
tahun = int(input("masukkan tahun: "))

if bulan == 2:
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        print("Bulan", bulan, "pada tahun", tahun, "memiliki 29 hari.")
    else:
        print("Bulan", bulan, "pada tahun", tahun, "memiliki 28 hari.")
else:
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        print("Bulan", bulan, "pada tahun", tahun, "memiliki 31 hari.")
    else:
        print("Bulan", bulan, "pada tahun", tahun, "memiliki 30 hari.")
