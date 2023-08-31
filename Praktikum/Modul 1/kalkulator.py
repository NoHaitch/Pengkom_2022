"""
Program : Kalkulator Sederhana
Spesifikasi : kalkulator sederhana yang hanya menerima 2 angka dan sebuah operasi perhitungan
Asumsi : 
    input integer pasti bilangan bulat
    operasi pasti string antara +, -, *, / dan %

Kamus :
    num1, num2 : int
    operasi : string
"""

# ALGORITMA

# Meminta input angka pertama sebagai num1, angka kedua sebagai num2, dan operasi hitung sebagai operasi
num1 = int(input("\nMasukan angka pertama : "))
num2 = int(input("Masukan angka kedua : "))
operasi = input("Masukan operator (+,-,*,/,%) : ")

# Melakukan operasi sesuai dengan operasi yang mungkin
if(operasi == "+"):
    print(f"Hasil = {num1 + num2}")
elif(operasi == "-"):
    print(f"Hasil = {num1 - num2}")
elif(operasi == "*"):
    print(f"Hasil = {num1 * num2}")
elif(operasi == "/"):
    print(f"Hasil = {num1 / num2}")
elif(operasi == "*"):
    print(f"Hasil = {num1 % num2}")    