inventory = ["pedang", "tameng", "roti"]
perintah = input("Isi Perintah:").split()

match perintah:
    case ["ambil", item]:
        inventory.append(item)
        print(f"kamu mengambil {item}")
    case ["buang", item]:
        inventory.remove(item)
        print(f"kamu membuang {item}")
    case ["lihat"]:
        print(f"inventory kamu: {inventory}")
print(f"inventory akhir: {inventory}")
