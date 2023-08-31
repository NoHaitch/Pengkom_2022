x = int(input("Masukkan X: "))
terkecil = None

pangkat = 1
while terkecil == None:
    for digit in range(1,10):
        num = ""
        for _ in range(pangkat):
            num += str(digit)
        num = int(num)
        #print(num) # untuk menjelaskan
        if(num % x == 0):
            terkecil = num
            break         
    pangkat += 1
print(f"Bilangan cantik terkecil yang habis dibagi {x} ialah {terkecil}")
