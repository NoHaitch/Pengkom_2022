# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 20 Oktober 2022
# Deskripsi : Menghitung banyaknya kemunculan substring pada string, input hanya terdiri dari huruf kecil a-z dan substring tidak lebih besar dari string utama

"""
    Asumsi : 
        input int pasti bilangan bulat positif
        input string hanya a-z
    KAMUS :
        nstr1, nstr2, kemunculan, count_sama, i, j : int
        str1, str2 : string 
"""
#Algoritma

# meminta panjang string 1 sebagai nstr1
nstr1 = int(input("Masukkan panjang string 1: "))
# meminta string 1 sebagai str1
str1 = input("Masukkan string 1: ")
while len(str1) != nstr1:
    print("Panjang string 1 harus sesuai")
    str1 = input("Masukkan string 1: ")
# meminta panjang string 2 sebagai nstr2
nstr2 = int(input("Masukkan panjang string 2: "))
# meminta string 2 sebagai str2
str2 = input("Masukkan string 2: ")
while len(str2) != nstr2:
    print("Panjang string 2 harus sesuai")
    str2 = input("Masukkan string 2: ")
# inisialisasi total kemunculan str1 di str2
kemunculan = 0
# untuk setiap index i di str2
for i in range(nstr2):
    # inisialisasi penghitung jumlah kesamaan str1 dengan str2 dari index i
    count_sama = 0
    for j in range(nstr1):
        if(i+j <= nstr2-1):
            # menggunakan string indexing --> menganggap string sebagai array yang terdiri dari karakter
            if(str2[i+j] == str1[j]):
                count_sama = count_sama + 1
    # jika count_sama nilainya sama dengan panjang str1 maka benar ditemukan str1 di str2
    if(count_sama == nstr1):
        kemunculan = kemunculan + 1
print(f"String 1 muncul sebanyak {kemunculan} kali.")
