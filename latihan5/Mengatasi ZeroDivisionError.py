#Contoh 1: Mengatasi Type Error
try:
    x = "Hello"
    y = x + 5
except TypeError:
    print("Terjadi kesalahan tipe data, pastikan variabel yang digunakan sudah benar!")

#Contoh 2 : Mengatasi ZeroDivisionError
try:
    x = 10
    y = x / 0
except ZeroDivisionError:
    print("Terjadi kesalahan pembagian dengan nol!")

#Contoh 3 : Mengatasi FileNotFoundError
try:
    with open("file_yang_tidak_ada.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File yang diminta tidak ditemukan!")

#Contoh 4 : Mengatasi KeyError
dictionary = {"satu": 1, "dua": 2, "tiga": 3}
try:
    value = dictionary["empat"]
except KeyError:
    print("Key yang diminta tidak ditemukan pada dictionary!")

#Contoh 5 : Mengatasi IndexError
list_angka = [1, 2, 3]
try:
    value = list_angka[4]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")

#Contoh 6 : Mengatasi AttributeError
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
manusia = Manusia("Andi", 20)
try:
    print(manusia.alamat)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")

#Contoh 7 : Mengatasi ValueError
try:
    angka = int("bukan_angka")
except ValueError:
    print("Terjadi kesalahan konversi nilai ke dalam tipe data yang diinginkan!")

#Contoh 8 : Mengatasi NameError
try:
    print("nama")
except NameError:
    print("Variabel yang diminta belum didefinisikan!")

#Contoh 9 : Mengatasi KeyboardInterrupt
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program dihentikan oleh pengguna!")

#Contoh 10 : Mengatasi MemoryError
try:
    data = " " * (10**10)
except MemoryError:
    print("Memori tidak cukup untuk menampung data yang diminta!")