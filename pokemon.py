import random
import json
import os.path


  
class Pokemon():
    def __init__(self, name, puissance, level, type):
        self.__pointsVie = 100
        self.__name = name
        self.puissance = puissance
        self.defense = 0
        self.level = level
        self.type = type
        
    def getName(self):
        return self.__name
    
    def getPV(self):
        return self.__pointsVie
    
    def getPuissance(self):
        return self.puissance
    
    def getDefense(self):
        return self.defense
    
    def getLevel(self): 
        return self.level
    
    def getType(self):
        return self.type
    
    def modifierPV(self, pointsVie):
        self.__pointsVie += pointsVie
      
      
    def to_dict(self):
        return {"name": self.__name,"type": self.type,"puissance": self.puissance, "PV": self.__pointsVie, "defense": self.defense, "level": self.level}
        
    def afficher(self):
        print(self.__name, self.__pointsVie, self.puissance, self.defense)
     
class PokemonNormal(Pokemon):
    def __init__(self, name, puissance, pointsVie, defense, level, type="normal"):
        super().__init__(name, puissance,level, type)
        self.type = type
    def getTypeNor(self):
        return self.type
        
    def modifierNorPui(self, puissance):
        self.getPuissance= puissance 
        
    def modifierNorPoints(self, pointsVie):
        self.getPV = pointsVie
        
    def modifierNorDefense(self, defense):
        self.getDefense = defense
        
    def afficherNor(self):
        print(self.get(), self.getPV(), self.getPuissance(), self.getDefense())
        
        
class PokemonEau(Pokemon):
    def __init__(self, name, puissance, pointsVie, defense, level, type="eau"):
        super().__init__(name, pointsVie, level, type)
        self.type = type
     
    def getTypeau(self):
        return self.type
       
    def modifierEauPui(self, puissance):
        self.getPuissance= puissance 
        
    def modifierEauPui(self, pointsVie):
        self.getPV = pointsVie
        
    def modifierEauPui(self, defense):
        self.getDefense = defense
        
    def affichereau(self):
        print(self.get(), self.getPV(), self.getPuissance(), self.getDefense())
        
        
class PokemonFeu(Pokemon):
    def __init__(self, name, puissance, pointsVie, defense, level, type="feu"):
        super().__init__(name, pointsVie, level, type)
        self.type = type
        
    def getTypeFeu(self):
        return self.type
    
    def modifierFeuPui(self, puissance):
        self.getPuissance= puissance
        
    def modifierFeuPoi(self, pointsVie):
        self.getPV = pointsVie
        
    def modifierFeuDefense(self, defense):
        self.getDefense = defense
        
    def afficherfeu(self):
        print(self.get(), self.getPV(), self.getPuissance(), self.getDefense())
   
   
class PokemonTerre(Pokemon):
    def __init__(self, name, puissance, pointsVie, defense, level, type="terre"):
       super().__init__(name, pointsVie, level, type)
       self.type = type
       
    def getTerType(self):
        return self.type
       
    def modifierTerPui(self, puissance):
        self.getPuissance= puissance
        
    def modifierTerPoint(self, pointsVie):
        self.getPV = pointsVie
        
    def modifierTerDefense(self, defense):
        self.getDefense = defense
        
    def afficherTerre(self):
        print(self.get(), self.getPV(), self.getPuissance(), self.getDefense())

class Combat():
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
    def mortPokemon(self):
        if self.pokemon1.getPV() <= 0:
            print(self.pokemon1.getName(), "est mort")
            return True
        elif self.pokemon2.getPV() <= 0:
            print(self.pokemon2.getName(), "est mort")
            return True
        else:
            return False
        
    def vainqueur(self):
        if self.pokemon1.getPV() > self.pokemon2.getPV():
            return self.pokemon1
        else:
            return self.pokemon2
        
        
    def choisirAttanquant(self):
        rand=random.randint(0,1)
        if rand == 1:
            # self.modifier(self.pokemon1)
            return self.pokemon1
            
        else:
            # self.modifier(self.pokemon2)
            return self.pokemon2
            
            
    def recupere(self):
        
        type_attaque = self.pokemon1.getType()
        type_defense = self.pokemon2.getType()
        puissance_attaque = self.pokemon1.getPuissance()
        
        if type_attaque == "eau" and type_defense == "terre":
            degats = int(puissance_attaque * 0.5)
            print(degats)
            
        elif type_attaque == "feu" and type_defense == "eau":
            degats =int (puissance_attaque * 2)
            print(degats)
        else:
            degats = puissance_attaque
            print(degats)
        return degats  
       
       
    def enleverPV(self, attaquant, defenseur):
        degats = self.recupere()
        defenseur.modifierPV(-degats)
        
        print(attaquant.getName(), "a infligé", degats, "degats à", defenseur.getName())
            
    def perdant(self):
        if self.pokemon1.getPV() < self.pokemon2.getPV():
            return self.pokemon1
        else:
            return self.pokemon2       
           
        
    def enregistrerPokemon(self, pokemon):
        
        try:

# ouvre le fichier users.json en mode lecture et charge son contenu dans la variable data
            with open('pokedex.json') as mon_fichier :
                data = json.load(mon_fichier)
            
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        
        # Chargement des données depuis le fichier "users.json"
        if pokemon in data:
            print("Pokemon déjà existant")

# Ajouter un Pokemon à la liste "data"
        else: 
            data[pokemon.getName()] = pokemon.to_dict()
            data = {'name': pokemon.getName(),'type': pokemon.getType(),'pv': pokemon.getPV(),'puissance': pokemon.getPuissance() ,'defense': pokemon.getDefense(), 'level': pokemon.getLevel()}
            # Ajouter le Pokemon aux données
            
            print("Pokemon ajouté")

# Enregistrer les données dans le fichier "users.json"
        with open('pokedex.json', 'w') as f:
            json.dump(data, f, indent=4)



      
      
    def menu(self):
        print("1 - Attaquer")
        print("2 - Changer de Pokemon") 
        print("3 - Fuir")
        choix = int(input("Que voulez-vous faire ?"))
        
        if choix == "1":
            self.attaquer()
            print("Vous avez attaqué")
             
        elif choix == "2":
            self.changerPokemon()
            print("Vous avez changé de Pokemon")
            
            
        elif choix == "3":
            self.fuir()
            print("Vous avez fui")
            
        else:
            print("Choix incorrect")
            self.menu()
            
    def jouer(self):
        print("le combat commnece !")
        tour= 1
        attaquant = self.choisirAttanquant()
        defenseur = self.pokemon1 if attaquant == self.pokemon2 else self.pokemon2
        while not self.mortPokemon():
            print("Tour", tour)
            print(attaquant)
            print(defenseur)
            self.enleverPV(attaquant, defenseur)
            attaquant, defenseur = defenseur, attaquant
            tour += 1
        
        perdant = self.perdant()
        print("Le vainqueur est", self.vainqueur())
     
    
            
    
pok= Pokemon("pikachu", 10, 1, "eau")
pok1= Pokemon("salameche", 10, 1, "feu")
pokeau= PokemonEau("carapuce", 10, 100, 10, 1)
pokterre= PokemonTerre("bulbizarre", 10, 100, 10, 1)
pokeaux=Combat(pok, pok1)
pokeaux.jouer()
#pokeaux.enregistrerPokemon(pok)
#pokeaux.enregistrerPokemon(pok1)


           