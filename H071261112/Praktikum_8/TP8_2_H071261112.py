import re

name_valid = []
def Validasi(name):
    pattern = r"^[a-zA-Z]\w{4,12}$"
    result = re.match(pattern, name)
    if result:
        name_valid.append(name)
        print("Username tersedia.")
    else:
        print("Username tidak valid!")
    return name_valid

def rekap(data):
    nomor = 0
    if data:
        print("\n=== Rekapitulasi ===")
        print("Username valid:")
        for i in data:
            nomor += 1
            print(f"{nomor}. {i}")
        print(f"\nJumlah username valid: {nomor}")
    else:
        print("\nTidak ada username yang di input!\n")

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
while True:
    username = input("\nMasukkan username: ")
    if username == "SELESAI":
        break
    if username not in name_valid:
        Validasi(username)
    else:
        print("Username telah di input sebelumnya!")

rekap(name_valid)