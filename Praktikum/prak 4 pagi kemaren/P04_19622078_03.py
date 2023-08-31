# Deskripsi : bidak katak "K" pada papan catur serta gerakannya "#" (lompat 2 ke depan/belakang; lompat 3 ke kanan/kiri)
"""
KAMUS:
    n, m, x, y, i, j : int
    M : matrix (NxN) of string
"""
#ALGORTIMA
# meminta input
n = int(input("Masukkan nilai N: "))
m = int(input("Masukkan banyak bidak: "))
# inisialisasi matriks M yang terdiri dari string "."
M = [["." for _ in range(n)] for _ in range(n)]
for i in range(m):
    # meminta posisi bidak ke-i
    valid = True
    while valid:
        x = int(input(f"Masukkan posisi x bidak {i+1}: "))
        y = int(input(f"Masukkan posisi y bidak {i+1}: "))
        if(0<x<=n and 0<y<=n):
            valid = False
            continue
        print("Posisi bidak harus di dalam matriks.")
    M[y-1][x-1] = "K"
    # mengecek apakah bidak bisa bergerak atau tidak 
    if(x-4 >= 0):
        if(M[y-1][x-4] != "K"):
            M[y-1][x-4] = "#"
    if(x+2 <= n-1):
        if(M[y-1][x+2] != "K"):
            M[y-1][x+2] = "#"
    if(y-3 >= 0):
        if(M[y-3][x-1] != "K"):
            M[y-3][x-1] = "#"
    if(y+1 <= n-1):
        if(M[y+1][x-1] != "K"):
            M[y+1][x-1] = "#"
    # output papan
for i in M:
    for j in i:
        print(j,end=" ")
    print()
