#FAJAR SODIK
#210511101
#KELAS C

class Kendaraan:
    def __init__(self, jenis_kendaraan):
        self.jenis_kendaraan = jenis_kendaraan

    def tampilkan_jenis_kendaraan(self):
        print("Jenis kendaraan:", self.jenis_kendaraan)


class Mobil(Kendaraan):
    def __init__(self, jenis_kendaraan, merek_mobil):
        super().__init__(jenis_kendaraan)
        self.merek_mobil = merek_mobil

    def tampilkan_merek_mobil(self):
        print("Merek mobil:", self.merek_mobil)


class Sedan(Mobil):
    def __init__(self, jenis_kendaraan, merek_mobil, jenis_sedan):
        super().__init__(jenis_kendaraan, merek_mobil)
        self.jenis_sedan = jenis_sedan

    def tampilkan_jenis_sedan(self):
        print("Jenis sedan:", self.jenis_sedan)


sedan1 = Sedan("Mobil", "Toyota", "Sedan")
sedan1.tampilkan_jenis_kendaraan()
sedan1.tampilkan_merek_mobil()
sedan1.tampilkan_jenis_sedan()