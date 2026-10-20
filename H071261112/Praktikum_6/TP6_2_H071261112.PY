kandidat_set = set()
rekap_suara = {}

def daftar_kandidat(kandidat_set, nama):
    nama_format = nama.capitalize()
    kandidat_set.add(nama_format)
    print(f"'{nama_format}' berhasil didaftarkan sebagai kandidat")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):       
    nama_lower = nama_pemilih.lower()
    pilihan_format = pilihan.capitalize()
    if nama_lower in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya")
    elif pilihan_format not in kandidat_set:
        print(f"kandidat '{pilihan}' tidak terdaftar")
    else:
        rekap_suara[nama_lower] = pilihan_format
        print(f"Suara '{nama_pemilih}' untuk '{pilihan_format}' berhasil dicatat")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in kandidat_set}
    for kandidat_pilihan in rekap_suara.values():
        if kandidat_pilihan in perolehan:
            perolehan[kandidat_pilihan] += 1
    return perolehan

def tampilkan_hasil(perolehan):
    print("\n=== HASIL PEMILIHAN KETUA KELAS ===")
    for kandidat in sorted(perolehan.keys()):
        print(f"{kandidat}: {perolehan[kandidat]} suara")
    total_suara = sum(perolehan.values())
    print(f"Total suara masuk: {total_suara}")
    print("===================================")
    if total_suara > 0:
        suara_tertinggi = max(perolehan.values())
        pemenang = [k for k, s in perolehan.items() if s == suara_tertinggi]
        if len(pemenang) > 1:
            print(f"Hasil seri antara: {', '.join(sorted(pemenang))}")
            print("Perlu dilakukan pemilihan ulang")
        else:
            print(f"THE WINNER: {pemenang[0]} dengan {suara_tertinggi} suara!!! :)")
    print("===================================")

print("=== SISTEM PEMILIHAN KETUA KELAS ===")
print("\nFASE PENDAFTARAN KANDIDAT")
while True:
    nama = input("masukkan nama kandidat (kosogkan untuk selesai): ")
    if nama == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat sebelum bisa lanjut")
            continue
        else:
            break
    daftar_kandidat(kandidat_set, nama)
print(f"Kandidat terdaftar: {kandidat_set}")
print("\nFASE PEMUNGUTAN SUARA")
while True:
    nama_pemilih = input("Nama Pemilih (kosongkn untuk selesai):")
    if nama_pemilih == "":
        break
    print(f"Kandidat yang tersedia: {kandidat_set}")
    pilihan = input("Pilih kandidat: ")
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)
perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)