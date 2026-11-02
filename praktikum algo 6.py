def tahun_kabisat(tahun):
    return tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)


def jumlah_hari(bulan, tahun):
    if bulan == 2:
        return 29 if tahun_kabisat(tahun) else 28
    elif bulan in (4, 6, 9, 11):
        return 30
    elif 1 <= bulan <= 12:
        return 31
    else:
        return None


try:
    bulan = int(input("Masukkan nomor bulan (1-12): "))
    tahun = int(input("Masukkan tahun: "))

    if tahun < 1:
        print("Tahun harus berupa bilangan positif.")
    else:
        hari = jumlah_hari(bulan, tahun)
        if hari is None:
            print("Bulan tidak valid. Masukkan angka 1 sampai 12.")
        else:
            print(f"Jumlah hari pada bulan {bulan} tahun {tahun} adalah {hari} hari.")
except ValueError:
    print("Input tidak valid. Masukkan angka bulat untuk bulan dan tahun.")
