from pokemon import Pokemon
from random import randint
from type import *
from recognition.API import SearchCard, CameraPhotoTexte, SearchPokemon



txt = CameraPhotoTexte()
print(txt)
carte = SearchCard(txt)
pokemon = SearchPokemon(txt)
# Pokemon1 = Pokemon("Dracaufeu", 300, Type.FEU, 250, "Growl", 5, Type.NORMAL, "Ember", 20, Type.FEU)
# Pokemon2 = Pokemon("Tortank", 350, Type.EAU, 100, "Head butt", 10, Type.NORMAL, "Water Canon", 25, Type.EAU)
Pokemon1 = Pokemon(carte.name, int(carte.hp), Def_types(pokemon.types[0]), 0, carte.attacks[0].name, int(carte.attacks[0].damage), Def_types(pokemon.types[0]), carte.attacks[0].name, int(carte.attacks[0].damage), Def_types(pokemon.types[0]))

txt = CameraPhotoTexte()
carte = SearchCard(txt)
pokemon = SearchPokemon(txt)
Pokemon2 = Pokemon(carte.name, int(carte.hp), Def_types(pokemon.types[0]), 0, carte.attacks[0].name, int(carte.attacks[0].damage), Def_types(pokemon.types[0]), carte.attacks[0].name, int(carte.attacks[0].damage), Def_types(pokemon.types[0]))

print(Pokemon1.type)

nbTours = 0
while Pokemon1.is_alive() and Pokemon2.is_alive():
    nbTours += 1
    print('---------------------------')
    print("Début du tours  :  ", nbTours)
    print('---------------------------')
    ########################################################   CHOIX DES ATTAQUES   ########################################################
    numAtkPoke1 = int(input(f"Numéro de l'attaque choisie pour {Pokemon1.nom} :  (1) {Pokemon1.atkNom[0]}  (2) {Pokemon1.atkNom[1]} ")) - 1
    numAtkPoke2 = int(input(f"Numéro de l'attaque choisie pour {Pokemon2.nom} :  (1) {Pokemon2.atkNom[0]}  (2) {Pokemon2.atkNom[1]} ")) - 1
    while numAtkPoke1 != 0 and numAtkPoke1 != 1:
        numAtkPoke1 = int(input(f"Numéro de l'attaque choisie pour {Pokemon1.nom} :  (1) {Pokemon1.atkNom[0]}  (2) {Pokemon1.atkNom[1]} ")) - 1
    while numAtkPoke2 != 0 and numAtkPoke2 != 1:
        numAtkPoke2 = int(input(f"Numéro de l'attaque choisie pour {Pokemon2.nom} :  (1) {Pokemon2.atkNom[0]}  (2) {Pokemon2.atkNom[1]} ")) - 1   

    if randint(1,2) == 1: # CHOI DU JOUEUR PRIORITAIRE
        ########################################################   ATTAQUE DES POKEMONS   ######################################################## 
        Pokemon2.DamageTaken(Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type))
        print(f"{Pokemon1.nom} attaque {Pokemon2.nom} de ",Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type) , f"      {Pokemon2.nom} a encore  : ", Pokemon2.hp)
        if not (Pokemon2.is_alive()):
            print(f"{Pokemon2.nom} fainted")
            print('---------------------------')
            break
        Pokemon1.DamageTaken(Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type))
        print(f"{Pokemon2.nom} attaque {Pokemon1.nom} de ",Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type) , f"      {Pokemon1.nom} a encore  : ", Pokemon1.hp)
        if not (Pokemon1.is_alive()):
            print(f"{Pokemon1.nom} fainted")
            print('---------------------------')
            break
    else:
        ########################################################   ATTAQUE DES POKEMONS   ########################################################
        Pokemon1.DamageTaken(Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type))
        print(f"{Pokemon2.nom} attaque {Pokemon1.nom} de ",Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type) , f"      {Pokemon1.nom} a encore  : ", Pokemon1.hp)
        if not (Pokemon1.is_alive()):
            print(f"{Pokemon1.nom} fainted")
            print('---------------------------')
            break
        Pokemon2.DamageTaken(Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type))
        print(f"{Pokemon1.nom} attaque {Pokemon2.nom} de ",Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type) , f"      {Pokemon2.nom} a encore  : ", Pokemon2.hp)
        if not (Pokemon2.is_alive()):
            print(f"{Pokemon2.nom} fainted")
            print('---------------------------')
            break

    
if Pokemon1.is_alive():
    print(f"{Pokemon1.nom} gagne ce combat !!")
else:
    print(f"{Pokemon2.nom} gagne ce combat !!")

    


