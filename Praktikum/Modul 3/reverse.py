"""
Program : Reverse
Spesifikasi : menerima N buah bilangan dan menuliskan kembali bilangan tersebut dengan urutan terbalik
Asumsi : input pasti bilangan bulat positif

Kamus :
    n,x : int
    angka : array int
"""

# ALGORITMA

# Meminta N
n = int(input("Masukan N: "))
# Inisialisasi list/array
angka = []
# Meminta data untuk list
for _ in range(n):
    angka.append(int(input("")))
# Print dengan urutan terbalik
for x in angka[::-1]:
    print(f"{x} ",end="")
print()