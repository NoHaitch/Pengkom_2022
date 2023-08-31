# Program SisiMiringSegitiga;
# Isi menghitung panjang sisi miring segitiga siku-siku dari 2 bilangan ril alas dan tingginya
"""
Kamus :    
    a, b : float 
"""
# ALGORITMA
a = float(input("Masukkan alas segitiga: "))
b = float(input("Masukkan tinggi segitiga: "))
print(f"Panjang sisi miring segitiga adalah {(a**2 + b**2)**0.5}.")