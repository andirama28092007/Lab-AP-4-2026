total_belanja = 0
def sistem(harga, jumlah, adalah_member=False):
    harga_jumlah = harga * jumlah
    if adalah_member:
        harga_jumlah = harga_jumlah * 90/100
        return int(harga_jumlah)
    return int(harga_jumlah)

print("Selamat datang di kasir Minimarket!")
while True:
    status_member = input("Apakah Anda member? (y/n): ")
    if status_member == "y":
        member = 1
        break
    elif status_member == "n":
        member = 2
        break
    else:
        print("Input yang anda masukkan tidak valid")
        continue

while True:
    try:
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
        if nama_barang == "":
            print(f"Total belanja: {total_belanja}")
            break
        harga_barang = int(input("Harga barang: "))
        if harga_barang < 0:
            raise ValueError("Input yang anda masukkan tidak valid")
        jumlah_barang = int(input("Jumlah barang: "))
        if member == 1:
            subtotal = sistem(harga_barang, jumlah_barang, adalah_member=True)
        elif member == 2:
            subtotal = sistem(harga_barang, jumlah_barang,)
        total_belanja += subtotal
        print(f"Subtotal {nama_barang}: {subtotal}")
    except:
        print("Input yang anda masukkan tidak valid")