n = int(input("Masukkan banyak kota: "))
kota = [0 for _ in range(n)]
for i in range(n):
    kota[i] = int(input(f"Masukkan perubahan uang di kota {i+1}: "))
maks = None
awal = 0
akhir = 0
# loop semua elemen
for x in range(n):
    terbesar = kota[x]
    # cari maksimum dengan awal x
    terbesar = None
    for y in range(n):
        for z in range(n-y-1):
        if(terbesar == None):
            terbesar = kota[]
        kota[-y]
print(f"Tuan Kil dapat memiliki uang maksimum sebesar {maks} dengan berawal pada kota {awal} dan berkahir di kota {akhir}")