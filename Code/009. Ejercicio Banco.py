# Crea una clase para hacer cuentas bancarias
# El constructor tendrá en cuenta el nombre del usuario y el saldo inicial.
# Añade métodos para:
#  - Retirar dinero
#  - Ingresar dinero

class cuenta:
    def __init__(self,user,balance):
        self.usuario = user
        self.saldo = balance

    def retirar(self):
        retirada = int(input("Indique el importe a retirar: "))
        return retirada

    def ingresar(self):
        ingreso = int(input("Indique la cantidad a ingresar: "))
        return ingreso
while True:
    cuentaA = cuenta("jonatan",50900)
    cuentaB = cuenta("hugo",500)
    seleccionCuenta = int(input(f"Seleccione una cuenta:\n \n 1. cuentaA. Saldo = {cuentaA.saldo} \n 2. cuentaB. Saldo = {cuentaB.saldo} \n \n 0. Finalizar sesión \n Selección: "))
    if seleccionCuenta == 1:
        cuentaSeleccionada = cuentaA
    elif seleccionCuenta == 2:
        cuentaSeleccionada = cuentaB
    elif seleccionCuenta == 0:
        print(f"Cerrando sesion")
        break
    else:
        print("ERROR. Selección incorrecta")

    accion = int(input(f"Eliga una opcion :\n \n 1. RETIRAR EFECTIVO \n 2. INGRESAR EFECTIVO \n \n 0. Finalizar sesión \n Selección: "))
    if accion == 1:
        retirada = cuentaSeleccionada.retirar
        saldo = cuentaSeleccionada.saldo
        prev = saldo - retirada
        if prev >= 0:
            cuentaSeleccionada.saldo -= retirada
            print("Retirada realizada. Su saldo actual es {cuenta.saldo}")
        else:
            print ("ERROR. SALDO INSUFICIENTE. TRABAJA!")
    elif accion == 2:
        ingreso = cuentaSeleccionada.ingresar
        cuentaSeleccionada.saldo += cuentaSeleccionada.ingresar
        print(f"Ingreso realizado \n Su saldo asciende a {cuentaSeleccionada.saldo}")
    elif accion == 0:
        print(f"Cerrando sesion")
        break
    else:
        print("ERROR. Seleccione una acción correcta.")