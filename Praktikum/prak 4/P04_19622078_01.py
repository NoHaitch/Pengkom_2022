# NIM/Nama  : 19622078 / Raden Francisco Trianto Bratadiningrat
# Tanggal   : 9 November 2022
# Deskripsi : Memilih K mahasiswa sebagai perwakilan dari N mahasiswa dengan 
#             rumus C(n,k) = n!/(n-k)!k!
"""
KAMUS:
    faktorial(n) : function
    n, k, c : int
"""
# ALGORTIMA

# inisialisasi fungsi faktorial(n) untuk mencari nilai faktorial dari n
def faktorial(n):
    hasil = 1
    for i in range(1,n+1):
        hasil = hasil * i
    return hasil

# minta semua input, asumsi k < n dan n,k > 0
n = int(input("Masukkan N: "))
k = int(input("Masukkan K: "))
# menghitung c = cara memilih mahasiswa
c = int(faktorial(n)/(faktorial(n-k)*faktorial(k)))
# output 
print(f"Tuan Riz memiliki {c} cara untuk memilih mahasiswa.")
