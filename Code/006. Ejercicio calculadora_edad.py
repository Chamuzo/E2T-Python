#Crear calculadora de edad
dias_mes = (0,31,28,31,30,31,30,31,31,30,31,30,31)
meses_nac = []
meses_hoy = []
import datetime
ano = int(1992)
mes = int(1)
dia = int(1)
fecha_nac = datetime.date(ano,mes,dia)
hoy = datetime.date.today()
d = (hoy-fecha_nac).days
año_normal = 0
año_bisiesto = 0
month_days = 0
for i in range (fecha_nac.year+1,hoy.year):
    if i%4 == 0 or (i%100 == 0 and i%400 == 0):
        año_bisiesto += 1
    else:
        año_normal += 1
dias_medio = año_bisiesto*366 + año_normal*365
dias_pre = dias_mes[fecha_nac.month] - fecha_nac.day
n_month = 0
for i in range(fecha_nac.month+1,13):
    meses_nac.append(i)
    dias_pre += dias_mes[i]
dias_hoy = dias_mes[hoy.month]
for i in range(1,hoy.month):
    meses_hoy.append(i)
    dias_hoy += dias_mes[i]
print(dias_hoy)
años_total = año_bisiesto + año_normal
if (len(meses_nac)+len(meses_hoy)) >= 12:
    for i in meses_nac:
        if i in meses_hoy:


#####################
# Días por mes, index 1 = enero, 12 = diciembre
dias_mes = (0,31,28,31,30,31,30,31,31,30,31,30,31)

# Fecha de nacimiento
ano_nac = 1992
mes_nac = 1
dia_nac = 1

# Fecha actual
import datetime
hoy = datetime.date.today()
ano_hoy = hoy.year
mes_hoy = hoy.month
dia_hoy = hoy.day

# Ajuste por años bisiestos
def es_bisiesto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Ajustar febrero si es bisiesto
def dias_en_mes(mes, ano):
    if mes == 2 and es_bisiesto(ano):
        return 29
    else:
        return dias_mes[mes]

# Calcular días
if dia_hoy >= dia_nac:
    dias = dia_hoy - dia_nac
else:
    # Tomamos días del mes anterior
    if mes_hoy == 1:
        mes_anterior = 12
        ano_anterior = ano_hoy - 1
    else:
        mes_anterior = mes_hoy - 1
        ano_anterior = ano_hoy
    dias = dia_hoy + dias_en_mes(mes_anterior, ano_anterior) - dia_nac
    mes_hoy -= 1
    if mes_hoy == 0:
        mes_hoy = 12
        ano_hoy -= 1

# Calcular meses
if mes_hoy >= mes_nac:
    meses = mes_hoy - mes_nac
else:
    meses = mes_hoy + 12 - mes_nac
    ano_hoy -= 1

# Calcular años
años = ano_hoy - ano_nac

print(f"Tienes {años} años, {meses} meses y {dias} días.")
