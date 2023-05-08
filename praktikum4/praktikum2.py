class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok_kkm = None

    def gabung_kelompok(self, kelompok):
        self.kelompok_kkm = kelompok
        kelompok.tambah_anggota(self)

    def __str__(self):
        return f"{self.nama} ({self.nim})"

class Kelompok_KKM:
    def __init__(self, nomor, dosen_pengampu):
        self.nomor = nomor
        self.dosen_pengampu = dosen_pengampu
        self.anggota = []

    def tambah_anggota(self, mahasiswa):
        self.anggota.append(mahasiswa)

    def __str__(self):
        return f"Kelompok KKM {self.nomor} (Dosen Pengampu: {self.dosen_pengampu})"


# Contoh penggunaan komposisi
mahasiswa1 = Mahasiswa("Fajar", "210511101")
mahasiswa2 = Mahasiswa("Sodik", "210511101")
kelompok1 = Kelompok_KKM(1, "Dr. xxx")

mahasiswa1.gabung_kelompok(kelompok1)
mahasiswa2.gabung_kelompok(kelompok1)

print(f"Kelompok KKM: {kelompok1}")
print("Anggota:")
for anggota in kelompok1.anggota:
    print(anggota)
