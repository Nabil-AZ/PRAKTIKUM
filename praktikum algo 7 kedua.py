def ordinal(angka):
    if angka % 10 == 1 and angka % 100 != 11:
        return str(angka) + "st"
    elif angka % 10 == 2 and angka % 100 != 12:
        return str(angka) + "nd"
    elif angka % 10 == 3 and angka % 100 != 13:
        return str(angka) + "rd"
    else:
        return str(angka) + "th"

user = int(input("Masukkan angka: "))
print(f"Angka {user} dalam bentuk ordinal adalah: {ordinal(user)}")