print("--- Reakpitulasi Transaksi DIns Store")
print("Ketik '0' untuk menutup toko dan mengakiri sesi.")

while True:
    try: 
        item = int(input("Masukkan jumlah item: "))
        if item == 0:
            break
        elif item < 0:
            print("Jumlah tidak boleh negatif")
            print()
        elif item > 0 and item <= 100:
            print(f"Transaksi {item} item berhasil!")
            print()
        elif item > 100:
            print("Maksimal 100 per transakasi!")
            print()
    except:
        print("Input harus berupa angka!/n")
        print()
print("Toko ditutup, Sesi rekap selesai.")