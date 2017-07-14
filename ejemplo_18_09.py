import calculos
import constantes

'''
    Ejemplo 18.9: Calentamiento de un gas ideal diatomico
    
    Dos moles de gas oxigeno se calientan desde una temperatura de 20'C (293K) y una presion de 1 atm a una temperatura
    de 100'C, suponer que el oxigeno es un gas ideal.
    a) ¿Cuanto calor debe suministrarse si el volumen se mantiene constante durante el calentamiento?
    b) ¿Cuanto calor debe suministrarse si la presion permanece constante
    c) ¿Cuanto trabaja realiza el gas en el apartado b) ?

'''

# Datos
temperatura_inicial = 293
presion_inicial = 1
n_moles = 2
temperatura_final = 373


# Qv = Cv * /|T
# Cv = 5/2 * n * R

# Capacidad calorifica a volumen constante
cv = 5/2 * n_moles * constantes.CONSTANTE_GASES_J

# Calor a volumen constante
qv = cv * (temperatura_final-temperatura_inicial)
variacion_temperatura = temperatura_final - temperatura_inicial
qv = calculos.obtener_calor_volumen_constante(cv, variacion_temperatura)

print("1) Calor a volumen constante: " + str(qv) + "J")

# B

# Capacidad calirifica presion constante
cp = cv + n_moles * constantes.CONSTANTE_GASES_J

calor_presion_constante = calculos.obtener_calor_volumen_constante(cp, variacion_temperatura)

print("2) Calor preceso a presion constante: " + str(calor_presion_constante) + "J")

# c) ¿Cuanto trabaja realiza el gas en el apartado b) ?

#trabajo = calculos.