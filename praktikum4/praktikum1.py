class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang
        self.jurnal_publikasi = []

    def tambah_jurnal(self, jurnal):
        self.jurnal_publikasi.append(jurnal)

    def __str__(self):
        return f"{self.nama} ({self.bidang})"

class Jurnal:
    def __init__(self, judul, tahun_terbit):
        self.judul = judul
        self.tahun_terbit = tahun_terbit

    def __str__(self):
        return f"{self.judul} ({self.tahun_terbit})"


# Contoh penggunaan komposisi
peneliti1 = Peneliti("Dr. Nurfadhlina Mohd Sharef", "Informatika")
jurnal1 = Jurnal("A Review of Feature Selection Techniques in Intrusion Detection System", 2018)
jurnal2 = Jurnal("Intelligent Intrusion Detection System using Hybrid Machine Learning Algorithm", 2021)

peneliti1.tambah_jurnal(jurnal1)
peneliti1.tambah_jurnal(jurnal2)

print(f"Peneliti: {peneliti1}")
print("Jurnal yang diterbitkan:")
for jurnal in peneliti1.jurnal_publikasi:
    print(jurnal)
