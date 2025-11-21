inventori = ["pedang", " tameng", "roti"]
perintah =input("isi perintah:").split()

match perintah:
    case["ambil", item]:
        inventori.append(item)
        print(f"kamu mengambil {item}")
    case["buang", item]:
        inventori.remove(item)
        print(f"kamu membuang {item}")
    case["lihat"]:
        print(f"inventori kamu: {inventori}")

