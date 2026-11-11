class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_peforma(self):
        skor = self.hitung_skor_akhir()
        if skor >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        return f" {self.nama}".ljust(12) + " | " + self.id_pemain.ljust(10) + " | " + self.role.ljust(10) + " | " + f"{self.hitung_skor_akhir()}".ljust(10) + " | " + f"{self.status_peforma()}".ljust(16) + " |"

data_pemain = []

print("--- SISTEM PENILAIAN PEFORTMA PEMAIN ---")
while True:
    try:
        jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))
        if jumlah_pemain <= 0:
            print("Jumlah pemain harus lebih dari 0!")
            continue
        else:
            break
    except:
        print("Input yang anda masukkan tidak valid!")
        continue

pemain = 1
while pemain < jumlah_pemain + 1:
    try:
        print(f"\n-- Data Pemain ke-{pemain} --")
        data_nama = input("Nama".ljust(16) + ": ")
        data_id = input("ID Pemain".ljust(16) + ": ")
        data_role = input("Role".ljust(16) + ": ")
        data_kill = int(input("Nilai Kill".ljust(16) + ": "))
        data_assist = int(input("Nilai Assist".ljust(16) + ": "))
        data_objective = int(input("Nilai Objective".ljust(16) + ": "))
        isi_data_pemain = Pemain(data_nama, data_id, data_role, data_kill, data_assist, data_objective)
        data_pemain.append(isi_data_pemain)
        pemain += 1
    except:
        print("Input yang anda masukkan tidak valid!")
        continue

print("\n--- REKAPITULASI PERFORMA PEMAIN ---")
print("=" * 78)
print("| " + "No".ljust(3) + "|" + " Nama".ljust(12) + " | " + "ID Pemain".ljust(10) + " | " + "Role".ljust(10) + " | " + "Skor Akhir".ljust(10) + " | " + "Status".ljust(16) + " |")
print("=" * 78)
for i, isi in enumerate(data_pemain, start=1):
    print(f"| {i}  |" + isi.tampilkan_data())
print("=" * 78)
