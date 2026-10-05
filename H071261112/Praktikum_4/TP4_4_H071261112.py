def konversi(suhu, asal: str, tujuan: str):
    if asal == "C":
        if tujuan == "F":
            nilai = (suhu * 1.8) + 32
            return nilai
        elif tujuan == "K":
            nilai = suhu + 273.15
            return nilai
        else:
            nilai = suhu
            return nilai
    if asal == "F":
        if tujuan == "C":
            nilai = (suhu - 32) * 5 / 9
            return nilai
        if tujuan == "K":
            nilai = (suhu -32) * 5 / 9 + 273.15
            return nilai
        else:
            nilai = suhu
            return nilai
    if asal == "K":
        if tujuan == "C":
            nilai = suhu - 273.15
            return nilai
        if tujuan == "F":
            nilai = (suhu - 273.15) * 1.8 + 32
            return nilai
        else:
            nilai = suhu
            return nilai


print("=== Konversi Suhu ===")
while True:
    try:
        nilai_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
        if nilai_suhu == "selesai":
            break
        suhu = float(nilai_suhu)
        try:
            skala_asal = input("Skala asal (C/F/K): ")
            skala_tujuan = input("Skala tujuan (C/F/K): ")
            if skala_asal != "C" and skala_asal != "F" and skala_asal != "K":
                raise ValueError("Error")
            if skala_tujuan != "C" and skala_tujuan != "F" and skala_tujuan != "K":
                raise ValueError("Error")
            konversi_akhir = konversi(suhu, skala_asal, skala_tujuan)
            print(f"Hasil: {suhu} {skala_asal} = {konversi_akhir} {skala_tujuan}")
        except:
            print("Error: Skala suhu tidak dikenali.")
            continue
    except:
        print("Input yang anda masukkan tidak valid")
        continue

