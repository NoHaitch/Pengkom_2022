# NIM/Nama  : 19622078/Raden Francisco Trianto Bratadingrat
# Tanggal   : 18 Oktober 2022
# Deskripsi : Membeli produk dengan diskon paling besar, N buah barang dan N diskon, jika 2 diskon yang sama maka keluarkan yang indeks terkecil

"""
    Asumsi : 
        input int pasti bilangan bulat positif
    KAMUS :
        n, i, nilai : int
        barang, nilai_diskon, terbesar : array int
"""
#ALGORITMA
# meminta jumlah barang sebagai n
n = int(input("Masukkan banyak barang: "))
# inisialisasi barang yang berisi 2 array, array-1 adalah harga awal, array-2 adalah persen diskon
barang = [[0 for _ in range(n)],[0 for _ in range(n)]]
# meminta input harga awal dan persen diskon
for i in range(n):
    barang[0][i] = int(input(f"Masukkan harga awal barang ke-{i+1}: "))
for i in range(n):
    barang[1][i] = int(input(f"Masukkan besar diskon (dalam persen) barang ke-{i+1}: "))
# membuat array nilai_diskon yang berisi semua nilai_diskon dari perkalian harga awal dan persentase diskon/100
nilai_diskon = [(barang[0][i] * barang[1][i]/100) for i in range(n)]
# insialisasi array terbesar, dengan i-0 sebagai nilai diskon terbesar dan i-1 sebagai i barang ditemukannya nilai terbesar tersebut (-1 karena harga tidak mungkin negatif)
terbesar = [-1,0]
# mengecek semua nilai_diskon dan jika ditemukan yang lebih besar maka terbesar = [nilai_terbesar,indexnya]
for i in range(len(nilai_diskon)):
    if(nilai_diskon[i] > terbesar[0]):
        terbesar[0] = nilai_diskon[i]
        terbesar[1] = i
# output hasilnya
print(f"Barang {terbesar[1]+1} memiliki diskon paling besar yaitu {terbesar[0]:.0f}.")