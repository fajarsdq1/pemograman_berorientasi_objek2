#FAJAR SODIK
#210511101
#KELAS C

class Warna:
    def __init__(self, nama_warna, hex_code):
        self.nama_warna = nama_warna
        self.hex_code = hex_code

    def display_info(self):
        print("Nama Warna:", self.nama_warna)
        print("Kode Hex:", self.hex_code)

class WarnaDasar(Warna):
    def __init__(self, nama_warna, hex_code, rgb_code):
        super().__init__(nama_warna, hex_code)
        self.rgb_code = rgb_code

    def display_info(self):
        super().display_info()
        print("Kode RGB:", self.rgb_code)
        print("Kategori: Warna Dasar")

class WarnaCampuran(Warna):
    def __init__(self, nama_warna, hex_code, daftar_warna):
        super().__init__(nama_warna, hex_code)
        self.daftar_warna = daftar_warna

    def display_info(self):
        super().display_info()
        print("Daftar Warna:", self.daftar_warna)
        print("Kategori: Warna Campuran")

# Penggunaan Program
warna1 = Warna("Merah", "#FF0000")
warna1.display_info()

warna2 = WarnaDasar("Kuning", "#FFFF00", "255, 255, 0")
warna2.display_info()

warna3 = WarnaCampuran("Hijau Tua", "#008000", ["Hijau", "Putih"])
warna3.display_info()
