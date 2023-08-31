while True:
    injam = input("Masukan jam : ")
    inmenit = input("Masukan menit : ")
    indetik = input("Masukan detik : ")
    if(any(inputs.isdigit() == False for inputs in [injam,inmenit,indetik])):
        print("Invalid input, input must be natural number")
        continue
    else:
        jam = int(injam)
        menit = int(inmenit)
        detik = int(indetik)
        if not (0 <= jam <= 23) and (0 <= menit <= 59) and (0 <= detik <= 59):
            print("Invalid input")
            continue

    
    detik = detik + 60*menit + 3600*jam + 1
    jambaru = detik // 3600
    detik -= jambaru*3600
    menitbaru = detik // 60
    detik -= menitbaru*60
    print(f"Detik selanjutnya adalah {jambaru}:{menitbaru}:{detik} (jam:menit:detik)")