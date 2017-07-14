import matplotlib.pyplot as plt



plt.ylabel('Temperatura (K)')
plt.xlabel('Tiempo (seg)')
plt.title('Grafico PV')


def generar_grafico(lista_etapas):
    instancia_x = []
    instancia_y = []

    for tupla in lista_etapas:
        instancia_x.append(tupla[0])
        instancia_y.append(tupla[1])

    plt.plot(instancia_x, instancia_y)

    plt.show()

# Test
#generar_grafico()