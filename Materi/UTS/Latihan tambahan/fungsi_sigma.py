# Program : Fungsi f(x)
# Deskripsi: diketahui fungsi f(x) = sigma(n,i=1)[ax^i + b
"""
Asumsi:
    a, b , x --> bil real
    n --> bil bulat > 0
Kamus:
    a, b, x, sum : float
    n : int
"""

# ALGORTIMA
a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))
x = float(input("Masukkan x: "))
n = int(input("Masukkan n: "))
hasil = 0
for i in range(1,n+1):
    print(hasil,end="-")
    hasil = hasil + (a*((x)**i) + b)
print(hasil)
print(f"Hasil dari f({x}) adalah {hasil}.")