# Buat program untuk minta input jumlah baris dan buat
# rangkaian berikut ini
# *
# **
# ***
# ****
# Dan seterusnya sejumlah baris yang diinputkan
# Gunakan for loop dengan range

baris = int(input("Masukkan jumlah baris: "))
for i in range(1, baris + 1):
    for j in range(i):
        print("*", end="")
    print()  # Pindah ke baris berikutnya setelah mencetak satu baris bintang
print("Loop finished.")




