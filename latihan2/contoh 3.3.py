class kendaraan:
    def _init_(self, name):
        self.name = name

class mobil(kendaraan):
    def _init_(self, name, merk):
        self.name = name
        self.merk = merk

    def display(self):
        print("name:",self.name)
        print("merk:",self.merk)

class sepedamotor(kendaraan):
    def _init_(self, name, tipe):
        self.name = name
        self.tipe = tipe

    def display(self):
        print("name:",self.name)
        print("tipe:",self.tipe)

class truk(mobil):
    def _init_(self, name, kapasitas, merk):
        self.name = name
        self.kapasitas = kapasitas
        self.merk = merk

    def display(self):
        print("name:",self.name)
        print("kapasitas:",self.kapasitas)
        print("merk:",self.merk)
        
class motorlistrik(sepedamotor):
    def _init_(self, name, tipe, daya):
        self.name = name
        self.tipe = tipe
        self.daya = daya

    def display(self):
        print("name:",self.name)
        print("tipe:",self.tipe)
        print("daya:",self.daya)

m=mobil("brio","honda")
m.display()
B=sepedamotor("ninja","kawasaki")
B.display()
m=truk("fuso","2000kg","mitsubishi")
m.display()
B=motorlistrik("honda u-go","honda","500watt")
B.display()