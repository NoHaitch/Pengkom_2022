"""
Program : Anagram
Spesifikasi : Mengecek apakah array A anagram dari B. Anagram jika semua elemen A dapat ditukar2 sehingga menghasilkan array B
Asumsi : input pasti bilangan bulat positif, na == nb

Kamus :
    a,b : array int
    na,nb : int
    x : int
"""

# ALGORITMA

# meminta semua input
na = int(input("Masukkan banyaknya elemen A: "))
a = []
for x in range(na):
    a.append(int(input(f"Masukkan elemen A ke-{x+1}: ")))
nb = int(input("Masukkan banyaknya elemen B: "))
b = []
for x in range(nb):
    b.append(int(input(f"Masukkan elemen A ke-{x+1}: ")))

# mensortir array a dan b sehingga urutan angka pasti sama jika isinya sama
a.sort()
b.sort()

# jika semua nilai index x di A sama dengan index x di b
if(all(a[x] == b[x] for x in range(na))):
    print("B adalah anagram dari A")
else:
    print("B bukan anagram dari A")