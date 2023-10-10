while True:
    injam = input("Masukan jam : ")
    inmenit = input("Masukan menit : ")
    indetik = input("Masukan detik : ")
    if(any(inputs.isdigit() == False for inputs in [injam,inmenit,indetik])):
        print("Invalid input")
        continue
    else:
        jam = int(injam)
        menit = int(inmenit)
        detik = int(indetik)
        if not (0 <= jam <= 23) and (0 <= menit <= 59) and (0 <= detik <= 59):
            print("Invalid input")
            continue
    detik += 1
    if(detik // 60 == 1):
        detik -= 60
        menit += 1 
    if(menit // 60 == 1):
        menit -= 60
        jam += 1

    print(f"Detik selanjutnya adalah {jam}:{menit}:{detik} (jam:menit:detik)")

