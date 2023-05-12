class KubusMeta(type): 
    def __init__(cls, name, bases, attrs): 
        super().__init__(name, bases, attrs) 

        #Tambahkan method untuk menghitung luas dan volume kubus
        def luas(cls, sisi): 
            return sisi * sisi 
        cls.luas = classmethod(luas) 

        def volume(cls, sisi): 
            return sisi * sisi * sisi 
        cls.volume = classmethod(volume) 
        
class Kubus(metaclass=KubusMeta): 
    pass
k = Kubus() 
# Menghitung luas segitiga dengan sisi=10 
luas_kubus = Kubus.luas(12) 
print("Luas Kubus:", luas_kubus) 
# Menghitung volume segitiga dengan sisi=10
volume_kubus = Kubus.volume(15) 
print("Volume Kubus:", volume_kubus)
