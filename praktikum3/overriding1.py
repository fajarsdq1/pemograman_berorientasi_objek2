#Nama : FAJAR SODIK
#Nim : 210511101
#Kelas : TIF21C / R3

class Hero:
    def help(self):
        print("Hero in here")

class Superman(Hero):
    def help(self):
        print("Superman is helping you")

class Batman(Hero):
    def help(self):
        print("Batman in dark is coming to you")

class Ahmad(Superman):
    def help(self):
        print("Ahmad akan menolongmu")

class Joko(Superman):
    def help(self):
        print("Joko sang pahlawan kegelapan akan menghampirimu")

def hero_help(hero):
    hero.help()

hero = Hero()
parman = Superman()
batman = Batman()
orang1 = Ahmad()
orang2 = Joko()

hero_help(hero)
hero_help(parman)
hero_help(batman)
hero_help(orang1)
hero_help(orang2)