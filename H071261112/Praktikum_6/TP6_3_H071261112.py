playlist = []
genre_set = set()

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    playlist.append((judul, artis, genre, durasi))
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan")

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist kosong.")
        return
    print(f"{'No':<3} {'Judul':<25} {'Artis':<20} {'Genre':<10} {'Durasi'}")
    total_detik = 0
    for i, lagu in enumerate(playlist, 1):
        judul, artis, genre, durasi = lagu
        menit = durasi // 60
        detik = durasi % 60
        print(f"{i:<3} {judul:<25} {artis:<20} {genre:<10} {menit}:{detik:02d}")
        total_detik += durasi
    total_menit = total_detik // 60
    sisa_detik = total_detik % 60
    print("=" * 68)
    print(f"Total durasi playlist: {total_menit} menit {sisa_detik} detik")

def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]

def hapus_lagu(playlist, nomor):
    if 1 <=nomor<= len(playlist):
        lagu_terhapus = playlist.pop(nomor -1)
        print(f"Lagu '{lagu_terhapus[0]}' berhasil dihapus!")
    else:
        print("Nomor lagu tak valid")

def statistik_playlist(playlist, genre_set):
    if not playlist:
        print("Playlist kosong, tidak ada statistik.")
        return
    print(f"Total lagu\t: {len(playlist)}")
    print(f"Jumlah Genre\t: {len(genre_set)}")
    print(f"Daftar Genre\t: {genre_set}")

    print("Distribusi genre")
    distribusi = {}
    for lagu in playlist:
        genre = lagu[2]
        distribusi[genre] = distribusi.get(genre, 0) + 1
    for genre, count in distribusi.items():
        print(f"{genre:<10}: {'#' * count} ({count})")
    terpanjang = max(playlist, key=lambda x: x[3])
    terpendek = min(playlist, key=lambda x: x[3])
    print(f"Lagu terpanjang: {terpanjang[0]} ({terpanjang[3]//60}:{terpanjang[3]%60:02d})")
    print(f"Lagu terpendek\t: {terpendek[0]} ({terpendek[3]//60}:{terpendek[3]%60:02d})")

while True:
    print("\n=== PLAYLIST MUSIK PLAYTUNE ===")
    print("Menu:")
    print("1. Tambah Lagu\n2. Tampilkan Playlist\n3. Filter berdasarkan Genre\n4. Hapus Lagu\n5. Statistik Playlist\n6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == '1':
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
        while True:
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Durasi harus angka positif.")
                    continue
                break
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
        tambah_lagu(playlist, genre_set, judul, artis, genre.capitalize(), durasi)
        
    elif pilihan == '2':
        tampilkan_playlist(playlist)
        
    elif pilihan == '3':
        print(f"Genre tersedia: {genre_set}")
        genre_target = input("Masukkan genre yang ingin difilter: ")
        hasil_filter = filter_genre(playlist, genre_target)
        
        print(f"Lagu bergenre '{genre_target}':")
        if hasil_filter:
            for i, lagu in enumerate(hasil_filter, 1):
                menit, detik = lagu[3] // 60, lagu[3] % 60
                print(f"{i}. {lagu[0]} - {lagu[1]} ({menit}:{detik:02d})")
        else:
            print("Tidak ada lagu dengan genre tersebut.")
            
    elif pilihan == '4':
        tampilkan_playlist(playlist)
        if playlist:
            try:
                nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)
            except ValueError:
                print("Input harus berupa angka.")
                
    elif pilihan == '5':
        print("\n=== STATISTIK PLAYLIST PLAYTUNE ===")
        statistik_playlist(playlist, genre_set)
        
    elif pilihan == '6':
        print("Terima kasih telah menggunakan PlayTune!")
        break
        
    else:
        print("Pilihan menu tidak valid.")