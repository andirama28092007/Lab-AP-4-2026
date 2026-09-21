# Nomor 4
tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan waktu (Pagi/Malam): ")
tipe_penunjung = input("Masukkan tipe penunjung (Anak/Dewasa): ")

match tujuan:
    case "Pantai":
        if waktu == "Pagi" and tipe_penunjung == "Anak" or tipe_penunjung == "Dewasa":
            print("Paket A")
        elif waktu == "Malam" and tipe_penunjung == "Dewasa":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Pegunungan":
        if waktu == "Pagi" and tipe_penunjung == "Dewasa":
            print("Paket B")
        elif waktu == "Malam" and tipe_penunjung == "Dewasa":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Kota":
        if waktu == "Malam" and tipe_penunjung == "Anak" or tipe_penunjung == "Dewasa":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")