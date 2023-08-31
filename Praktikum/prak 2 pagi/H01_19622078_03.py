# Deskripsi: Mengelompokan kamar kepada 9 ruang makan yang dipisah 
# dengan menghitung digit hingga tersisa satu digit dan itu menjadi kelompoknya

# ALGORITMA

n = int(input("Masukkan nomor kamar: "))
noskrg = n
print(n,end="")
while len(str(noskrg)) > 1:
    jumlah_digit = 0
    for digit in str(noskrg):
        jumlah_digit = jumlah_digit + int(digit)
    noskrg = jumlah_digit
    print(f" -> {noskrg}",end="")
print(f"\nKamar {n} akan termasuk ke dalam ruang makan {noskrg}.") 