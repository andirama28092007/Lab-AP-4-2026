# NOMOR 2
jarak = int(input("Masukkan Jarak pengiriman:"))
layanan = input("Layanan Expres (ya/tidak) :")

if jarak < 5 and jarak >0 :
    jarak = 10000
elif jarak >= 5 and jarak <= 20:
    jarak = 20000
elif jarak <= 0:
    jarak = 0
else :
    jarak = 35000

express = 15000 if layanan == "ya" else 0
tarif = jarak + express

print(f"total tarif pengiriman: Rp.{tarif}")