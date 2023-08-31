"""
Program : Segitiga Angka
Spesifikasi : membuat segitiga dari angka dengan panjang alas n
Asumsi : input pasti bilangan bulat positif

Kamus :
    n : int
"""

# Menerima bilangan n sebagai alas segitiga
n = int(input("Masukan N: "))

# Membuat pengulangan yang diulang n kali dan i sebagai representasi baris/tinggi yang dimulai dari baris ke-1 hingga n
for i in range(1,n+1):
    # Membuat pengulangan yang diulang i kali (baris ke-1 maka i = 1), yang berulang mencetak angka dimulai dari angka 1 dengan spasi(" ") sebagai pemisah 
    for x in range(1,i+1):
        print(f"{x} ",end="")
    print()