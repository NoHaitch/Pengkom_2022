# Deskripsi : Mengisi Matriks secara zig zag
"""
KAMUS:
    n, m, a, b : int
    i, j, num : int
    M : matrix (NxM) of int
"""
#ALGORTIMA
# minta semua input
n = int(input("Masukkan N: "))
m = int(input("Masukkan M: "))
a = int(input("Masukkan A: "))
b = int(input("Masukkan B: "))
# inisialisasi matriks M dengan besar NxM
M = [[0 for _ in range(m)] for _ in range(n)]
# inisialisasi num = 1 karena nilai baris 1 kolom 1 adalah 1 dan terus bertambah matriks terisi semua
num = 1
# pengulangan untuk semua baris
for i in range(n):
    # pengulangan semua kolom
    for j in range(m):
        # jika genap maka urutan normal
        if(i % 2 == 0):
            M[i][j] = num
            num = num + 1
        else: # jika ganjil urutan terbalik dari ujung dahulu
            j = m - j - 1
            M[i][j] = num
            num = num + 1
# output 
print(f"Nilai elemen tersebut adalah {M[a-1][b-1]}.")