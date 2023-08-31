"""
Program : Ganjil-Genap
Spesifikasi : Menentukan bilangan ganjil atau genap jika menerima bilangan positif
Asumsi : input pasti bilangan bulat
Kamus :
    x : int
"""
# ALGORITMA

# Menerima bilangan input sebagai x
x = int(input("\nMasukan nilai N: "))

# Mengecek apakah bilangan positif atau tidak
if(x <= 0):
    # Mengecek apakah bilangan negatif atau bernilai 0
    if(x == 0):
        print(f"{x} bukan bilangan positif atau negatif")
    else:
        print(f"{x} bilangan negatif")
else:
    # Mengecek bilangan positif jika genap atau ganjil
    if(x % 2 == 0):
        print(f"{x} bilangan positif genap")
    else:
        print(f"{x} bilangan positif ganjil")
