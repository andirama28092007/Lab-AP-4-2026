def tambah_buku(inventaris, judul, penulis, harga, stok):
    inventaris.append({
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    })
    print(f"Buku *{judul}* berhasil di tambahkan")

def cari_buku(inventaris, kata_kunci):
    hasil_cari = [buku for buku in inventaris if kata_kunci.lower() in buku['judul'].lower()]
    if hasil_cari:
        print(f"ditemukan {len(hasil_cari)} buku:")
        for i, buku in enumerate(hasil_cari, 1):
            print(f"{i}. {buku['judul']} | {buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")
    else:
        print("Buku tidak di temukan.")
        print("=================")

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku['judul'].lower() == judul.lower():
            if buku['stok'] + jumlah < 0:
                print("Gagal: Stok tidak boleh menjadi negatif!\n")
                return
            buku['stok'] += jumlah
            status = "berkurang " if jumlah < 0 else "bertambah "
            print(f"stok '{buku['judul']}' {status}{abs(jumlah)}. Stok sekarang: {buku['stok']}\n")
            return
    print("Error: Buku tidak ditemukan!!!\n")

def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = sum(buku['stok'] for buku in inventaris)
    total_aset = sum(buku['harga']*buku['stok'] for buku in inventaris)
    print("===*RINGKASAN INVENTARIS BOOKNEST*===")
    print(f"jumlah jenis buku: {jumlah_jenis}")
    print(f"total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset}")
    if inventaris:
        buku_termahal = max(inventaris, key=lambda x: x['harga'])
        print(f"Buku termahal: {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print("=====================================\n")

inventaris = []
while True:
    try:
        print("Menu:\n1. Tambah Buku\n2. Cari Buku\n3. Update Stok\n4. Ringkasan Inventaris\n5. Keluar")
        pilihan = int(input("Pilih menu (1-5): "))
        if pilihan == 1:
            judul = input("Judul buku: ")
            penulis = input("Penulis: ")
            try:
                harga = int(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Harga dan stok tidak boleh negatif!\n")
                else:
                    tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Error: Harga dan stok harus berupa angka!\n")
        elif pilihan == 2:
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kata_kunci)
        elif pilihan == 3:
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
                update_stok(inventaris, judul, jumlah)
            except ValueError:
                print("Error: Jumlah perubahan harus berupa angka!\n")
        elif pilihan == 4:
            ringkasan_inventaris(inventaris)
        elif pilihan == 5:
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")
    except:
        print("eit input hanya boleh dari angka 1 sampai 5")
