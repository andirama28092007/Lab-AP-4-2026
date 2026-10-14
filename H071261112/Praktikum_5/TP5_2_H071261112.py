huruf = "abcdefghijklmnopqrstuvwxyz"

def cek_kata(teks, kata):
    indeks_list = []
    start = 0
    while True:
        posisi = teks.find(kata, start)
        if posisi == -1:
            break
        indeks_list.append(posisi)
        start = posisi + 1
    return indeks_list

def cek_batas_kata(teks, i, panjang):
    if i > 0:
        kata_sebelum = teks[i - 1]
        if kata_sebelum == huruf or kata_sebelum == huruf.upper():
            return False
    if i + panjang < len(teks):
        kata_sesudah = teks[i + panjang]
        if kata_sesudah == huruf or kata_sesudah == huruf.upper():
            return False
    return True

def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    indeks_kemunculan = cek_kata(teks, kata)
    indeks_valid = [i for i in indeks_kemunculan if cek_batas_kata(teks, i, panjang)]
    teks_akhir = ""
    last_idx = 0
    pengganti = simbol * panjang
    
    for idx in indeks_valid:
        teks_akhir += teks[last_idx:idx] + pengganti
        last_idx = idx + panjang
    teks_akhir += teks[last_idx:]
    return teks_akhir, len(indeks_valid), indeks_valid


teks = input("Masukkan Teks: ").lower ()
kata_target = input("Masukkan kata target: ").lower ()
simbol = input("Masukkan simbol: ")

teks_baru, jumlah, daftar_indeks = sensor_kata(teks, kata_target, simbol)

print(f"Hasil Sensor  : {teks_baru}")
print(f"Jumlah Tersensor : {jumlah}")
print(f"Indeks Awal      : {daftar_indeks}")