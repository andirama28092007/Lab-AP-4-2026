pendapatan = 0
while True:
    try:
        maksimal_kursi = int(input("Masukkan maksimal kursi: "))
        while maksimal_kursi < 0:
            print("Input tidak boleh kurang dari 1")
            maksimal_kursi = int(input("Masukkan maksimal kursi: "))
        while maksimal_kursi > 0:
            try: 
                print()
                print("--- Sistem Revervasi PO BUS Dimulai ---")
                print()
                print(f"Sisa kursi: {maksimal_kursi}")
                umur_penumpang = int(input("Masukkan umur penumpang: "))
                if 0 <= umur_penumpang <= 5:
                    ticket = 0
                    kategori = "Balita - Tiket Gratis (Rp 0)"
                elif 6 <= umur_penumpang <= 12:
                    ticket = 50000
                    kategori = "Anak - Harga: Rp 50.000"
                elif umur_penumpang > 12:
                    ticket = 100000
                    kategori = "Dewasa - Harga: Rp 100.000"
                else:
                    print("Umur tidak valid")
                    continue
                maksimal_kursi -= 1
                pendapatan += ticket
                print(f"Kategori: {kategori}")
            except:
                print("Input harus berupa angka!")
                print()
        print()
        print("--- Semua Kursi Terisi ---")
        print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {pendapatan}")
        break
    except:
        print("Input harus berupa angka!")