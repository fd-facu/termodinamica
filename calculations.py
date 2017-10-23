
#import  grafico_temp_calor as graft
import constantes as const
import math
# pag 521 tipler


# Devuelve el calor necesario para elevar la temperatura de una sustancia a una temp especifica
def obtener_calor(masa, calor_espacifico, variacion_temperatura):
    return masa * calor_espacifico * variacion_temperatura


def obtener_capacidad_calorifica(masa, calor_especifico):
    return masa * calor_especifico


def obtener_temperatura_final(calor, masa, calor_especifico, temperatura_inicial):
    return (calor/(masa*calor_especifico)) + temperatura_inicial

calor_ejemplo = obtener_calor(3, const.CALOR_ESPECIFICO_COBRE, 20)


# Trabajo a presion constante(Isobara)
def obtener_trabajo_presion_constante(presion, volumen_final, volumen_inicial):
    return (-1) * presion * (volumen_final-volumen_inicial)

# NO EXISTE TRABAJO EN UN PROCESO A VOLUMEN CONSTANTE


# Trabajo a temperatura constante(Isotermico)
def obtener_trabajo_temperatura_constante(n_moles, temperatura, volumen_final, volumen_inicial):
    return n_moles * const.CONSTANTE_UNIVERSAL_GASES_J * temperatura * math.log(volumen_inicial / volumen_final)


#Temperatura gas ideal en Kelvin
def obtener_temperatura_gas_ideal(presion, volumen, n_moles):
    return (presion * volumen) / (n_moles * const.CONSTANTE_UNIVERSAL_GASES)


# CAPITULO 18.6: CAPACIDADES CALORIFICAS DE LOS GASES

def obtener_calor_volumen_constante(capacidad_calorifica, variacion_temperatura):
    return capacidad_calorifica * variacion_temperatura

# CAPITULO 18.9: Compresion adiabatica cuasiestatica del aire

def obtener_delta(cp, cv):
    return cp / cv

def obtener_presion_final(presion_inicial, volumen_final, volumen_inicial, delta):
    return presion_inicial * ((volumen_inicial / volumen_final)**delta)

def trabajo_proceso_adiabatico(cv, temperatura_final, temperatura_inicial):
    return cv * (temperatura_final - temperatura_inicial)


def trabajo_proceso_adiabatico_pv(presion_final, volumen_final, presion_inicial, volumen_inicial, delta):
    return ((presion_final * volumen_final)-(presion_inicial * volumen_inicial)) /(delta - 1)


# Conversiones
def convertir_caloria_a_joule(valor_en_cal):
    return valor_en_cal * 4.18


def convertir_joule_a_caloria(valor_en_joule):
    return valor_en_joule / 4.18


def convertir_celcius_a_kelvin(valor_en_celcius):
    return valor_en_celcius + 273.15


def convertir_kelvin_a_celcius(valor_en_kelvin):
    return valor_en_kelvin - 273.15


def convertir_atm_a_joule(valor_en_atm):
    return valor_en_atm * 101.3


def convertir_joule_a_atm(valor_en_joule):
    return valor_en_joule / 101.3





#print("Calar necesario para elevar 3kg de cobre en 20k: " + str(calor_ejemplo))

# CALORIMETRIA

# Calor latente

# Ejemplo 18.3


def calor_de_cambio_fase(masa,calor_latente):
    return masa * calor_latente

# Hacer grafico Temperatura/Tiempo(1kJ/s)

# q1 = obtener_calor(1500, 2.05, 273+293)

'''q1 = 61.5

q2 = 500

q3 = 627

q4 = 3390

qtotal = q1 + q2 + q3 + q4

lista_q = [q1, q2, q3, q4]

lista_fases = [(0, 253), (q1, 273), (q2, 273), (q3, 373), (q4, 373)]

# print("Calor realizado total: " + str(qtotal))'''

# graft.generar_grafico(lista_fases)

