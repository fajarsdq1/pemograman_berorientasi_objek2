#FAJAR SODIK
#210511101
#KELAS C

class Pesawat:
    def __init__(self, jenis, merk, tahun):
        self.jenis = jenis
        self.merk = merk
        self.tahun = tahun

    def display_info(self):
        print("Jenis:", self.jenis)
        print("Merk:", self.merk)
        print("Tahun:", self.tahun)

class PesawatKomersial(Pesawat):
    def __init__(self, jenis, merk, tahun, jumlah_penumpang):
        super().__init__(jenis, merk, tahun)
        self.jumlah_penumpang = jumlah_penumpang
    
    def display_info(self):
        super().display_info()
        print("Jumlah Penumpang:", self.jumlah_penumpang)
        print("Kategori: Pesawat Komersial")

class PesawatMiliter(Pesawat):
    def __init__(self, jenis, merk, tahun, kecepatan_maksimum):
        super().__init__(jenis, merk, tahun)
        self.kecepatan_maksimum = kecepatan_maksimum
    
    def display_info(self):
        super().display_info()
        print("Kecepatan Maksimum (km/jam):", self.kecepatan_maksimum)
        print("Kategori: Pesawat Militer")

class PesawatPenumpang(PesawatKomersial):
    def __init__(self, jenis, merk, tahun, jumlah_penumpang, kelas):
        super().__init__(jenis, merk, tahun, jumlah_penumpang)
        self.kelas = kelas
    
    def display_info(self):
        super().display_info()
        print("Kelas:", self.kelas)
        print("Jenis Pesawat: Pesawat Penumpang")

class PesawatKargo(PesawatKomersial):
    def __init__(self, jenis, merk, tahun, jumlah_penumpang, kapasitas_kargo):
        super().__init__(jenis, merk, tahun, jumlah_penumpang)
        self.kapasitas_kargo = kapasitas_kargo
    
    def display_info(self):
        super().display_info()
        print("Kapasitas Kargo:", self.kapasitas_kargo)
        print("Jenis Pesawat: Pesawat Kargo")

# Penggunaan Program
pesawat1 = Pesawat("Terbang Tinggi", "Airbus", 2010)
pesawat1.display_info()

pesawat_penumpang1 = PesawatPenumpang("Boeing", "747", 2005, 500, "Bisnis")
pesawat_penumpang1.display_info()

pesawat_kargo1 = PesawatKargo("Antonov", "An-124", 1999, 0, 150000)
pesawat_kargo1.display_info()

pesawat_militer1 = PesawatMiliter("F-16", "Lockheed Martin", 1988, 2410)
pesawat_militer1.display_info()
