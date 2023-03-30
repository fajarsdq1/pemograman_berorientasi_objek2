#FAJAR SODIK
#210511101
#KELAS C

class Animal:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bergerak(self):
        print(self.nama, "berjalan")

class Kambing(Animal):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu

    def bersuara(self):
        print("Mbekkk!")

kambingA = Kambing("Sumbing", 2, "Samosir")
kambingA.bergerak() # output: Sumbing berjalan
kambingA.bersuara() # output: Mbekkk!