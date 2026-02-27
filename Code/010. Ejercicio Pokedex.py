# Crea una clase pokemon para llevar un registro de pokemon capturados
# Tendrán nombre, tipo nivel y si estan capturados o no.
# Habrá un contador del numero de pokemon capturados.
from pokelist import pokekanto
from random import choice,randint
from tabulate import tabulate
class pokemon:
    pokemon_capturados = 0
    pokemon_identificados = 0
    pokedex = []

    def __init__(self,name,poketype,lvl,capturado):
        self.nombre = name
        self.tipo = poketype
        self.nivel = lvl
        self.capturado = capturado
        # Si existia en la pokedex, pero ahora lo capturamos, actualizamos campo Capturado.
        for i in pokemon.pokedex:   
            if name in i:
                pokemon.pokedex[i,3] = True
        pokemon.pokedex.append([name,poketype,lvl,capturado])
        
    def capturar(nombre,tipo,nivel):
        pokemon(nombre,tipo,nivel,True)
        pokemon.pokemon_capturados += 1

    def identificar(nombre,tipo,nivel):
        pokemon(nombre,tipo,nivel,False)
        pokemon.pokemon_identificados += 1

    def lanzar_pokeball(self):
        return randint(0,100)

    def encontrar(poke,lvl):
        prob_capt = 40
        if pokemon.lanzar_pokeball <= prob_capt:
            pokemon.capturar(aparicion[0],aparicion[1],lvl)
        else:
            pokemon.identificar(aparicion[0],aparicion[1],lvl)

    def ver_pokedex(self):
        print(tabulate(pokemon.pokedex,headers=["Nombre","Tipo","Nivel","Capturado"], tablefmt="grid"),end="\r")

for i in range(5):
    aparicion = choice(pokekanto)
    a = pokemon.pokedex
    b = "Hola"
    print(f"{a:<25}")
    
