# Crea un generador de contraseñas seguras usando los modulos:
#  -random
#  -string
import random
import string

def pass_gen(leng):
    contrasena = ""
    caracter = string.ascii_letters + string.digits + string.punctuation
    for i in range(leng):
        contrasena += random.choice(caracter)
    return(contrasena)
print(pass_gen(1000))

