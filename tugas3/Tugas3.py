#Nama    : Lala 'Adilah
#NIM     : 210511117
#Kelas   : R3/TI21C

import pygame
from tkinter import *

class PemutarMusik():
    
    def __init__(self):
        self.insialisasiFile()
        self.buatTeks()
        self.buatTombolAnjing()
        self.buatTombolAyam()
        self.buatTombolBurung()
        self.buatTombolGajah()
        self.buatTombolHarimau()
        self.buatTombolKambing()
        self.buatTombolKucing()
        self.buatTombolSapi()
        self.buatTombolSerigala()
        self.buatTombolTokek()
        self.buatTombolStop() 
    def insialisasiFile(self):
        self.file1 = 'C:/Users/hp/Documents/TIF/Semester 4/PBO II/Pertemuan 3/Tugas 3/anjing.mp3'
        self.file2 = 'C:/Users/hp/Documents/TIF/Semester 4/PBO II/Pertemuan 3/Tugas 3/ayam.mp3'
        self.file3 = 'C:/Users/hp/Documents/TIF/Semester 4/PBO II/Pertemuan 3/Tugas 3/burung.mp3'
        self.file4 = 'C:/Users/hp/Documents/TIF/Semester 4/PBO II/Pertemuan 3/Tugas 3/gajah.mp3'
        self.file5 = 'C:/Users/hp/Documents/TIF/Semester 4/PBO II/Pertemuan 3/Tugas 3/harimau.mp3'
        self.file6 = 'C:/Users/hp/Documents/TIF/Semester 4/PBO II/Pertemuan 3/Tugas 3/kambing.mp3'
        self.file7 = 'C:/Users/hp/Documents/TIF/Semester 4/PBO II/Pertemuan 3/Tugas 3/kucing.mp3'
        self.file8 = 'C:/Users/hp/Documents/TIF/Semester 4/PBO II/Pertemuan 3/Tugas 3/sapi.mp3'
        self.file9 = 'C:/Users/hp/Documents/TIF/Semester 4/PBO II/Pertemuan 3/Tugas 3/serigala.mp3'
        self.file10 = 'C:/Users/hp/Documents/TIF/Semester 4/PBO II/Pertemuan 3/Tugas 3/tokek.mp3'
    def anjing(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file1)
        pygame.mixer.music.play()
    def ayam(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file2)
        pygame.mixer.music.play()
    def burung(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file3)
        pygame.mixer.music.play()
    def gajah(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file4)
        pygame.mixer.music.play()
    def harimau(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file5)
        pygame.mixer.music.play()
    def kambing(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file6)
        pygame.mixer.music.play()
    def kucing(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file7)
        pygame.mixer.music.play()
    def sapi(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file8)
        pygame.mixer.music.play()
    def serigala(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file9)
        pygame.mixer.music.play()
    def tokek(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file10)
        pygame.mixer.music.play()
   
    def stopMusik(self):
        pygame.mixer.music.stop()
    def buatTeks(self):
        Label(text="ANIMAL VOICE APPLICATION", fg="black", bg="light blue", background = "#1c9a77", font="Calibri 28 bold", width=40, height=4).pack(fil=X)
    def buatTombolStop(self):
        Button(text="Stop", font="Calibri 24 bold", width=10, height=2, background = "#e65b25", command=self.stopMusik).pack(fill=X)
    def buatTombolAnjing(self):
        Button(text="Suara Anjing",  font="verdana 16 bold", width=5, height=1, background = "#D4AC0D", command=self.anjing).pack(fill=X)
    def buatTombolAyam(self):   
        Button(text="Suara Ayam",font="verdana 16 bold", width=5, height=1, background = "#D4AC0D", command=self.ayam).pack(fill=X)
    def buatTombolBurung(self):
        Button(text="Suara Burung", font="verdana 16 bold", width=5, height=1, background = "#D4AC0D", command=self.burung).pack(fill=X)  
    def buatTombolGajah(self):
        Button(text="Suara Gajah", font="verdana 16 bold", width=5, height=1, background = "#D4AC0D", command=self.gajah).pack(fill=X)   
    def buatTombolHarimau(self):
        Button(text="Suara Harimau", font="verdana 16 bold", width=5, height=1, background = "#D4AC0D", command=self.harimau).pack(fill=X)
    def buatTombolKambing(self):
        Button(text="Suara Kambing", font="verdana 16 bold", width=5, height=1, background = "#D4AC0D", command=self.kambing).pack(fill=X)    
    def buatTombolKucing(self):
        Button(text="Suara Kucing", font="verdana 16 bold", width=5, height=1, background = "#D4AC0D", command=self.kucing).pack(fill=X)    
    def buatTombolSapi(self):
        Button(text="Suara Sapi", font="verdana 16 bold", width=5, height=1, background = "#D4AC0D", command=self.sapi).pack(fill=X)    
    def buatTombolSerigala(self):
        Button(text="Suara Serigala", font="verdana 16 bold", width=5, height=1, background = "#D4AC0D", command=self.serigala).pack(fill=X)    
    def buatTombolTokek(self):
        Button(text="Suara Tokek", font="verdana 16 bold", width=5, height=1, background = "#D4AC0D", command=self.tokek).pack(fill=X)    

Tk()
PemutarMusik()
mainloop()
pygame.quit()
