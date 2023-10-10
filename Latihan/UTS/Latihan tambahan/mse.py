# Program : Mean Squared Error(MSE)
# Deskripsi: Menentukan nilai MSE dari data yang diberikan
"""
Kamus:
    n, i : int
    t0, t1 : array int
"""

# ALGORTIMA
n = int(input("Masukkan banyak data: "))
if(n <= 0 ):
    print("Tidak ada data yang tersedia.")
else:
    t0 = [0.0 for _ in range(n)]
    t1 = [0.0 for _ in range(n)]
    for i in range(n):
        t0[i] = float(input(f"Masukkan data teramati ke-{i+1}: "))
    for i in range(n):
        t1[i] = float(input(f"Masukkan data estimasi model ke-{i+1}: "))
    mse = 0
    for i in range(n):
        mse = mse + (t0[i] - t1[i])**2
    mse = mse / n
    print(f"Hasil MSE adalah {mse}.")
