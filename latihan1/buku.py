class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}")

bukuA = Buku("Beruang Kutub dan Panda", "Matthew J.baek")
bukuA.info()