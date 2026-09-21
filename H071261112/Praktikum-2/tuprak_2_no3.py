# NOMOR 3
nilai = int(input("masukkan nilai tes anda:"))


if nilai >= 80:
    print("anda lolos ke tahap wawancara")
elif nilai < 80 and nilai >= 65:
    pengalaman = int(input("masukkan pengalaman kerja (tahun):"))
    if pengalaman >= 2:
        print("anda dinyatakan lolos bersyarat")
    else:
        print("anda tidak lolos")
elif nilai < 0:
    print("input tidak valid")
else:
    print("anda tidak lolos")
