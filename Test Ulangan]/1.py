nama_kendaraan = input("Masukan Nama Kendaraan (mobil/motor): ")
jenis_bensin = input("Masukan Jenis Bensin (Pertalite/Pertamax/Pertamax Turbo): ").lower()
kota_tujuan = input("Masukan Kota yang dituju (Jakarta/Bekasi/Depok/Tangerang/Bogor): ").lower()
if jenis_bensin == "pertalite":
    harga_perliter = 10000
    jarak_tempuh = 12 
elif jenis_bensin == "pertamax":
    harga_perliter = 14000
    jarak_tempuh = 13
elif jenis_bensin == "pertamax turbo":
    harga_perliter = 17000
    jarak_tempuh = 13.5
else:
    print("Jenis bensin tidak tersedia.")
    exit()
if kota_tujuan == "jakarta":
    jarak_kota = 20
elif kota_tujuan == "bekasi":
    jarak_kota = 35.7
elif kota_tujuan == "depok":
    jarak_kota = 5
elif kota_tujuan == "tangerang":
    jarak_kota = 99
elif kota_tujuan == "bogor":
    jarak_kota = 120.6
# else:
#     print("Kota tidak tersedia.")
#     exit()
pemakaian_bensin = jarak_kota / jarak_tempuh
total_harga = pemakaian_bensin * harga_perliter
print("--- Rincian Perjalanan ---")
print("Nama Kendaraan: {}".format(nama_kendaraan))
print("Jenis Bensin: {}".format(jenis_bensin.title()))
print("Kota yang dituju: {} ".format(kota_tujuan.title()))
print("Pemakaian Bensin (liter): {:.2f}".format(pemakaian_bensin))
print("Total Harga dari Bensin: Rp. {:.2f}".format(total_harga))




