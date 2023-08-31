# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 11 November 2022
# Deskripsi : Menumpuk barang dengan beratnya, tumpukan dalam bentuk matriks, setiap terbawah harus terberat dari tumpukan tersebut

"""
    Asumsi : 
        input int pasti bilangan bulat positif
    KAMUS :
        tinggi, banyak, i, j : int
        sesuai : bool
        barang : matriks 2D
"""
# ALGORITMA
# meminta input tinggi dan banyak tumpukkan
tinggi = int(input("Masukkan tinggi tumpukan: "))
banyak = int(input("Masukkan banyak tumpukkan: "))
# inisialisasi matriks barang
barang = [[0 for _ in range(banyak)] for _ in range(tinggi)]
# inisialisasi sesuai untuk pengecekan apakah tumpukan sesuai atau tidak
sesuai = True
# meminta input matriks barang
for i in range(tinggi):
    for j in range(banyak):
        barang[i][j] = int(input(f"Masukkan berat benda pada baris ke-{i+1} kolom ke-{j+1}: "))
# mengecek apakah setiap tumpukkan sesuai atau tidak
for i in range(tinggi):
    # jika sudah ditemukan tidak sesuai maka pengecekan tidak perlu dilanjutkan
    if(sesuai == False):
            continue
    for j in range(banyak):
        # jika sudah ditemukan tidak sesuai maka pengecekan tidak perlu dilanjutkan
        if(sesuai == False): 
            continue
        # jika tidak sesuai maka sesuai = False
        if(barang[tinggi-1][j] < barang[i][j]):
            sesuai = False
# output hasil
if(sesuai):
    print("Susunan tersebut memenuhi perintah Tuan Leo.")
else:
    print("Susunan tersebut tidak memenuhi perintah Tuan Leo.")