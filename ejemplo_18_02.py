import  calculos

# Datos
masa_plomo = 0.6 # En kg
temperatura_inicial_plomo = 373 # En K
masa_recipiente_aluminio = 0.2
calor_especifico_aluminio = 0.9 # En kJ/kg * K
masa_agua = 0.5
calor_especifico_agua = 4.18
temperatura_inicial_agua = 290.3
temperatura_final_sistema = 293

# Se busca el calor especifico del plomo

variacion_temperatura_agua = temperatura_final_sistema - temperatura_inicial_agua
calor_agua = masa_agua * calor_especifico_agua * variacion_temperatura_agua
variacion_temperatura_recipiente = temperatura_final_sistema - temperatura_inicial_agua
calor_recipiente = masa_recipiente_aluminio * calor_especifico_aluminio * variacion_temperatura_recipiente

calor_especifico_cobre = (calor_agua + calor_recipiente) / (masa_plomo * (temperatura_inicial_plomo- temperatura_final_sistema))

print("Resulado: " + str(calor_especifico_cobre))