class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.magang = None

    def gabung_kelompok(self, kelompok):
        self.magang= kelompok
        kelompok.tambah_anggota(self)

    def __str__(self):
        return f"{self.nama} ({self.nim})"

class Magang:
    def __init__(self, nomor, dosen_pengampu):
        self.nomor = nomor
        self.dosen_pengampu = dosen_pengampu
        self.anggota = []

    def tambah_anggota(self, mahasiswa):
        self.anggota.append(mahasiswa)

    def __str__(self):
        return f"Magang {self.nomor} (Dosen Pengampu: {self.dosen_pengampu})"


# Contoh penggunaan komposisi
mahasiswa1 = Mahasiswa("Fajar", "101")
mahasiswa2 = Mahasiswa("Afan", "102")
mahasiswa3 = Mahasiswa("Zidan", "103")
mahasiswa4 = Mahasiswa("Indra", "104")
kelompok1 = Magang(1, "Freddy Wicaksono")

mahasiswa1.gabung_kelompok(kelompok1)
mahasiswa2.gabung_kelompok(kelompok1)
mahasiswa3.gabung_kelompok(kelompok1)
mahasiswa4.gabung_kelompok(kelompok1)

print(f"Magang: {kelompok1}")
print("Anggota:")
for anggota in kelompok1.anggota:
    print(anggota)