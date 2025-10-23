#Soal 1

# kendaraan = ["nama kendaraan", "jenis kendaraan", "cc kendaraan", "warna kendaraan", "roda kendaraan"]

# kendaraan.extend(["harga kendaraan", "tipe kendaraan"])
# # extend sama insert sama tapi extend lebih cepat, kalau insert bisa atur posisi
# kendaraan.insert(2, "merk kendaraan")

# print(kendaraan)

#Soal 2

# print("program menghitung luas bangun datar")
# print("1. Persegi")
# print("2. Lingkaran")
# print("3. Segitiga")

# hitung = int(input("memilih bangun datar yang akan dihitung (1/2/3): "))

# match hitung:
#     case 1:
#         sisi = float(input("Masukkan panjang sisi persegi: "))
#         luas = sisi * sisi
#         print("Luas Persegi adalah:", luas)
#     case 2:
#         radius = float(input("Masukkan jari-jari lingkaran: "))
#         luas = 3.14 * radius * radius
#         print("Luas Lingkaran adalah:", luas)
#     case 3:
#         alas = float(input("Masukkan panjang alas segitiga: "))
#         tinggi = float(input("Masukkan tinggi segitiga: "))
#         luas = 0.5 * alas * tinggi
#         print("Luas Segitiga adalah:", luas)
#     case _:
#         print("Pilihan tidak valid")