class Penulis:
    def __init__(self, nama):
        self.nama = nama
        self.buku = []

    def tulis_buku(self, judul, tahun_terbit):
        buku = Buku(judul, tahun_terbit)
        self.buku.append(buku)
        buku.penulis = self

    def __str__(self):
        return f"{self.nama}"

class Buku:
    def __init__(self, judul, tahun_terbit):
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penulis = None

    def __str__(self):
        return f"{self.judul} ({self.tahun_terbit}) oleh {self.penulis}"

# Contoh penggunaan komposisi
penulis1 = Penulis("Tere Liye")
buku1 = Buku("Negeri Para Bedebah", 2012)
buku2 = Buku("Negeri di ujung tanduk", 2013)

penulis1.tulis_buku(buku1.judul, buku1.tahun_terbit)
penulis1.tulis_buku(buku2.judul, buku2.tahun_terbit)

print(f"Penulis: {penulis1}")
print("Buku:")
for buku in penulis1.buku:
    print(buku)
