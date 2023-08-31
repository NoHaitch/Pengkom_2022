# NIM/Nama  : 19622078 / Raden Francisco Trianto Bratadiningrat
# Tanggal   : 9 November 2022
# Deskripsi : Mencari pasangan komposit (a,b dan a+b -> bil bukan prima) dari selang [a,b]
"""
KAMUS:
    komposit(n) : function
    a, b, i, j : int
"""
# ALGORTIMA

# inisialisi komposit(n) yang mengecek apakah suatu angka komposit atau tidak
def komposit(n): # return True jika komposit, False jika bukan komposit
    faktor = 0
    # mencari semua faktor dari angka n
    for i in range(1,n+1):
        if(n % i == 0):
            faktor = faktor + 1
        # jika faktor lebih dari 2 maka bilangan tersebut adalah bil komposit
        if(faktor > 2):
            return True
    # karena faktor <= 2 maka bilangan adalah bil prima yang bukan komposit
    return False

# meminta input, asumsi a < b dan a,b > 0
a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))

print("Pasangan bilangan komposit")
# mencari pasangan komposit pada selang [a,b]
for i in range(a,b+1):
    if(komposit(i)): 
        # jika i komposit
        for j in range(i+1,b+1): # mulai dari i+1 karena pasangan tidak boleh bernilai sama
            if(komposit(j) and komposit(j+i)):
                # jika j komposit dan i+j juga komposit
                # maka ditemukan pasangan komposit i dan j -> output
                print(i,j,sep=" ")