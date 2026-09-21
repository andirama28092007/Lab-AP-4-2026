# NOMOR 1
pedas = int(input("masukkan persentase kependasan :"))

if pedas >= 0 and pedas <= 10:
    print("Level Aman")
elif pedas >= 11 and pedas <= 40:
    print("Level Sedang")
elif pedas >=41 and pedas <=70:
    print ("Level Pedas")
elif pedas >= 71 and pedas <= 100:
    print("Level Extream")
else:
    print("input tidak valid")