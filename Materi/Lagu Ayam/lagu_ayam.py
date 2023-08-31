while True:

    # Program Lagu Anak Ayam
    # menyanyikan lagu anak ayam n mati satu tinggal n-1
    """
    KAMUS :
        ayam, hidup : int
    ASUMSI :
        input bilangan bulat
    """
    # ALGORITMA
    while True:
        ayam = int(input("Masukan jumlah ayam : "))
        if(ayam > 0):
            break
        else:
            print("Jumlah anak ayam harus lebih besar dari 0")
    print(f"Anak ayam turunlah {ayam}")
    
    hidup = ayam-1
    while hidup != 0 :
        print(f"Mati satu tinggallah {hidup}")
        hidup -= 1

    print("Mati satu tinggal induknya")
    
    for hidup in range(ayam)[::-1]:
        if(hidup != 0):
            print(f"Mati satu tinggallah {hidup}")
        else:
            print("Mati satu tinggal induknya")
    