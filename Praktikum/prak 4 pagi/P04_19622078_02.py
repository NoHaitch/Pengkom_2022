# Deskripsi : menghilangkan baris i dan kolom j dari matriks MxN
"""
KAMUS:
    M, N: matrix of int
    n, m, i, j : int
    a, b : int
    valid : bool
"""
#ALGORTIMA
# minta semua input
m = int(input("Masukkan M: "))
n = int(input("Masukkan N: "))
valid = True
while valid:
    i = int(input("Masukkan i: "))
    j = int(input("Masukkan j: "))
    if(0<j<=m and 0<i<=n):
        valid = False
        continue
    print("baris dan kolom harus lebih kecil sama dengan ukuran matriks")
M = [[0 for _ in range(m)] for _ in range(n)]
for y in range(n):
    for x in range(m):
        M[y][x] = int(input(f"Masukkan elemen baris {y+1} kolom {x+1}: "))
N = [[0 for _ in range(m-1)] for _ in range(n-1)]
a, b = 0, 0
for y in range(n):
    if(y != i-1):
        for x in range(m):
            if(x != j-1):
                N[a][b] = M[y][x]
                b = b + 1
        a = a + 1
        b = 0
for i in N:
    for j in i:
        print(j,end=" ")
    print()