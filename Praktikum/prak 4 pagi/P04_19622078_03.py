# Deskripsi : Permainan catur, apakah pion raja putih ama dari serangan kuda hitam
"""
KAMUS:
    M : matrix of string
    i, j, m : int
    aman : bool
"""
#ALGORTIMA
# minta semua input
m = int(input("Masukkan nilai m: "))
M = [["." for _ in range(m)] for _ in range(m)]
for i in range(m):
    for j in range(m):
        M[i][j] = input(f"Masukkan elemen matriks ke-{i+1} {j+1}: ")
print("Hasil papa catur")
for i in M:
    for j in i:
        print(j,end=" ")
    print()
aman = True
for i in range(m):
    if(aman == False):
            continue
    for j in range(m):
        if(aman == False):
            continue
        if(M[i][j] == "K"):
            if(j-2 >= 0):
                if(i-2 >= 0):
                    if(M[i-1][j-2] == "R" or M[i-2][j-1] == "R"):
                        aman = False
                        continue
                elif(i-1 >= 0):
                    if(M[i-2][j-1] == "R"):
                        aman = False
                        continue
                if(i+2 <= m-1):
                    if(M[i+1][j-2] == "R" or M[i+2][j-1] == "R"):
                        aman = False
                        continue
                elif(i+1 <= m-1):
                    if(M[i+1][j-2] == "R"):
                        aman = False
                        continue
            elif(j-1 >= 0):
                if(i-2 >= 0):
                    if( M[i-2][j-1] == "R"):
                        aman = False
                        continue
                if(i+2 <= m-1):
                    if(M[i+2][j-1] == "R"):
                        aman = False
                        continue
            if(j+2 <= m-1):
                if(i-2 >= 0):
                    if(M[i-1][j+2] == "R" or M[i-2][j+1] == "R"):
                        aman = False
                        continue
                elif(i-1 >= 0):
                    if(M[i-1][j+2] == "R"):
                        aman = False
                        continue
                if(i+2 <= m-1):
                    if(M[i+1][j+2] == "R" or M[i+2][j+1] == "R"):
                        aman = False
                        continue
                elif(i+1 <= m-1):
                    if(M[i+1][j+2] == "R"):
                        aman = False
                        continue
            elif(j+1 <= m-1):
                if(i-2 >= 0):
                    if( M[i-2][j+1] == "R"):
                        aman = False
                        continue
                if(i+2 <= m-1):
                    if(M[i+2][j+1] == "R"):
                        aman = False
                        continue
if(aman):
    print("Raja aman dari serangan kuda.")
else:
    print("Raja tidak aman dari serangan kuda.")