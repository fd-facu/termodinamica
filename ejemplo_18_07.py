import calculos
import grafico_presion_volumen as graph


trabajo_ab = calculos.obtener_trabajo_presion_constante(2,2.5,1)

trabajo_ab = calculos.convertir_atm_a_joule(trabajo_ab)

print("Trabajo proceso A-B: " + str(trabajo_ab) + "J")

trabajo_bc = 0

print("Trabajo proceso B-C: " + str(trabajo_bc) + "J (Volumen constante)")

trabajo_cd = calculos.obtener_trabajo_presion_constante(1, 1, 2.5)

trabajo_cd = calculos.convertir_atm_a_joule(trabajo_cd)

print("Trabajo proceso C-D: " + str(trabajo_cd) + "J")

trabajo_da = 0

print("Trabajo proceso D-A: " + str(trabajo_da) + "J (Volumen constante)\n")

trabajo_total = trabajo_ab + trabajo_bc + trabajo_cd + trabajo_da

# Variacion de energia interna: /|U = Q + W

# Calor añadido: Q = /|U - W

variacion_energia = 0

calor_añadido = variacion_energia - trabajo_total

print("Trabajo total: " + str(trabajo_total) + " J")
print("Calor añadido: " + str(calor_añadido) + " J")

lista_etapas = [(1, 2), (2.5, 2), (2.5, 1), (1, 1), (1, 2)]

graph.generar_grafico(lista_etapas)
