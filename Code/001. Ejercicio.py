def calcula_imc(peso,altura):
    IMC = peso / altura*altura
    if IMC < 18.5:
        return("Bajo peso")
    elif 18.5 <= IMC < 25:
        return("Normal")
    elif 25 <= IMC < 30:
        return("Sobrepeso")
    elif 30 <= IMC:
        return("Obesidad")
    else:
        return("ERROR")

print(calcula_imc(100,176))