# Ejercicio de proceso adiabatico
# Proceso donde no existe flujo de calor
# delta = Cp / Cv
# T*V^(delta - 1) = Cte
# P*V^(delta) = cte
# Trabajo en proceso adiabatico = Cv * /|T
# Trabajo en proceso adiabatico en funcion de P y de V =

# Cv: Capacidad calorifica a volumen constante.
# Cp: Capacidad calorifica a presion constante.
# Cp para gas ideal: Cv + n*R
# Cv para gas ideal monoatomico: 3/2 * n*R
# Cv para gas ideal diatomico: 5/2 * n*R

import calculos as calc
import constantes
import grafico_presion_volumen as graph

'''
    Una cantidad de aire se comprime adiabaticamente y cuasiestaticamente desde una presion inicial de 1 atm y volumen
    a 4L a la temperatura de 20'C hasta la mitad de su volumen original
    
    A) ¿Cual es la presion final?
    B) ¿Cual es la temperatura final?
    c) ¿Cual es el trabajo realizado sobre el gas?
    
    
'''

# datos

presion_inicial = 1 # En atm
volumen_inicial = 4 # En litros
temperatura_inicial = 293 # En Kelvin
volumen_final = 2

# a) Buscar presion final

cv = 5/2
cp = 5/2 + 1
delta = calc.obtener_delta(cp, cv)

presion_final = calc.obtener_presion_final(presion_inicial, volumen_final, volumen_inicial, delta)

# B) Buscar temperatura final

temperatura_final = temperatura_inicial * (volumen_inicial/volumen_final) ** (delta-1)

# C) Trabajo realizado sobre el gas

trabajo = calc.trabajo_proceso_adiabatico_pv(presion_final, volumen_final, presion_inicial, volumen_inicial, delta)

print("Valor del delta: " + str(delta))
print("Presion final: " + str(presion_final))
print("Temperatura final: " + str(temperatura_final))
print("Trabajo realicado sobre el gas: " + str(calc.convertir_atm_a_joule(trabajo)))

''' otra forma de hacer el punto c

nr = presion_inicial * volumen_inicial / temperatura_inicial

cv2 = 5/2 * nr

trabajo2 = calc.trabajo_proceso_adiabatico(cv2, temperatura_final, temperatura_inicial)

print("trabajo2: " + str(calc.convertir_atm_a_joule(trabajo2)))'''

print("Generande grafico")

diferencia_volumen = volumen_final-volumen_inicial

n_moles = (presion_inicial* volumen_inicial) / (temperatura_inicial * constantes.CONSTANTE_GASES_L_ATM)
print("n_moles : " + str(n_moles))

cantidad = 30
fraccion = diferencia_volumen / cantidad
print("Fraccion: " + str(fraccion))
puntos = []
puntos.append((presion_inicial, volumen_inicial))
for x in range(1, cantidad-1):
    volumen = volumen_inicial + (fraccion * x)

    puntos.append( (calc.obtener_presion_final(presion_inicial, volumen, volumen_inicial, delta), volumen))
puntos.append((presion_final, volumen_final))

puntos2 = graph.generar_puntos_adiabatica(presion_final, presion_inicial, volumen_final, volumen_inicial, False, 30)

#graph.generar_grafico(puntos, "")
graph.generar_grafico(puntos2, "")
print("Puntos de la curva adiabatica: " + str(puntos))
print("Puntos de la curva adiabatica: " + str(puntos2))
