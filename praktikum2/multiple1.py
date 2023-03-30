#FAJAR SODIK
#210511101
#KELAS C

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def belajar(self):
        print(self.nama, "sedang belajar")

class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan

    def bekerja(self):
        print(self.nama, "sedang bekerja")

class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)

    def bersosialisasi(self):
        print(self.nama, "sedang bersosialisasi")

mhs_pekerja = MahasiswaPekerja("Fajar", "210511101", "Programmer")
mhs_pekerja.belajar() # output: Fajar sedang belajar
mhs_pekerja.bekerja() # output: Fajar sedang bekerja
mhs_pekerja.bersosialisasi() # output: Fajar sedang bersosialisasi