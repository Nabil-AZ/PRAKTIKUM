def bilangan(angka):
    if angka <= 1:
        return False
    for i in range(2, angka):
        if angka % i == 0:
            return False
    else:
        return True
    
def hasil(angka):
    if bilangan(angka):
        return print(f"{angka} adalah bilangan prima")
    else:
        return print(f"{angka} bukan bilangan prima")

nomor = int(input("Masukkan angka: "))
hasil(nomor)