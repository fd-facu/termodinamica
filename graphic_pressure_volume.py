import matplotlib.pyplot as plt
import constants as consts
import calculations as calc

plt.xlabel('Volumen')
plt.ylabel('Presion')
plt.title('Grafico PV')


def generar_grafico(lista_etapas, datos = None):
    instancia_presion = []
    instancia_volumen = []

    if datos is not None:
        plt.annotate(datos, (0, 0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')

    for tupla in lista_etapas:

        instancia_presion.append(tupla[0])
        instancia_volumen.append(tupla[1])

    print("Volumenes" + str(instancia_volumen))
    print("Presiones" + str(instancia_presion))
    plt.plot(instancia_volumen, instancia_presion) # x, y

    plt.show()


# Create points to repesent an isometric process curve
def generar_puntos_isoterma(n_moles, final_volume, initial_volume, final_pressure, initial_pressure, quantity, temperature):
    print("Entro en generar puntos isoterma.")
    fraction = (final_volume - initial_volume) / quantity
    print("Fraction: " + str(fraction))
    points = []
    points.append((initial_pressure, initial_volume))
    for x in range(1, quantity-1):
        volume = initial_volume + fraction * x

        points.append( (n_moles * consts.IDEAL_GAS_CONSTANT_L_ATM * temperature / (volume) ,volume))
    points.append((final_pressure, final_volume))

    print("Isometric process points: " + str(points))

    return points


def generar_puntos_adiabatica(presion_final, presion_inicial, volumen_final, volumen_inicial, es_monoatomico, cantidad):
    print("Entro en generar puntos adiabatica.")
    delta = 5/3
    if es_monoatomico:
        delta = 5/3
    else:
        delta = 1.4

    fraccion = (volumen_final - volumen_inicial) / cantidad
    print("Fraccion: " + str(fraccion))
    puntos = []
    puntos.append((presion_inicial, volumen_inicial))
    for x in range(1, cantidad - 1):
        volumen = volumen_inicial + fraccion * x

        puntos.append((calc.obtener_presion_final(presion_inicial, volumen, volumen_inicial, delta), volumen))
    puntos.append((presion_final, volumen_final))

    print("Puntos de la adiabatica: " + str(puntos))

    return puntos


