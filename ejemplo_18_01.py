import calculos
import math

# Datos del problema
masa_cobre = 3  # En kg
calor_especifico_cobre = 0.386  # en kJ/kg
variacion_temperatura = 20  # En K

resultado = calculos.obtener_calor(masa_cobre, calor_especifico_cobre, variacion_temperatura)
# Redondeo el resultado a 2 decimales

resultado = math.ceil(resultado*100)/100
print("Se necesita " + str(resultado) + " kJ de calor para elevar la temperatura del cobre 20K")
