from math import pi
from random import randint

#exercice 1

class StringFoo:
    def __init__(self):
        self.text = ""
    def set_string(self, text):
        self.text = text
    def  print_string(self):
        print(self.text)

text1 = StringFoo()
text1.set_string("PYcharmm PY chaRMM")
text1.print_string()

#exercice 2

class rectangle:
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur
    def calcul_aire(self):
        return self.base * self.hauteur
    def info(self):
        print(self.base,self.hauteur,self.calcul_aire())


rectangle1 = rectangle(5,6)
rectangle1.info()

#execice 3

class cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    def cercle_circonference(self):
        return 2 * pi * self.rayon
    def cercle_aire(self):
        return pi * self.rayon ** 2
    def info(self):
        print(self.rayon,self.cercle_circonference(),self.cercle_aire())

cercle1 = cercle(5)
cercle1.info()

#exercice 4

class hero:
    def __init__(self, name):
        self.vie = 2 * randint(1,10)
        self.attaque = randint(1,6)
        self.defense = randint(1,6)
        self.name = name
    def real_attaque(self):
        return self.attaque + randint(1,6)
    def dommage(self,dommages):
        self.dommage = dommages
        self.vie = self.vie - self.dommage
    def est_vivant(self):
        if self.vie <= 0:
            return False
        else:
            return True
    def info(self):
        print(self.vie,self.attaque,self.defense,self.name)

hero1 = hero("JFW")
hero1.info()
hero1.dommage(21)
hero1.est_vivant()






