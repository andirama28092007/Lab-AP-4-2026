import re

data_nomor = []

def validasi(data):
    pattern_bersih = r"[\s-]"
    pattern_nomor = r"^[0-9]{10,13}$"
    replace = ""
    data_keberapa = 0
    data_valid = 0
    print("\n--- Hasil Pembersihan ---")
    for i in data:
        data_keberapa += 1
        result_bersih = re.sub(pattern_bersih, replace, i)
        resultnya = re.match(pattern_nomor, result_bersih)
        if resultnya:
            print(f"\nData {data_keberapa}:")
            print(f"Sebelum :".ljust(10) + f" {i}")
            print(f"Sesudah :".ljust(10) + f" {result_bersih}")
            print(f"Status :".ljust(10) + " Valid")
            data_valid += 1
        else:
            print(f"\nData {data_keberapa}:")
            print(f"Sebelum :".ljust(10) + f" {i}")
            print(f"Sesudah :".ljust(10) + f" {result_bersih}")
            print(f"Status :".ljust(10) + " Tidak valid")
    print(f"Jumlah Nomor valid: {data_valid}")

print("\n=== Peembersihan Data Nomor Telepon ===\n")
try:
    jumlah_nomor = int(input("Masukkan jumlah data: "))
    berapa_nomor = 0

    while berapa_nomor < jumlah_nomor:
        berapa_nomor += 1 
        nomor_nya = input(f"\nNomor ke-{berapa_nomor}: ")
        pattern = r"^[\d\s-]+$"
        result = re.match(pattern, nomor_nya)
        if result:
            data_nomor.append(nomor_nya)
        else:
            print("Cara anda menginput nomor tidak benar")
            berapa_nomor -= 1
except:
    print("Input yang anda masukka tidak valid!")

validasi(data_nomor)