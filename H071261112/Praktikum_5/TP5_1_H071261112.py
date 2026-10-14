huruf = "abcdefghijklmnopqrstuvwxyz"
# funsi untuk mengecek dan membersihkan teks
def bersihkan_teks(text):
    simpan = ""
    for i in text:
        if i in huruf:
            simpan += i
    return simpan

# fungsi untuk mengecek kata yang dibalik apakah sama dengan sabelum dibalik
def cek_palinrome(text):
    teks_terbalik = "".join(reversed(text))
    panjang_teks = len(text)
    for i in range(panjang_teks):
        if text[i] != teks_terbalik[i]:
            return (False, i)
    return (True, -1)

# untuk melihat panjang isi dan lainlain
def inti_palinrome(text):
    teks_bersih = bersihkan_teks(text)
    palinrome_terpanjang = ""
    panjang_teks = len(teks_bersih)
    for i in range(panjang_teks):
        for j in range(i + 1, panjang_teks + 1):
            potongan = teks_bersih[i:j]
            palinrome = cek_palinrome(potongan)[0]
            if palinrome:
                if len(potongan) > len(palinrome_terpanjang):
                    palinrome_terpanjang = potongan
                    indeks_awal = i
    return {
        "teks": palinrome_terpanjang,
        "panjang": len(palinrome_terpanjang),
        "indek_awal": indeks_awal
    }

input_kata = input("Masukkan teks prasasti: ").lower()
tes = inti_palinrome(input_kata)
bersih = bersihkan_teks(input_kata)
print(f"Teks Bersih: {bersih}")
print(f"Output Terharap: {tes}")