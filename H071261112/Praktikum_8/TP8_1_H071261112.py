import re

def Validasi(nim, email, telepon):

    pattern_nim = r"^H071[0-9]{6,6}$"
    result_nim = re.match(pattern_nim, nim)
    if result_nim:
        result_nim = "Valid"
    else:
        result_nim = "Tidak Valid"
    
    pattern_email = r"\w+@\w+\.\w+"
    result_email = re.match(pattern_email, email)
    if result_email:
        result_email = "Valid"
    else:
        result_email = "Tidak Valid"

    pattern_telepon = r"[0-9]{10,13}$"
    pattern_pembersih_telepon = r"-|s+"
    replace = ""
    result_pembersih_telepon = re.sub(pattern_pembersih_telepon, replace, telepon)
    result_telepon = re.match(pattern_telepon, result_pembersih_telepon)
    if result_telepon:
        result_telepon = "Valid"
    else:
        result_telepon = "Tidak Valid"

    print("\n --- Hasil Validasi ---")
    print("NIM".ljust(15) + f": {result_nim}")
    print("Email".ljust(15) + f": {result_email}")
    print("No. Telepon".ljust(15) + f": {result_telepon}")

    if result_nim == "Valid" and result_email == "Valid" and result_telepon == "Valid":
        print("\nData mahasiswa berhasil diverifikasi!")
    else:
        print("\n Data mahasiswa tidak berhasil diverifikasi!")


print("\n=== Validasi Data Mahasiswa ===\n")
nim_nya = input("Masukkan NIM".ljust(18) + ": ")
email_nya = input("Masukkan Email".ljust(18) + ": ")
telepon_nya = input("Masukkan No. Telp".ljust(18) + ": ")

Validasi(nim_nya, email_nya, telepon_nya)

