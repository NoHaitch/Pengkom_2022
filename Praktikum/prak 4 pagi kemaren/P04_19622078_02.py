# Deskripsi : Mengisi Matriks secara zig zag
"""
KAMUS:
    komposit() : function
    a, b, i, j : int
"""
#ALGORTIMA
# inisialisi komposit(num) yang mengecek apakah suatu angka komposit atau tidak
def komposit(num):
    faktor = 0
    for i in range(1,num+1):
        if(num % i == 0):
            faktor = faktor + 1
        if(faktor > 2):
            return True
    return False
# meminta input selang [a,b]
a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))
print("Pasangan bilangan komposit")
# mencari pasangan komposit pada selang [a,b]
for i in range(a,b+1):
    if(komposit(i)):
        for j in range(i+1,b+1): # mulai dari i+1 karena pasangan tidak boleh bernilai sama
            if(komposit(j) and komposit(j+i)):
                print(i,j,sep=" ")