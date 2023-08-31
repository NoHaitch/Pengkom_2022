# NIM/Nama  : 19622078 / Raden Francisco Trianto Bratadiningrat
# Tanggal   : 9 November 2022
# Deskripsi : Mencari banyak kapal musuh dari peta ukuran NxM yang berisi 0/1. 
#             1 jika musuh, 0 jika laut, suatu kapal hanya dapat berbentuk vertikal/horizontal
""" 
KAMUS :
    M : matrix of int
    n, m : int
    i, j, a, count : int
    baris : string
    lanjut : bool
"""
# ALGORITMA

# minta input, asumsi n,m > 0
n = int(input("Masukkan N: "))
m = int(input("Masukkan M: "))

# inisialisasi M sebagai matriks peta
M = [[0 for _ in range(m)] for _ in range(n)]
print("Masukkan peta:")
for i in range(n):
    baris = input("") 
    # anggap input selalu benar yaitu M angka bernilai 0/1 
    # contoh input baris m = 5, baris = "10010" 
    # dan diasumsikan tidak ada kapal yang bersilangan
    for j in range(len(baris)):
        M[i][j] = int(baris[j])

# inisialisasi count sebagai total kapal musuh
count = 0
# Mulai mencari kapal musuh dari kiri atas menuju kanan bawah
for i in range(n):
    for j in range(m):
        # mencari kapal musuh
        if(M[i][j] == 1):
            M[i][j] = 0
            count = count + 1
            # karena mengecek ke kanan bawah maka hanya perlu membersihkan kanan dan bawah
            # cek kanan dan membersihkan bagian dari kapal musuh yang tersambung ke arah kanan
            if(i+1 <= n-1):
                if(M[i+1][j] == 1):
                    a = 1
                    lanjut = True
                    while lanjut:
                        if(i+a <= n-1):
                            if(M[i+a][j] != 0):
                                M[i+a][j] = 0
                                a = a +1
                            else:
                                lanjut = False
                        else:
                            lanjut = False
            # cek bawah dan membersihkan bagian kapal musuh yang tersambung ke arah bawah
            if(j+1 <= m-1):
                if(M[i][j+1] == 1):
                    a = 1
                    lanjut = True
                    while lanjut:
                        if(j+a <= m-1):
                            if(M[i][j+a] != 0):
                                M[i][j+a] = 0
                                a = a +1
                            else:
                                lanjut = False
                        else:
                            lanjut = False
# output
if(count == 0):
    print("Tidak terdapat kapal musuh pada peta.")
else:
    print(f"Terdapat {count} kapal musuh pada peta.")
