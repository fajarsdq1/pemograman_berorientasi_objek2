#FAJAR SODIK
#210511101
#KELAS C

# Paradigma Pemrograman Berorientasi Objek
class Karyawan:
    def __init__(self, nama, umur, jenis_kelamin):
        self.nama = nama
        self.umur = umur
        self.jenis_kelamin = jenis_kelamin

    def display_karyawan(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)
        print("Jenis Kelamin:", self.jenis_kelamin)

class Gaji:
    def __init__(self, gaji_pokok, tunjangan, bonus):
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan
        self.bonus = bonus
    
    def display_gaji(self):
        print("Gaji Pokok:", self.gaji_pokok)
        print("Tunjangan:", self.tunjangan)
        print("Bonus:", self.bonus)

class Manager(Karyawan, Gaji):
    def __init__(self, nama, umur, jenis_kelamin, gaji_pokok, tunjangan, bonus):
        Karyawan.__init__(self, nama, umur, jenis_kelamin)
        Gaji.__init__(self, gaji_pokok, tunjangan, bonus)
    
    def display_manager(self):
        Karyawan.display_karyawan(self)
        Gaji.display_gaji(self)
        print("Jabatan: Manager")

class PegawaiTetap(Karyawan, Gaji):
    def __init__(self, nama, umur, jenis_kelamin, gaji_pokok, tunjangan, bonus):
        Karyawan.__init__(self, nama, umur, jenis_kelamin)
        Gaji.__init__(self, gaji_pokok, tunjangan, bonus)
    
    def display_pegawai_tetap(self):
        Karyawan.display_karyawan(self)
        Gaji.display_gaji(self)
        print("Jabatan: Pegawai Tetap")

class PegawaiKontrak(Karyawan):
    def __init__(self, nama, umur, jenis_kelamin, lama_kontrak, gaji):
        Karyawan.__init__(self, nama, umur, jenis_kelamin)
        self.lama_kontrak = lama_kontrak
        self.gaji = gaji
    
    def display_pegawai_kontrak(self):
        Karyawan.display_karyawan(self)
        print("Lama Kontrak (bulan):", self.lama_kontrak)
        print("Gaji per bulan:", self.gaji)
        print("Jabatan: Pegawai Kontrak")

# Penggunaan Program
manager1 = Manager("Fajar", 20, "Laki-laki", 10000000, 5000000, 3000000)
manager1.display_manager()

pegawai_tetap1 = PegawaiTetap("Rizqi", 20, "Laki-laki", 6000000, 3000000, 1000000)
pegawai_tetap1.display_pegawai_tetap()

pegawai_kontrak1 = PegawaiKontrak("Fadli", 21, "Laki laki", 12, 3000000)
pegawai_kontrak1.display_pegawai_kontrak()
