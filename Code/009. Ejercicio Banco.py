# Crea una clase para hacer cuentas bancarias
# El constructor tendrá en cuenta el nombre del usuario y el saldo inicial.
# Añade métodos para:
#  - Retirar dinero
#  - Ingresar dinero

import random

class cuenta:
    def __init__(self,name,balance):
        self.titular = name
        self.saldo = balance
        self.iban = self.numero_cuenta

    def retirar(self,cantidad):
        self.saldo -= cantidad
    
    def ingresar(self,cantidad):
        self.saldo += cantidad
    
    def numero_cuenta(self):
        x = ""
        for i in range(20):
            x += random.randint(0,9)
        return x

cuenta_sauca = cuenta("Sauca",100)

while True:
    print(f"BANCO SAUCA")
    print(f"Elija opción:")
    print(f"1. Consultar datos")
    print(f"2. Retirar dinero")
    print(f"3. Ingresar dinero")
    print(f"0. Finalizar sesion")
    opcion = int(input(f"Introduzca opción: "))

    if opcion == 1:
        print(f"Titular: {cuenta_sauca.titular}\nSaldo: {cuenta_sauca.saldo}\nIBAN: {cuenta_sauca.iban}")
    elif opcion == 2:
        x = int(input(f"Dinero a retirar: "))
        cuenta_sauca.retirar(x)
    elif opcion == 3:
        x = int(input(f"Dinero a ingresar: "))
    elif opcion == 0:
        break
    else:
        print(f"Opción no válida.")
cuentas = {"paco":500,"pepe":1000,"maria":900}


for i in cuentas:
    cuenta(nombres[i],saldos[i])