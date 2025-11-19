print("PENJUMLAHAN")
angka_pertama = int(input("masukkan nilai pertama: "))
angka_kedua= int(input("masukkan nilai kedua: "))

hasil = angka_pertama + angka_kedua

print("Hasilnya adalah: ", hasil)

if hasil %2 == 0:
    print(hasil, "adalah bilangan genap")
else:
    print(hasil, "adalah bilangan ganjil")
    
print()
print("HURUF VOKAL")

huruf = input("masukkan huruf: ")

if huruf.lower() in ("a", "i", "u", "e", "o"):
    print(huruf, "adalah huruf vokal")
else:
    print(huruf, "adalah huruf non vokal")
    
    
    
    
    