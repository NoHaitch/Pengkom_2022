# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 14 September 2022
# Deskripsi : Menentukan kelas dari NIM

"""
    kode dibatasi menggunakan input, output dan percabangan

    Asumsi : 
        input pasti bilangan bulat positif

    variable :
        nim : int
"""

# Meminta input
nim = int(input("Masukan akhiran NIM: "))

# Membagi kasus jika nim > 300 , > 200, > 100, dan <= 100
if(nim > 300):
    # Karena nim > 300 maka: ganjil masuk kelas K7 dan genap masuk kelas K8
    if(nim % 2 == 0):
        # genap
        print("Mahasiswa masuk ke kelas K8.")
    else:
        # ganjil
        print("Mahasiswa masuk ke kelas K7.")

elif(nim > 200):
    # Karena nim > 200 tapi nim tidak > 300 maka: ganjil masuk kelas K5 dan genap masuk kelas K6
    if(nim % 2 == 0):
        # genap
        print("Mahasiswa masuk ke kelas K6.")
    else:
        # ganjil
        print("Mahasiswa masuk ke kelas K5.")

elif(nim > 100):
    # Karena nim > 100 tapi nim tidak > 200 maka: ganjil masuk kelas K3 dan genap masuk kelas K5
    if(nim % 2 == 0):
        # genap
        print("Mahasiswa masuk ke kelas K4.")
    else:
        # ganjil
        print("Mahasiswa masuk ke kelas K3.")

else:
    # Karena nim <= 100 serta nim > 0 maka: ganjil masuk kelas K1 dan genap masuk kelas K2
    if(nim % 2 == 0):
        # genap
        print("Mahasiswa masuk ke kelas K2.")
    else:
        # ganjil
        print("Mahasiswa masuk ke kelas K1.")