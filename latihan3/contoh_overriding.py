#contoh 1
class Matematika: 
    def add(self, a, b): 
        return a + b 
        
    def add(self, a, b, c=0): 
        return a + b + c 
        
mat = Matematika() 
B = mat.add(5, 3, 4) 
print(B) 

mut = Matematika() 
C = mut.add(7,3) 
print(C)

#contoh 2
class Shape: 
    def area(self): 
        pass 
    
class Rectangle(Shape): 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 
        
    def area(self): 
        return self.width * self.height 
        
class Circle(Shape): 
    def __init__(self, radius): 
        self.radius = radius 
        
    def area(self): 
        return 3.14 * self.radius ** 2 
        
shapes = [Rectangle(3, 4), Circle(5)] 
for shape in shapes: 
    print(shape.area())

#contoh 3
class Animal: 
    def make_sound(self): 
        print("The animal makes a sound") 
        
class Dog(Animal): 
    def make_sound(self): 
        print("The dog barks") 
        
class Cat(Animal): 
    def make_sound(self): 
        print("The cat meows") 
        
class Chihuahua(Dog): 
    def make_sound(self): 
        print("The chihuahua yaps") 
        
class Siamese(Cat): 
    def make_sound(self): 
        print("The Siamese purrs") 
        
def animal_sound(animal): 
    animal.make_sound() 

# Instantiate objects of each class 
animal = Animal() 
dog = Dog() 
cat = Cat() 
chihuahua = Chihuahua() 
siamese = Siamese() 

# Call the animal_sound function for each object 
animal_sound(animal) # Output: The animal makes a sound 
animal_sound(dog) # Output: The dog barks 
animal_sound(cat) # Output: The cat meows 
animal_sound(chihuahua) # Output: The chihuahua yaps 
animal_sound(siamese) # Output: The Siamese purrs

#contoh 4
from abc import ABC, abstractmethod 

class Vehicle(ABC): 
    @abstractmethod 
    def start(self): 
        pass 
    
class Car(Vehicle): 
    def start(self): 
        print("Starting car...") 
        
class Motorcycle(Vehicle): 
    def start(self): 
        print("Starting motorcycle...") 
        
class Bus(Vehicle): 
    def start(self): 
        print("Starting bus...") 
        
vehicles = [Car(), Motorcycle(), Bus()] 
for vehicle in vehicles: 
    vehicle.start()

#contoh 5
class Kucing: 
    def bersuara(self): 
        print("Meow") 
        
class Anjing: 
    def bersuara(self): 
        print("Guk guk") 
        
def cetak_suara(objek): 
    objek.bersuara() 
    
kucing = Kucing() 
anjing = Anjing()

cetak_suara(kucing) # Output: Meow 
cetak_suara(anjing) # Output: Guk guk

