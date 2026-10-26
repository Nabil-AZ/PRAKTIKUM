print("=== PROGRAM HITUNG TIKET KEBUN BINATANG ===")
print("Selesai memasukkan umur? Tekan 'Enter' tanpa mengetik angka.\n")

total_harga = 0
jumlah_pengunjung = 0

while True:
    input_umur = input(f"Masukkan umur pengunjung ke-{jumlah_pengunjung + 1}: ")
    
    if input_umur == "":
        break
        
    try:
        umur = int(input_umur)
        
        if umur < 0:
            print("Umur tidak valid. Silakan masukkan angka positif.")
            continue

        if umur <= 2:
            harga = 0
            kategori = "Gratis"
        elif 3 <= umur <= 12:
            harga = 14
            kategori = "$14"
        elif umur >= 65:
            harga = 18
            kategori = "$18"
        else:
            harga = 23
            kategori = "$23 (Normal)"
            
        print(f"-> Kategori: {kategori}")
        total_harga += harga
        jumlah_pengunjung += 1
        
    except ValueError:
        print("Input harus berupa angka bulat!")

print("\n===========================================")
print(f"Total pengunjung : {jumlah_pengunjung} orang")
print(f"Total Harga Tiket: ${total_harga}")
print("===========================================")

if total_harga > 0:
    while True:
        try:
            uang_dibayar = float(input("Masukkan jumlah uang pembayaran: $"))
            
            if uang_dibayar < total_harga:
                print(f"Uang Anda kurang! Dibutuhkan minimal ${total_harga}")
            else:
                kembalian = uang_dibayar - total_harga
                print(f"Pembayaran berhasil.")
                print(f"Uang Kembalian : ${kembalian:.2f}")
                break
        except ValueError:
            print("Input uang harus berupa angka!")
else:
    print("Tidak ada biaya yang perlu dibayar (Total: $0).")

print("\nTerima kasih, selamat menikmati kunjungan Anda!")
