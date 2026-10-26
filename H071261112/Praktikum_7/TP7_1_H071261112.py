import os
import random
from datetime import datetime

folder = os.path.dirname(os.path.abspath(__file__))
folder_invoices = os.path.join(folder, "invoices")
file_history = os.path.join(folder, "trx_history.txt")

# NOMOR 1
def siapkan_folder():
    os.makedirs(folder_invoices, exist_ok=True)
    if not os.path.exists(file_history):
        with open(file_history, "w") as file:
            file.write("=" * 76 + "\n")
            file.write(
                f"| {'Waktu':19} | {'ID Transaksi':15} "
                f"| {'Nominal Transaksi':23} |\n")
            file.write("=" * 76 + "\n")

def dapatkan_inisial(nama):
    inisial = "".join(kata[0].upper() for kata in nama.strip().split())
    inisial = "".join(huruf for huruf in inisial if huruf.isalnum())
    return inisial or "KSR"

def buat_id_transaksi(kasir):
    waktu = datetime.now()
    bagian_waktu = waktu.strftime("%y%m%d%H%M")
    inisial = dapatkan_inisial(kasir)
    id_transaksi = f"{inisial}{bagian_waktu}{random.randint(100, 999)}"
    while os.path.exists(os.path.join(folder_invoices, id_transaksi + ".txt")):
        id_transaksi = f"{inisial}{bagian_waktu}{random.randint(100, 999)}"
    return id_transaksi, waktu

def catat_riwayat(waktu, id_transaksi, total):
    try:
        with open(file_history, "a") as file:
            file.write(
                f"| {waktu:19} | {id_transaksi:15} "
                f"| Rp {total:20,} |\n".replace(",", "."))
            file.write("=" * 76 + "\n")
        return True
    except OSError:
        print("Gagal mencatat riwayat transaksi.")
        return False

def membuat_invoice(kasir, produk):
    id_transaksi, waktu = buat_id_transaksi(kasir)
    waktu_str = waktu.strftime("%Y-%m-%d %H:%M:%S")
    nama_file = os.path.join(folder_invoices, id_transaksi + ".txt")
    total = 0
    lebar = 67
    isi_invoice = [
        "=" * lebar,
        "TOKO SEDERHANA".center(lebar),
        "=" * lebar,
        f"Nama kasir   : {kasir}",
        f"Waktu        : {waktu_str}",
        f"ID transaksi : {id_transaksi}",
        "-" * lebar,
        f"| {'Produk':<20} | {'Harga':>14} | {'Jumlah':>6} | {'Subtotal':>14} |",
        "-" * lebar,]
    for item in produk:
        subtotal = item["harga"] * item["jumlah"]
        total += subtotal
        harga = f"{item['harga']:,}".replace(",", ".")
        subtotal_str = f"{subtotal:,}".replace(",", ".")
        isi_invoice.append(
            f"| {item['nama'][:20]:<20} | {harga:>14} | "
            f"{item['jumlah']:>6} | {subtotal_str:>14} |")
    isi_invoice.extend([
        "-" * lebar,
        f"TOTAL BELANJA: Rp {total:,}".replace(",", "."),
        "=" * lebar,
        "Terima kasih telah berbelanja!".center(lebar),
        "=" * lebar,])
    teks_invoice = "\n".join(isi_invoice) + "\n"
    try:
        with open(nama_file, "w") as file:
            file.write(teks_invoice)
    except OSError:
        print("Gagal menyimpan invoice.")
        return
    berhasil_dicatat = catat_riwayat(waktu_str, id_transaksi, total)
    if berhasil_dicatat:
        print("\nTransaksi berhasil!")
    else:
        print("\nInvoice berhasil disimpan,")
        print("tetapi riwayat transaksi gagal dicatat.")
    print("ID transaksi :", id_transaksi)
    print("Invoice      :", nama_file)
    print("Total        : Rp", format(total, ",").replace(",", "."))
    print("\n" + teks_invoice)
# =================================================================================

# NOMOR 2
def cari_invoice():
    id_transaksi = input("Masukkan ID transaksi: ").strip()
    nama_file = os.path.join(folder_invoices, id_transaksi + ".txt")
    try:
        with open(nama_file, "r") as file:
            print("\nInvoice ditemukan!\n")
            print(file.read())
    except FileNotFoundError:
        print("Invoice tidak ditemukan!")
    except OSError:
        print("Terjadi kesalahan saat membaca invoice.")
# ================================================================================= 

# NOMOR 3
def tampilkan_riwayat():
    try:
        with open(file_history, "r") as file:
            print("\n" + "=" * 45)
            print("          RIWAYAT TRANSAKSI")
            print("=" * 45)
            print(file.read())
    except FileNotFoundError:
        print("File riwayat belum tersedia.")
    except OSError:
        print("Gagal membaca riwayat transaksi.")
# ================================================================================

try:
    siapkan_folder()
except OSError:
    print("Gagal menyiapkan folder atau file riwayat.")
    raise SystemExit
# Menjalankan menu utama aplikasi kasir.
print("=" * 40)
print("APLIKASI KASIR".center(40))
print("=" * 40)
nama_kasir = input("Nama kasir: ").strip().title()
while True:
    print("\n1. Transaksi baru")
    print("2. Cari invoice")
    print("3. Riwayat transaksi")
    print("4. Keluar")
    pilihan = input("Pilih menu: ").strip()
    if pilihan == "1":
        if not nama_kasir:
            print("Nama kasir tidak boleh kosong!")
            continue
        daftar_produk = []
        while True:
            nama = input("Nama produk: ").strip()
            if not nama:
                print("Nama produk tidak boleh kosong!")
                continue
            while True:
                try:
                    harga = int(input("Harga produk: Rp "))
                    if harga <= 0:
                        print("Harga harus lebih dari 0!")
                        continue
                    break
                except ValueError:
                    print("Harga harus berupa angka!")
            while True:
                try:
                    jumlah = int(input("Jumlah produk: "))
                    if jumlah <= 0:
                        print("Jumlah harus lebih dari 0!")
                        continue
                    break
                except ValueError:
                    print("Jumlah harus berupa angka!")
            daftar_produk.append({
                "nama": nama,
                "harga": harga,
                "jumlah": jumlah})
            while True:
                tambah = input("Tambah produk? (y/t): ").strip().lower()
                if tambah == "y":
                    break
                elif tambah == "t":
                    break
                else:
                    print("input tidak valid hanya boleh memasukkan y atau t saja")
            if tambah == "t":
                break
        if daftar_produk:
            membuat_invoice(nama_kasir, daftar_produk)
        else:
            print("Transaksi dibatalkan karena belum ada produk.")
    elif pilihan == "2":
        cari_invoice()
    elif pilihan == "3":
        tampilkan_riwayat()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan aplikasi kasir!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1-4.")