# Programa que genere un numero aleatorio del 1 al 100.
# Le pregunte al usuario un numero, y le diga si es mas bajo o mas alto.
import random
rango = []
max = 100 #rango máximo
for i in range (1,max+1):
    rango.append(i)
rand_num = random.choice(rango)
#ESTO MISMO SE PUEDE HACER CON RANDOM.RANDINT
intentos = 5
while intentos > 0:
    choice = int(input(f"Seleciona un número del 1 al {max}. \n Dispones de {intentos} intentos. \n Número: "))
    if 0 < choice <= 100:
        if choice < rand_num:
            print ("Has apuntado demasiado BAJO, inténtalo de nuevo.\n")
            intentos -= 1
        elif choice > rand_num:
            print ("Has apuntado demasiado ALTO, inténtalo de nuevo.\n")
            intentos -= 1
        else:
            print ("ENHORABUENA!!!!, has acertado!.\n")
            break
    else:
        print("Parece que ha habido un error con el valor que has introducido, inténtalo de nuevo.\n")
