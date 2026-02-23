# Crea una funcion llamada generar_lista que reciba un numero
# y haga una lista de los numeros impares hasta eso número.
# Al final imprimira por pantalla los números en una sola línea 
# separados por el caracter "|" (AltGr +1)

#Version While
def generar_lista(num):
    lista = []
    x = num
    while x > 0 in range(0,num):
        if x%2 != 0:
            lista.append(x)
        x -= 1
    return lista
print(generar_lista(10))

#Version For
def generar_lista2(num):
    lista = []
    for i in range (0,num+1):
        if i%2 != 0:
            lista.append(i)
print(generar_lista2(10))
