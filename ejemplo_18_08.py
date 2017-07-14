# Ecuacion de los gases ideales: P*V = N*R*T
# T = P*V/(n*R
import calculos
import grafico_presion_volumen as graph
import math

''' 
    Un sistema formado por 0.32 moles de un gas monoatomico con Cv = 3/2RT ocupa un volumen de 2.2l a una presion de
2.4 atm. El sistema describe un ciclo formado por 3 procesos

    1. El gas se calienta a presion constante hasta que su volumen es 4.4L (punto b)
    2. El gas se enfria a volumen constante hasta que la presion disminuye a 1.2 atm (punto c)
    3. El gas esperimenta una compresion isoterma y vuelve al punto a

    A) Cual es la temperatura en los puntos A, B y C?
    B) Determinar W, Q y U para cada proceso y para el ciclo completo '''

# datos del problema
moles = 0.32
volumen_a = 2.2
presion_a = 2.4
volumen_b = 4.4
presion_b = 2.4
volumen_c = 4.4
presion_c = 1.2


temperatura_a = calculos.obtener_temperatura_gas_ideal(presion_a, volumen_a, moles)


print("Temperatura A: " + str(temperatura_a))

temperatura_b = calculos.obtener_temperatura_gas_ideal(presion_b, volumen_b, moles)

print("Temperatura B: " + str(temperatura_b))

temperatura_c = calculos.obtener_temperatura_gas_ideal(presion_c, volumen_c, moles)

print("Temperatura C: " + str(temperatura_c))

trabajo_ab = calculos.obtener_trabajo_presion_constante(2.4,4.4,2.2)

trabajo_ab = calculos.convertir_atm_a_joule(trabajo_ab)

print("Trabajo a-b: " + str(trabajo_ab))

calor_ab = 5/2 * 0.32 * 0.082 * 101.3 * (temperatura_b - temperatura_a)

print("Calor a-b: " + str(calor_ab))

energia_ab = calor_ab + trabajo_ab

print("Energia a-b: " + str(energia_ab))

# Proceso B-C

# El trabajo a volumen constante siempre es cero.
trabajo_bc = 0

print("Trabajo B-C: " + str(trabajo_bc))

# C = Cv * (Tf - Ti) / Cv = 3/2 * n * R / Cp = 5/2 * n * R
calor_bc = 3/2 * moles * 0.082 * 101.3 * (temperatura_c - temperatura_b)

print("Calor B-C: " + str(calor_bc))

energia_bc = calor_bc + trabajo_bc

print("Energia B-C: " + str(energia_bc))

# Proceso C-A

trabajo_ca = calculos.obtener_trabajo_temperatura_constante(moles, temperatura_c, 2.2, 4.4)

print("Trabajo C-A: " + str(trabajo_ca))

energia_ca = 0

calor_ca = energia_ca - trabajo_ca
calor_ca = math.ceil(calor_ca*100)/100

print("Calor C-A: " + str(calor_ca))

print("Energia C-A: " + str(energia_ca))


puntos_isoterma = graph.generar_puntos_isoterma(moles, volumen_a, volumen_c, presion_a, presion_c, 20, temperatura_c)

lista = [(presion_a, volumen_a), (presion_b, volumen_b)]

for punto in puntos_isoterma:
    lista.append(punto)


trabajo_total = trabajo_ab + trabajo_bc + trabajo_ca
energia_total = energia_ab + energia_bc + energia_ca
calor_total = calor_ab + calor_bc + calor_ca
# Redondeamos a 3 decimales usando la libreria math


datos = " Energia total: " + str(math.ceil(energia_total*1000)/1000) + '\n Calor total: ' + str(math.ceil(calor_total*1000)/1000) + \
        '\n Trabajo total: ' + str(math.ceil(trabajo_total*1000)/1000)

print(datos)
graph.generar_grafico(lista, datos)

