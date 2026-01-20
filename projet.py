# commande git log permet de voir tous les commits éffectués
# git branch -a pour voir toutes les branches(principal et autres)

from tabulate import tabulate 

class Personne:
    def __init__(self ,a,b,c):
        self.a=input("entrez un nom")
        self.b=input("entrer la nature")
        self.c=int(input("entrer le point de vie"))
        
            
    def info(self):
        print(self.a,"est une ",self.b,"ayant",self.c,"de vie")








perso1=Personne("Alice","Guerrière", 100)
perso1.info()
