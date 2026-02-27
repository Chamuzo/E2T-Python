# Crea una clase pokemon para llevar un registro de pokemon capturados
# Tendrán nombre, tipo nivel y si estan capturados o no.
# Habrá un contador del numero de pokemon capturados.
from pokelist import pokekanto
from random import choice,randint

class pokemon:
    pokemon_capturados = 0
    pokemon_identificados = 0
    pokedex = []

    def __init__(self,name,poketype,lvl,capturado):
        self.nombre = name
        self.tipo = poketype
        self.nivel = lvl
        self.capturado = capturado
        pokemon.pokedex.append([name,poketype,lvl,capturado])
        
    def capturar(nombre,tipo,nivel):
        pokemon(nombre,tipo,nivel,True)
        pokemon.pokemon_capturados += 1

    def identificar(nombre,tipo,nivel):
        pokemon(nombre,tipo,nivel,False)
        pokemon.pokemon_identificados += 1

    def ver_pokedex(self):
        for i in pokemon.pokedex:
            print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]}")
            print("a")

    @classmethod
    def encontrar(cls):
        print("A")
        aparicion = choice(pokekanto)
        print(choice(pokekanto))
        prob_capt = 40
        lanzamiento_pokebal = randint(0,100)
        aparicion_lvl = randint(21,100)
        if lanzamiento_pokebal <= prob_capt:
            pokemon.capturar(aparicion[0],aparicion[1],aparicion[2],aparicion_lvl)
        else:
            pokemon.identificar(aparicion[0],aparicion[1],aparicion[2],aparicion_lvl)

for i in range(10):
    pokemon.encontrar

pokemon.ver_pokedex
print(pokemon.pokedex)
