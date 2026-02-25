# Haz un videojuego usando clases
# Clase personaje (nombre, vida y funcion de ataque)
# Jugador y enemigo son personaje y atacan por turnos
# Gana quien deje la vida del otro a 0.
import random
class Personaje:
    def __init__(self,alias,hp,power):
        self.nombre = alias
        self.vida = hp

    def atacar(self):
        return random.randint(0,15)

jugador = Personaje("Jugador",50)
enemigo = Personaje("Enemigo",20)
orden = [jugador,enemigo]
random.shuffle(orden)
while jugador.vida > 0 and enemigo.vida > 0:
    orden[0].vida -= ataque
    print(f"{orden[0].nombre} ha atacado a {orden[1].nombre} causandole {ataque} puntos de daño.")
    ataque = random.randint(0,15)
    orden[1].vida -= ataque
    print(f"{orden[1].nombre} ha atacado a {orden[0].nombre} causandole {ataque} puntos de daño.")
if jugador.vida >= 0:
    print(f"{jugador.nombre} ha vencido a {enemigo.nombre}")
else:
    print(f"{enemigo.nombre} ha vencido a {jugador.nombre}")

     

