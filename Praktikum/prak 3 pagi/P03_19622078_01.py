n = int(input("Masukkan nilai banyak data: "))
data = [0 for _ in range(n)]
for i in range(n):
    data[i] = int(input(f"Masukkan data ke-{i+1}: "))
nilai = int(input("Masukkan nilai yang dicari: "))
Nnilai = int(input("Masukkan nilai N: "))
Nskrg = 0
for i in range(n):
    if(data[i] == nilai):
        Nskrg = Nskrg + 1
    if(Nnilai == Nskrg):
        indeks = i
        continue
print(f"Nilai {nilai} ke-{Nnilai} berada pada indeks {indeks}.")