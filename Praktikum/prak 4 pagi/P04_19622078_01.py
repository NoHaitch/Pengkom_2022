# Deskripsi : Memilih K mahasiswa sebagai perwakilan dari N mahasiswa
"""
KAMUS:
    faktorial(n) : function
    n, k, c : int
"""
#ALGORTIMA
# inisialisasi fungsi faktorial(n) untuk mencari nilai faktorial dari n
def faktorial(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    return sum
# minta semua input
n = int(input("Masukkan N: "))
k = int(input("Masukkan K: "))
# menghitung kombinasi --> cara memilih mahasiswa
c = int(faktorial(n)/(faktorial(n-k)*faktorial(k)))
print(f"Tuan Riz memiliki {c} cara untuk memilih mahasiswa.")
