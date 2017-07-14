import calculos
import constantes

'''Transformacion de hielo en vapor

¿Cuanto calor es necesario suministrar para transformar 1,5kg de hielo en 253K y 1 atm en vapor
'''

# Datos

masa_hielo = 1.5  # en kg
calor_especifico_hielo = 2.05  # En kJ/kg
temperatura_inicial_hielo = 253  # En K


# 1. Elevar la temperatura del hielo DE 253K(-20C') a 273K (0C')

variacion_temperatura_1 = 273 - temperatura_inicial_hielo
calor_1 = calculos.obtener_calor(1.5, constantes.CALOR_ESPECIFICO_HIELO, variacion_temperatura_1)

print(str(calor_1))

# 2. Fundir el hielo a 273K en agua

calor_2 = calculos.calor_de_cambio_fase(masa_hielo, constantes.CALOR_LATENTE_FUSION_AGUA)

print(str(calor_2))

# 3. Elevar la temperatura del agua de 273K a 373K

variacion_temperatura_3 = 100
calor_3 = calculos.obtener_calor(masa_hielo, constantes.CALOR_ESPECIFICO_AGUA, variacion_temperatura_3)

print(str(calor_3))

# 4. Vaporizar el agua aa 373K

calor_4 = calculos.calor_de_cambio_fase(masa_hielo, constantes.CALOR_LATENTE_VAPORIZACION_AGUA)

print(str(calor_4))

# 5. Calor total del proceso

calor_total = calor_1 + calor_2 + calor_3 + calor_4

print(calor_total)

''' Opcional:

Un ttrozo de plomo de 830g se calienta hasta su punto de fusion de 600k ¿ Cuanta energia
calorica adicional debe añadirsse para fundir el plomo?
'''



# Opcional, generar grafico de calor en funcion del tiempo si el calor
# se adiciona a un kJ por segundo