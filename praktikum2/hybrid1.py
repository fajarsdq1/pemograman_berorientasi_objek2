#FAJAR SODIK
#210511101
#KELAS C

# Paradigma Pemrograman Berorientasi Objek
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    def display_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)

class Matakuliah:
    def __init__(self, kode_mk, nama_mk):
        self.kode_mk = kode_mk
        self.nama_mk = nama_mk
    
    def display_info(self):
        print("Kode MK:", self.kode_mk)
        print("Nama MK:", self.nama_mk)

class Nilai(Mahasiswa, Matakuliah):
    def __init__(self, nama, nim, kode_mk, nama_mk, nilai):
        Mahasiswa.__init__(self, nama, nim)
        Matakuliah.__init__(self, kode_mk, nama_mk)
        self.nilai = nilai
    
    def display_info(self):
        Mahasiswa.display_info(self)
        Matakuliah.display_info(self)
        print("Nilai:", self.nilai)

# Penggunaan Program
nilai = Nilai("Fajar", "210511101", "TIF21C", "PBO2", 99)
nilai.display_info()
