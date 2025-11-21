#Akbar Arnawa Adinata

usia = int(input("Usia : "))
if usia <= 1 and usia == 3:
    print("Balita")
elif usia <= 0:
    print("Umur Tidak Valid")
elif usia >= 4 and usia <= 12:
    print("Anak Anak")
elif usia >= 13 and usia <= 17:
    print("Remaja")
elif usia >= 18 and usia <= 60:
    print("Dewasa")
else:
    print("Lansia")