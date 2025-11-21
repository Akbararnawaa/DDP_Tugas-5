# 1. Buat program yang menampilkan angka 1 sampai 10 menggunakan 
# for i in range(1, 11):
#     print(i) 

# 2. Buat program yang menampilkan hitung mundur dari 10 ke 1 menggunakan for loop
# for i in range(10, 0, -1):
#     print(i)

# 3. Buat program yang meminta input password dari pengguna, 
#   dan akan terus meminta sampai password benar ("python123"). Gunakan while.
# password = ""
# while password != "python123":
#     password = input("Masukkan password: ")
# print("Password benar!")

# 4. Buat program yang meminta user memasukkan 5 nama teman, lalu tampilkan seluruh nama yang sudah dimasukkan.
teman = []
for i in range(5):
    nama = input("Masukkan nama teman ke-{}: ".format(i+1))
    teman.append(nama)
print("Nama-nama teman yang dimasukkan:")
for nama in teman:
    print(nama)



