# variable menu, harga, jumlah
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# perkalian harga dengan jumlah untuk setiap menu
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

# total masing-masing dari 3 sub di atas
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# pertotalan
total_barang = sum(jumlah) # total barang
total_seluruh = sum(subtotal_pendapatan) # total pendapatan (kotor)

# melakukan perhitungan pendapatan bersih
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# melakukan True and False untuk menentukan apakah target tercapai atau tidak
target = total_seluruh > 200000 and total_barang > 10

# Output
print(f"total: {total_seluruh}")
print(pendapatan_bersih)
print(target)