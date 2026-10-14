ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    is_upper = ch.isupper()
    ch_lower = ch.lower()    
    idx = ALFABET.find(ch_lower)
    if idx == -1:
        return ch
    
    idx_baru = (idx + k) % 26
    huruf_baru = ALFABET[idx_baru]
    
    if is_upper:
        return huruf_baru.upper()
    return huruf_baru

def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil_retas = []
    for k in range(26):
        teks_dekripsi = mesin_dekripsi(sandi, k)
        if teks_dekripsi.lower().find(kata_kunci.lower()) != -1:
            hasil_retas.append((k, teks_dekripsi))
            
    return hasil_retas

pesan_tersita = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci_target = input("Masukkan kata kunci target: ")

output = retas_sandi(pesan_tersita, kata_kunci_target)
print("Output Deskripsi:", output)