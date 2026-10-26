def ord_nilai_huruf(huruf):
    if huruf == "A":
        peringkat = 9
    elif huruf == "A-":
        peringkat = 8
    elif huruf == "B+":
        peringkat = 7
    elif huruf == "B":
        peringkat = 6
    elif huruf == "B-":
        peringkat = 5
    elif huruf == "C":
        peringkat = 4
    elif huruf == "C-":
        peringkat = 3
    elif huruf == "D":
        peringkat = 2
    elif huruf == "E":
        peringkat = 1
    else:
        peringkat = None
        
    return peringkat


total_nilai = 0
jumlah_data = 0

while True:
    input_huruf = input("Masukkan nilai huruf (atau ketik 'keluar' untuk berhenti): ")
    
    if input_huruf.lower() == "keluar":
        print("Program selesai. Terima kasih!")
        break
        
    hasil = ord_nilai_huruf(input_huruf)
    print(f"Peringkat untuk nilai {input_huruf} adalah: {hasil}\n")
    
    
    if hasil is not None:
        total_nilai += hasil
        jumlah_data += 1


if jumlah_data > 0:
    rata_rata = total_nilai / jumlah_data
    print(f"Rata-rata peringkat: {rata_rata}")