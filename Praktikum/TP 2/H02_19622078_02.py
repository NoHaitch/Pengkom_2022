# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 4 Oktober 2022
# Deskripsi : Jumlah bilangan yang lebih besar 

"""
    Asumsi : 
        input pasti bilangan bulat
    KAMUS :
        na, nb, i : int
        sum, count : int
"""

# meminta input pertama
na = int(input(f"Masukkan bilangan ke-1: "))
# meninisilaisasi sum sebagai jumlah, count sebagai hitungan gagal dan i untuk incremen
sum = 0
count = 0
i = 1

# jika gagal 3 kali maka berhenti
while count < 3:
        i += 1
        nb = int(input(f"Masukkan bilangan ke-{i}: "))
        # Syarat nilai sekarang lebih besar dari nilai awal
        if(nb > na):
            sum += nb
            count = 0
            # karena gagal harus berturut maka jika benar nilainya balik ke 0
        else:
            # gagal sehingga count ditambah 1
            count +=1
        na = nb
print(f"Jumlah nilai yang terbesar adalah {sum}")