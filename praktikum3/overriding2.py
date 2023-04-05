#Nama : FAJAR SODIK
#Nim : 210511101
#Kelas : TIF21C / R3

class Suhu: 
    def convert_to_celcius(self): 
        pass 
    
class Reamur(Suhu): 
    def __init__(self, reamur): 
        self.reamur = reamur
        
    def convert_to_celcius(self): 
        return 5/4 * self.reamur
        
class Kelvin(Suhu): 
    def __init__(self, kelvin): 
        self.kelvin = kelvin 
        
    def convert_to_celcius(self): 
        return self.kelvin - 273

class Fahrenheit(Suhu): 
    def __init__(self, fahren): 
        self.fahren = fahren 
        
    def convert_to_celcius(self): 
        return 5/9 * (self.fahren - 32)
        
derajat = [Reamur(20), Kelvin(54), Fahrenheit(30)] 
for suhu in derajat: 
    print(suhu.convert_to_celcius())