# Crea una clase pokemon para lelvar un registro de pokemon capturados
#Tendrán nombre, tipo nivel y si estan capturados o no.
# Habrá un contador del numero de pokemon capturados.
class pokemon:
    pokemon_capturados = 0
    pokemon_identificados = 0
    pokedex = []
    def __init__(self,name,poketype,lvl):
        self.nombre = name
        self.tipo = poketype
        self.nivel = lvl
        self.capturado = False
    def capturar(self,nombre,tipo,nivel):
        pokemon(nombre,tipo,nivel)
        nombreD = {nombre,pokemon.capturado}
        pokemon.pokedex.append(nombreD)
        pokemon.capturado = True
        self.pokemon_capturados += 1

    def identificar(self,nombre,tipo,nivel):
        pokemon(nombre,tipo,nivel,False)
        self.pokemon_identificados += 1
        nombreD = {nombre,pokemon.capturado}
        pokemon.pokedex.append(nombreD)

pokemon.capturar("Pikachu","Electrico",21)
pokemon.identificar("Arcanine","Fuego",51)
pokemon.identificar("Moltres","Fuego",87)
pokemon.capturar("Lucario","Lucha",64)

print(pokemon.pokedex)