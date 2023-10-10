x = int(input("Masukkan jumlah baris: "))
y = int(input("Masukkan jumlah kolom: "))
matriks = [[0 for _ in range(y)] for _ in range(x)]

for i in range(x):
    for j in range(y):
        matriks[i][j] = int(input(f"[{i}][{j}]: "))
for line in matriks:
    print(line)
if(i <= 2 and j <= 2):
    print("matriks tidak mungkin segitiga")
else:
    salah = False
    if(matriks[0][0] == 0):
        if(matriks[0][y-1] == 0):
            print(matriks[0][y-1])
            print(matriks[x-1][y-1])
            if(matriks[x-1][y-1] == 0):
                for i in range(x):
                    for j in range(y-i):
                        print(matriks[i][j])
                        if(matriks[i][j] != 0):
                            salah = True
                        
# cari ujung yang bernilai 0