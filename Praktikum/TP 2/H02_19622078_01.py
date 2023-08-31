# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 4 Oktober 2022
# Deskripsi : Bilangan sempurna

"""
    Asumsi : 
        input pasti bilangan bulat positif
    KAMUS :
        n, i : int
        sumfaktor : int
"""

# Meminta input
n = int(input("Masukkan bilangan: "))
# untuk menyimpan jumlah faktor
sumfaktor = 0
# loop dengan i dari 1 hingga n+1
for i in range(1,n+1):
    # jika faktor dan bukan sama dengan nilai n maka sumfaktor ditambah i
    if(n % i == 0 and n != i):
        sumfaktor += i
# Syarat dari bilangan sempurna
if(sumfaktor == n):
    print("Bilangan tersebut adalah bilangan sempurna")
else:
    print("Bilangan tersebut bukan bilangan sempurna")