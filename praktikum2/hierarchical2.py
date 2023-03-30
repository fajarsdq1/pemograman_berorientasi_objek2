#FAJAR SODIK
#210511101
#KELAS C

class Universitas:
    def __init__(self, nama, alamat, tahun_berdiri):
        self.nama = nama
        self.alamat = alamat
        self.tahun_berdiri = tahun_berdiri

    def display_info(self):
        print("Nama Universitas:", self.nama)
        print("Alamat:", self.alamat)
        print("Tahun Berdiri:", self.tahun_berdiri)

class Fakultas(Universitas):
    def __init__(self, nama, alamat, tahun_berdiri, dekan):
        super().__init__(nama, alamat, tahun_berdiri)
        self.dekan = dekan
    
    def display_info(self):
        super().display_info()
        print("Nama Dekan:", self.dekan)
        print("Kategori: Fakultas")

class ProgramStudi(Universitas):
    def __init__(self, nama, alamat, tahun_berdiri, prodi, kaprodi):
        super().__init__(nama, alamat, tahun_berdiri)
        self.prodi = prodi
        self.kaprodi = kaprodi
    
    def display_info(self):
        super().display_info()
        print("Program Studi:", self.prodi)
        print("Ketua Program Studi:", self.kaprodi)
        print("Kategori: Program Studi")

# Penggunaan Program
universitas1 = Universitas("Universitas Muhammadiyah Cirebon", "Jl. Fatahillah, Watubelah, Kec. Sumber, Kabupaten Cirebon, Jawa Barat 45611", 2000)
universitas1.display_info()

fakultas1 = Fakultas("Fakultas Teknik", "Jl. Fatahillah, Watubelah, Kec. Sumber, Kabupaten Cirebon, Jawa Barat 45611", 2000, "Dian Novianti")
fakultas1.display_info()

prodi1 = ProgramStudi("Universitas Muhammadiyah Cirebon", "Jl. Fatahillah, Watubelah, Kec. Sumber, Kabupaten Cirebon, Jawa Barat 45611", 2000, "Teknik Informatika", "Dian Novianti")
prodi1.display_info()
