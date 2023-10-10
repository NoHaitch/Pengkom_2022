while True:

    # Program Menghitung Luas di bawah kurva
    # menghitung luas di bawah kurva dengan rumus trapesium
    """
    KAMUS :
        a, b, n : float
        delta : float
        luas : float
    ASUMSI : 
        a < b 
        a >= 0 
        b > 0 
        delta > 0
    """
    # ALGORITMA
    while True:
        a = float(input("Masukan a : "))
        b = float(input("Masukan b : "))
        delta = float(input("Masukan delta : "))
        if(delta <= b-a):
            break
        else:
            print("Delta tidak boleh lebih besar dari jarak b-a")
    luas = 0
    n = a
    while n < b:
        # f(x) = x^3 + x + 1
        # rumus trapesium = (f(panjang1) + f(panjang2)) * tinggi/2  
        # panjang1 = n, panjang2 = n+delta, tinggi = delta
        if(n+delta < b):
            luas += ((n**3+n+1) + ((n+delta)**3)+(n+delta)+1) * delta/2
        else: # percabangan agar luas pasti dibatasi oleh b
            luas += ((n**3+n+1) + ((b)**3)+(b)+1) * (b-n)/2
        n += delta
    print(f"Luas kurva dari x = {a} hingga {b} adalah {luas}")