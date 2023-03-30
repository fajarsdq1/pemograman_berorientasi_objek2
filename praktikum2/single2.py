#FAJAR SODIK
#210511101
#KELAS C

class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def presentasi(self):
        print(f"{self.nama} sedang presentasi.")

class Mahasiswa(Manusia):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nip = nim

    def belajar(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang belajar.")

MahasiswaA = Mahasiswa("Ismawati", 20, "210511101")
MahasiswaA.presentasi() # Output: Ismawati sedang Presentasi.
MahasiswaA.belajar() # Output: Ismawati dengan NIM 210511101 sedang Presentasi.