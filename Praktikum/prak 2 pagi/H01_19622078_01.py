# Deskripsi : Menghitung banyak pantulan bola bertipe2 atau lebih

"""
    Asumsi : 
        input pasti bilangan bulat positif > 0
    KAMUS :
        tinggi, tipe, count : int
        tinggiskrg : float
"""
#ALGORITMA

tinggi = int(input("Masukkan ketiggian awal bola: "))
tipe = int(input("Masukkan tipe bola: "))
tinggiskrg = tinggi
count = 0
while tinggiskrg/tipe > 1:
    tinggiskrg = tinggiskrg/tipe
    count = count + 1
print(f"Bola akan memantul sebanyak {count} kali")
