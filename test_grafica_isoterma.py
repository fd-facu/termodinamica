import calculos
import math
import constantes
import grafico_presion_volumen as graph

'''
    la particula realiza un proceso isotermico

    nmoles: 1

    temp: 283k

    Vi= 2

    vf = 6

'''
moles = 0.32

presion_a = 2.4
volumen_a = 2.2
volumen_c = 4.4
presion_c = 1.2

temperatura_c = calculos.obtener_temperatura_gas_ideal(presion_c, volumen_c, moles)

print(temperatura_c)


def generar_puntos(volumen_final, volumen_inicial, presion_inicial, presion_final, cantidad):
    fraccione = (volumen_final - volumen_inicial) / cantidad
    print("Fraccion: " + str(fraccione))
    puntos = []
    puntos.append((volumen_inicial, presion_inicial))
    for x in range(1, cantidad-1):
        volumen = volumen_inicial + fraccione * x

        puntos.append( (volumen, moles * constantes.CONSTANTE_UNIVERSAL_GASES * temperatura_c / (volumen) ))
    puntos.append((volumen_final, presion_final))

    return puntos

puntos = generar_puntos(volumen_a, volumen_c, presion_c, presion_a, 10)

print(puntos)


trabajo_ca = calculos.obtener_trabajo_temperatura_constante(moles, temperatura_c, volumen_a, volumen_c)

trabajo_ca = calculos.convertir_joule_a_atm(trabajo_ca)

print("Trabajo C-A: " + str(trabajo_ca))

energia_ca = 0

calor_ca = energia_ca - trabajo_ca
calor_ca = math.ceil(calor_ca*100)/100

print("Calor C-A: " + str(calor_ca))

print("Energia C-A: " + str(energia_ca))

graph.generar_grafico(puntos, "casa")