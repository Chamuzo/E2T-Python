# Escribe una funcion llamada calcular_imc que reciba el peso (kg)
# y la altura (m). La funcion devolverá el índice de Masa Corporal @ (IMC * peso / altura^2).
# - Si el IMC es menor que 18.5, "Bajo peso".
# - Entre 18.5 y menor que 25, "Normal".
# - Entre 25 y menor que 30, "Sobrepeso".
# - 30 o más, Obesidad"

def calcula_imc(kg,m): #Creamos función
    IMC = kg / m**2
    if IMC < 18.5:
        return(IMC,"Bajo peso")
    elif 18.5 <= IMC < 25:
        return(IMC,"Normal")
    elif 25 <= IMC < 30:
        return(IMC,"Sobrepeso")
    elif 30 <= IMC:
        return(IMC,"Obesidad")
    else:
        return("ERROR")

peso = float(input("Introduzca peso(kg):"))
altura = float(input("Introduzca altura(m):"))

print (f" Peso: {peso} \n ALtura: {altura} \n IMC: {calcula_imc(peso,altura)}")