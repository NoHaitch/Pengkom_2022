# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 15 September 2022
# Deskripsi : Menentukan waktu lari Tuan Riz

"""
    kode dibatasi menggunakan input, output dan percabangan

    Asumsi : 
        input pasti bilangan bulat positif,
        nilai jam dibatasi 24, menit 60, detik 60
        pasti ada yang berbeda tidak mungkin waktu mulai sama dengan waktu akhir
        waktu selesai pasti lebih dulu dibanding waktu mulai 

    variable :
        jam0, jam1, jam: int
        menit0, menit1, menit :int
        detik0, detik1, detik :int
"""

# Meminta waktu mulai 
print("Masukan waktu mulai !")
jam0 = int(input("Jam   : "))
menit0 = int(input("Menit : "))
detik0 = int(input("Detik : "))

# Meminta waktu selesai
print("Masukan waktu selesai !")
jam1 = int(input("Jam   : "))
menit1 = int(input("Menit : "))
detik1 = int(input("Detik : "))

# Mendapatakan selisih menit yang dibedakan jika menit mulai lebih besar dari menit selesai
if(jam0 > jam1):
    jam = jam1 + (24 - jam0)
else: 
    # jika menit selesai lebih besar sama dengan menit mulai
    jam = jam1 - jam0

# Mendapatakan selisih menit yang dibedakan jika menit mulai lebih besar dari menit selesai
if(menit0 > menit1):
    menit = menit1 + (60 - menit0)
else: 
    # jika menit selesai lebih besar sama dengan menit mulai
    menit = menit1 - menit0

# Mendapatakan selisih detik yang dibedakan jika detik mulai lebih besar dari detik selesai
if(detik0 > detik1):
    detik = detik1 + (60 - detik0)
else: 
    # jika detik selesai lebih besar sama dengan detik mulai
    detik = detik1 - detik0

# Memulai menyusun kalimat output
print("Tuan Riz berlari selama ",end="")
if(jam != 0):
    # karena ada perbedaan jam, maka dimasukan ke dalam kalimat
    print(f"{jam} jam",end="")
if(menit != 0):
    # karena ada perbedaan menit, maka dimasukan ke dalam kalimat
    if(jam != 0): # hanya untuk menambah spasi
        print(" ",end="")
    print(f"{menit} menit",end="")
if(detik != 0):
    # karena ada perbedaan detik, maka dimasukan ke dalam kalimat
    if(menit != 0 or jam != 0): # hanya untuk menambah spasi
        print(" ",end="")
    print(f"{detik} detik",end="")
# Mengakhiri penyusunan kalimat dengan titik
print(".")