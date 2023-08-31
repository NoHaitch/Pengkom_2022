
N=int(input("Masukkan N: "))
w=("Faktor primanya adalah ")
for i in range(1,N):
    if N%i == 0:
        if i == 1:
            continue
        if i == 2:
            w += (str(i)+', ')
        else:
            for y in range(2,i): # loop buat apa kalo langsung ke break saat satu kali pengecekan jadi cuman ngecek sekali aja  i % 2 == 0
                if (i%y)==0:
                    break # nih
                else:
                    w += (str(i)+', ')
                    break # nih
    else: 
        continue
print(w)