# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 11 November 2022
# Deskripsi : mengubah semua elemen array menjadi 0 dengan langkah: 1. mencari nilai min tidak 0, 2. mengurangi semua nilai dengan min kecuali sudah 0, 3. diulangi hingga semua berisi 0

"""
    Asumsi : 
        input int awal bilangan bulat tak negatif
    KAMUS :
        n, i, min : int
        num : array int
"""
# insialisasi Fungsi
def minimum(array):
    # fungsi : mencari nilai minimum array
    # Kamus
    # min, i : int
    min = None
    for i in array:
        if(min == None):
            if(i != 0):
                min = i
        elif(i < min and i != 0):
            min = i
    return min

def array0(array):
    # fungsi : mengecek apakah semua elemen array bernilai 0, True jika semua 0
    # Kamus
    # i : int
    # array : array 2
    for i in array:
        if(i != 0):
            return False
    return True
    
# ALGORITMA
# meminta input banyak nilai
n = int(input("Masukkan banyak nilai: "))
# inisialisasi array num
num = [0 for _ in range(n)]
# meminta input array num
for i in range(n):
    num[i] = int(input(f"Masukkan nilai ke-{i+1}: "))
# pengulangan hingga semua elemen array bernilai 0
while array0(num) == False:
    # output array num
    for i in num:
        print(f"{i} ",end="")
    print()
    # mendapatkan nilai minimum
    min = minimum(num)
    # mengurangi semua elemen bukan 0 dengan minimum
    for i in range(n):
        if(num[i] != 0):
            num[i] = num[i] - min
# output akhir num yang semua elemennya bernilai 0
for i in num:
    print(f"{i} ",end="")
print()