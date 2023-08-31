from math import sqrt


while True:
    # Program: Menghitung Akar N
    # menghitung nilai akar tanpa prosedur sqrt()
    """
    KAMUS :
        n,res : int
    ASUMSI : 
        input pasti bilangan bulat positif
    """
    # ALGORITMA

    while True:
        n = int(input("Masukan nilai N: "))
        if(n > 0):
            break
        else:
            print("N harus bilangan bulat positif")

    # Mencari nilai bilangan bulat terbesar yang dekat atau sama dengan N
    res = 0
    terbesar = 0
    for num in range(1,+n+1):
        if(num**2 <= n):
            terbesar = num
    res = terbesar
    if(res**2 == n):
        print(f"Akar dari N adalah: {res}")
    else:
        # Mencari decimalnya karena tidak pas
        for _ in range(10): # 10 sebagai jumlah decimal  ( underscore '_' karena variabelnya tidak diperlukan)
            n -= terbesar**2 # n menjadi sisanya yang semakin kecil tiap loop
            n *= 10 # kita kali 10 agar menjadi bilangan bulat contoh sisa 1 maka n = 10 agar looping dapat terjadi sebab for loop tidak bisa decimal  
            terbesar = 0
            print(n)
            for num in range(n):
                if(num**2 <= n):
                    terbesar = num
            print(terbesar)
            if(isinstance(res, int)): # jika angka masih bilangan bulat maka tambahkan koma dulu
                res = float(str(res)+"."+str(terbesar))
            else:
                res = float(str(res)+str(terbesar))
            print(f"saat ini n : {res} dengan terbesar {terbesar}")
    print(sqrt(n))
        #### GAGALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
        