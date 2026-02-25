#Crear calculadora de edad
dias_mes = (0,31,28,31,30,31,30,31,31,30,31,30,31)
import datetime
ano = int(1992)
mes = int(6)
dia = int(7)
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
    n_month += 1
    dias_pre += dias_mes[i]
dias_hoy = dias_mes[hoy.month]
for i in range(fecha_nac.month+1,13):
    n_month += 1
    dias_hoy += dias_mes[i]
print(n_month)
print(dias_hoy)


    

            


print(año_bisiesto)
print(año_normal)