# Deskripsi : Mencari apakah A dan B yang bergantian dikali akan bisa mencapai nilai N

"""
ASUMSI:
    a, b bilangan bulat positif relatif prima
"""

a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
n = int(input("Masukkan bilangan N: "))
bilskrg = 1
ganjil = True
while (bilskrg * a <= n) or (bilskrg*b <= n):
    if(ganjil == True):
        ganjil = False
        bilskrg = bilskrg * a
    else:
        ganjil = True
        bilskrg = bilskrg * b
if(bilskrg == n):
    print(f"bilangan {n} bisa didapat dari {a} dan {b}")
else:
    bilskrg = 1
    ganjil = False
    while (bilskrg * a <= n) or (bilskrg*b <= n):
        if(ganjil == True):
            ganjil = False
            bilskrg = bilskrg * a
        else:
            ganjil = True
            bilskrg = bilskrg * b
    if(bilskrg == n):
        print(f"bilangan {n} bisa didapat dari {a} dan {b}")
    else:
        print(f"bilangan {n} tidak bisa didapat dari {a} dan {b}")