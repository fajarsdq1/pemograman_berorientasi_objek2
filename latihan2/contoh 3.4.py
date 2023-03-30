class shape:
    def _init_(self, name, color):
        self.name = name
        self.color= color

class twoDimensional(shape):
    def _init_(self, name, color, sides):
        self.name = name
        self.color = color
        self.sides= sides

    def display(self):
        print("name:",self.name)
        print("color:",self.color)
        print("sides:",self.sides)

class thereeDimensional(shape):
    def _init_(self, name, color, faces):
        self.name = name
        self.color = color
        self.faces = faces

    def display(self):
        print("name:",self.name)
        print("color:",self.color)
        print("faces",self.faces)

class sphere(thereeDimensional):
    def _init_(self, name, color, faces, radius):
        self.name = name
        self.color = color
        self.faces = faces
        self.radius = radius

    def display(self):
        print("name:",self.name)
        print("color:",self.color)
        print("faces",self.faces)
        print("radius",self.radius)
        
TW=twoDimensional("lukisan","abstrak","2cm")
TW.display()
T=thereeDimensional("patung","emas","oval")
T.display()
S=sphere("bola sepak","putih dan hitam","5cm","bulat")
S.display()