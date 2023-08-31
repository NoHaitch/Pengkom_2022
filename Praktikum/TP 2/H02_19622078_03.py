# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 4 Oktober 2022
# Deskripsi : faktor prima terkecil hingga terbesar

"""
    Asumsi : 
        input pasti bilangan bulat positif
    KAMUS :
        n, x, i, numpertama : int
        countfaktor : int
"""

# Meminta input n yang valid
while True:
    n = int(input("Masukkan bilangan: "))
    if(n <2):
        print("n harus lebih besar dari 6")
    else:
        break
# Numpertama digunakan untuk format ouput agar persis seperti contoh
numpertama = True
print("Faktor primanya adalah ",end="")
# loop i sebagai semua angka dari 1 hingga n+1
for i in range(1,n+1):
    # jika benar maka n adalah faktor
    if(n % i == 0 and i != 1):
        # karena ciri-ciri faktor prima adalah faktornya ada 2, maka kita hitung faktor dari faktor milik n
        countfaktor = 0
        for x in range(1,i+1):
            if(i % x == 0):
                countfaktor += 1
        if(countfaktor == 2):
            # maka i adalah faktor prima
            if(numpertama == True):
                print(i,end="")
                numpertama = False
            else:
                print(f", {i}",end="")
print(".")