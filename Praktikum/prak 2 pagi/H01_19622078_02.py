# Deskripsi: kompetisi A dan B yang diikuti oleh klub pengkom

# ALGORITMA

n = int(input("Masukkan banyak pertandingan: "))
count = 0
gugurB = False
for pertandingan in range(1,n+1):
    hasil = input(f"Masukkan hasil pertandingan ke-{pertandingan}: ")
    if(pertandingan % 2 == 0 and gugurB == False):
        if(hasil == "L"):
            gugurB = True
    else:
        if(hasil == "W"): 
            count = count + 3
        elif(hasil == "D"):
            count = count + 1
print(f"Poin Klub Pengkom saat ini adalah {count}.")