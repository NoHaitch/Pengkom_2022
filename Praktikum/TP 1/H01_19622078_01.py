# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 14 September 2022
# Deskripsi : Menentukan barang yang ditawarkan (keuntungan terbesar)

"""
    kode dibatasi menggunakan input, output dan percabangan

    Asumsi : 
        input pasti bilangan bulat positif 
        setiap pasangan harga suatu barang, memiliki nilai untung yang berbeda (selisih harga jual dan dasar)
        atau tidak ada 2 barang dengan keuntungan tertinggi

    variable :
        dasarA, dasarB, dasarC : int
        jualA, jualB, jualC : int
        untungA, untungB, untungC : int
"""

# Meminta input data
dasarA = int(input("Masukkan harga dasar barang A: "))
jualA = int(input("Masukkan harga jual barang A: "))
dasarB = int(input("Masukkan harga dasar barang B: "))
jualB = int(input("Masukkan harga jual barang B: "))
dasarC = int(input("Masukkan harga dasar barang C: "))
jualC = int(input("Masukkan harga jual barang C: "))

# Mencari keuntungan setiap barang
untungA = jualA-dasarA
untungB = jualB-dasarB
untungC = jualC-dasarC

# Cek jika keuntungan barang A lebih besar dari B dan C
if(untungA > untungB and untungA > untungC):
    # maka A paling untung
    print("Barang yang harus ditawarkan adalah barang A.")

# Cek jika keuntungan barang B lebih besar dari A dan C
elif(untungB > untungA and untungB > untungC):
    # maka B paling untung
    print("Barang yang harus ditawarkan adalah barang B.")

else: # Karena A dan B bukan yang terbesar maka C adalah yang terbesar
    # maka C paling untung
    print("Barang yang harus ditawarkan adalah barang C.")