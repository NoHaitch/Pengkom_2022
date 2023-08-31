while True:

    # Program Statistika suhu udara 1 bulan
    # mendapat data statistika dari N hari dengan N data suhu udara 
    """
    KAMUS :
        hari, n : int
        suhu : list (int)
        jumlah, tertinggi, terendah : int
    ASUMSI : 
        hari pasti antara {28,29,30,31}
        input suhu pasti bilangan
    """
    # ALGORITMA
    hari = int(input("Masukan jumlah hari : "))
    suhu = []
    jumlah,tertinggi, terendah = 0, 0, None
    for n in range(1,hari+1):
        suhu.append(float(input(f"Suhu hari ke-{n} : ")))
        jumlah += suhu[n-1]
        if(suhu[n-1] > tertinggi):
            tertinggi = suhu[n-1]
        if(terendah == None):
            terendah = suhu[n-1]
        elif(suhu[n-1] < terendah):
            terendah = suhu[n-1]
    print(f"Suhu Rata-Rata : {jumlah/hari}")
    print(f"Suhu Tertinggi : {tertinggi}")
    print(f"Suhu Terendah  : {terendah}")