# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 19 Oktober 2022
# Deskripsi : bermain dengan lampu yg sejajar(keadaan awal semua mati), jika menekan suatu tombol maka lampu dikiri dan kanan akan berubah kondisi(mati atau nyala), jika mati->menyala, jika nyala->mati, mati bernilai(0) dan nyala bernilai(1)

"""
    Asumsi : 
        input int pasti bilangan bulat positif
    KAMUS :
        n, i, ntekan, ditekan : int
        lampu : array int 
"""
#Algoritma
# meminta banyak lampu
n = int(input("Masukkan banyak lampu: "))
# inisialisasi array lampu dengan keadaan awal mati == 0
lampu = [0 for _ in range(n)]
# meminta jumlah input tekan tombol
ntekan  = int(input("Masukkan berapa kali Tuan Kil menekan tombol: "))
# pengulangan setiap ditekannya tombol
for i in range(ntekan):
    ditekan = int(input(f"Tombol yang ditekan ke {i+1}: "))
    # validasi input ditekan
    while ditekan <= 0 :
        print(f"Lampu dimulai dari 1 hingga {n}")
        ditekan = int(input(f"Tombol yang ditekan ke {i+1}: "))

    # merubah kondisi lampu sendiri
    if(lampu[ditekan-1] == 0):
        lampu[ditekan-1] = 1
    else:
        lampu[ditekan-1] = 0
    # merubah kondisi lampu kiri kecuali ditekan yang paling kiri
    if(ditekan != 1):
        if(lampu[ditekan-2] == 0):
            lampu[ditekan-2] = 1
        else: 
            lampu[ditekan-2] = 0
    # merubah kondisi lampu kanan kecuali ditekan yang paling kanan
    if(ditekan != n):
        if(lampu[ditekan] == 0):
            lampu[ditekan] = 1
        else:
            lampu[ditekan] = 0
# output
print("Keadaan akhir rangkaian lampu adalah ",end="")
for i in lampu:
    print(i,end="")    
print(".")
