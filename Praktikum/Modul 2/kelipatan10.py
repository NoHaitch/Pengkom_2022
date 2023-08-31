"""
Program : Kelipatan 10 Terkecil
Spesifikasi : mencari kelipatan 10 terkecil yang lebih besar dari input
Asumsi : input pasti bilangan bulat tak negatif

Kamus :
    x, hasil : int
"""

#ALGORITMA

# Menerima bilangan x
x = int(input("\nMasukan bilangan : "))

# Mencari kelipatan 10 terkecil yang dimulai dengan nilai terendah 10
hasil = 10

# Mengecek jika hasil lebih kecil sama dengan x, jika iya maka akan mengkalikan hasil dengan 10 
while (hasil <= x) :
    hasil *= 10
# hasil lebih besar dari x sehingga loop selesai dan didapatkan bilangan yang diinginkan 

print(f"Kelipatan 10 terkecil : {hasil}")