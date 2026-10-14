database_email = []
domain_list = (".com", ".id", ".ac.id",)

def deteksi_anomali_email(email):
    list_error = []
    if " " in email:
        list_error.append("Email tidak boleh memiliki spasi")
    if email.count("@") != 1:
        list_error.append("Harus memiliki tepat satu karakter @")
        return list_error

    local, domain = email.split("@")

    if not local or not domain:
        list_error.append("Bagian sebelum @ (local) atau setelah @ (domai) tidak boleh kosong")

    if local:
        if local.startswith(".") or local.endswith("."):
            list_error.append("Bagian local tidak boleh diawali atau diakhiri titik, serta tidak boleh mengandung titik berurutan")
        if ".." in local:
            list_error.append("Bagian local tidak boleh diawali atau diakhiri titik, serta tidak boleh mengandung titik berurutan")

    if domain:
        if not "." in domain:
            list_error.append("Bagian domain wajib memiliki minimal satu titik")
        if ".." in domain:
            list_error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
        if domain.endswith("."):
            list_error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
        if domain.startswith("."):
            list_error.append("Bagian setelah domain(@) tidak boleh kosong")

    if not email.lower().endswith(domain_list):
        list_error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    if not list_error and email in database_email:
        list_error.append("Email sudah terdaftar (Duplikat)")

    return list_error

def cetak_daftar(daftar_email_valid, karakter_border):
    if not database_email:
        return ""
    email_terpanjang = max(len(email) for email in database_email)
    lebar_garis = email_terpanjang + 2
    garis_horizontal = karakter_border * lebar_garis

    hasil_bingkai = [f"+{garis_horizontal}+"]
    for email in daftar_email_valid:
        baris = f"| {email.ljust(email_terpanjang)} |"
        hasil_bingkai.append(baris)
    hasil_bingkai.append(f"+{garis_horizontal}+")

    return "\n".join(hasil_bingkai)

print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")

print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")
while True:
    user = input("Masukkan email: ")
    email_bersih = deteksi_anomali_email(user)
    if user == "tutup":
        break
    if not email_bersih:
        database_email.append(user.lower())
        print("Email VALID!")
    else:
        print("Email DITOLAK karena:")
        for error in email_bersih:
            print(f"   - {error}")

print()
print("--- HASIL EMAIL VALID ---")
if database_email:
        bingkai_teks = cetak_daftar(database_email, border)
        print(bingkai_teks)
        print()
else:
    print("(Tidak ada email valid yang terdaftar)")
    