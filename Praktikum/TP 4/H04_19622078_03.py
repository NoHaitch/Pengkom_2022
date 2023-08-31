# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 11 November 2022
# Deskripsi : dokumentasi tour dengan foto barisan bangunan, cari total foto bangungan paling besar yang terlihat(bangunan tidak boleh <= bangunan sebelumnya) dalam satu garis lurus dari atas ke bawah atau sebaliknya

"""
    Asumsi : 
        input int bilangan bulat positif
    KAMUS :
        n, i, j, maks, sum : int
        terlihat : bool
        kota : matriks 2D int
"""
# ALGORITMA
# meminta besar kota
n = int(input("Masukkan besar Kota Kompeng: "))
# inisialisasi matriks kota
kota = [[0 for _ in range(n)] for _ in range(n)]
# meminta input matriks kota
for i in range(n):
    for j in range(n):
        kota[i][j] = int(input(f"Masukkan tinggi bangunan baris {i+1} kolom {j+1}: "))
# inisialisasi maks, -1 karena maks baru tidak mungkin negatif
maks = -1
# mencari maksimum baru dari total foto dari atas ke bawah
for j in range(n):
    # inisialisasi sum untuk total baris ini, dan tertinggi untuk bangungan tertinggi saat ini
    sum = 0
    tertinggi = -1
    for i in range(n):
        # jika bangunan lebih tinggi maka simpan tinggi dan tambahkan ke sum
        if(kota[i][j] > tertinggi):
            tertinggi = kota[i][j]
            sum = sum + kota[i][j]
    # jika total lebih besar dari maksimum
    if(sum > maks):
        maks = sum
# mencari maksimum baru dari total foto dari bawah ke atas
for j in range(n):
    # inisialisasi sum untuk total baris ini, dan tertinggi untuk bangungan tertinggi saat ini
    sum = 0
    tertinggi = -1
    for i in range(n):
        i = (n-1)-i
         # jika bangunan lebih tinggi maka simpan tinggi dan tambahkan ke sum
        if(kota[i][j] > tertinggi):
            tertinggi = kota[i][j]
            sum = sum + kota[i][j]
    # jika total lebih besar dari maksimum
    if(sum > maks):
        maks = sum    
# output
print(f"Foto terbaik memiliki total tinggi: {maks}")