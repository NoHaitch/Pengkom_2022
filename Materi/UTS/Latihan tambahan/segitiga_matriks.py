# Program : Matriks Segitiga Atas
# Deskripsi: Diberikan sebuah matriks tentukan apakah segitga bagian atas(persegi potong diagonal ke bawah) terisi dengan bilangan bukan nol dan sisanya harus bernilai no
"""
Kamus:
    a, b, i, j : int
    sesuai : bool
    matriks : matriks 2D int
"""

# ALGORTIMA
a = int(input("Masukkan tinggi matriks(baris): "))
b = int(input("Masukkan lebar matriks(kolom): "))
matriks = [[0 for _ in range(b)] for _ in range(a)]
for i in range(a):
    for j in range(b):
        matriks[i][j] = int(input(f"Masukkan baris ke-{i+1} kolom ke-{j+1}: "))
if(a != b or a < 2):
    print("Bukan matriks segitiga.")
else:
    sesuai = True
    for i in range(a):
        if(sesuai == False):
            continue
        for j in range(i,a):
            if(sesuai == False):
                continue
            if(matriks[i][j] == 0):
                sesuai = False
    for i in range(1,a):
        if(sesuai == False):
            continue
        for j in range(i-1):
            if(sesuai == False):
                continue
            if(matriks[i][j]): 
                sesuai = False
    if(sesuai):
        print("Matriks segitiga atas.")
    else:
        print("Bukan matriks segitiga atas")