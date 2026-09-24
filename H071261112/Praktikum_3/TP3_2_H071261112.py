# print("--- Setup Denah Bioskop NontonYuk ---")

# while True:
#     try:
#         baris = int(input("Masukkan jumlah baris: "))
#         if baris <= 0:
#             print("Jumlah baris harus lebih dari 0!")
#             continue
#         kursi = int(input("Masukkan jumlah kursi per baris: "))
#         if kursi <= 0:
#             print("Jumlah kursi tidak boleh 0")
#             continue
#         break
#     except:
#         print("Input baris harus berupa angka!")

# for a in range(1, baris + 1):
#     for b in range(1, kursi + 1):
#         if b == 13:
#             continue
#         if a == 1 and b % 2 == 0:
#             continue
#         print(f"Baris {a}, Kursi {b}")

a = ["ayam","ikan"]
b = ["bbek", "kambing"]
for i in a:
    for j in b:
        print(i,j)