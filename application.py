# Importando librerias de python
# Presion final para adiabatica ejemplo: 2.64
import sys
print("Iniciando aplicacion...\n")
from matplotlib import pyplot as plt
if sys.version_info[0] < 3:
    import Tkinter as tk
    import tkFont as tkfont
else:
    import tkinter as tk
    from tkinter import font as tkfont

# Importanto archivos propios.
import calculos as calc
import grafico_presion_volumen as graf


# Cada pagina esta representada en una clase
# el sampleApp seria el main


class Aplicacion(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        self.menu = tk.Menu(container.master)

        container.master.config(menu=self.menu)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.help = tk.Menu(self.menu)
        self.help.add_command(label='Ayuda', command=self.create_help_window)
        self.help.add_command(label="Acerca de")
        self.menu.add_cascade(label="Ayuda", menu=self.help)

        self.frames = {}
        for F in (MenuPrincipal, MenuCalculos, MenuConversiones, CalculoCalor, CalculoCalorLatente, ConversionCelcius, CalculoTemperatura,
                CalculoTrabajoPresionConstante, CalculoTrabajoTemperaturaConstante, Grafico):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.title("Aplicacion Termodinamica")
        self.geometry("800x450")
        self.show_frame("MenuPrincipal")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def create_help_window(self):

        texto = "Primer principio de termodinamica: /|U = Q + W \n\n Constantes Importantes: \n\n Conversion de atm l a J: 1 atm*L = 101.3J \n Constante universal de los gases = 0.082 atm * L | 8.314J \n Calor latente de fusion agua: 333,5 kJ/kg \n Calor latenete de valorizacion agua: 2257 kJ/kg \n Ecuacion de equilibrio: PV=nRT \n Trabajo realizado en una compresion isoterma: W= nRT Ln(vi/vf) \n Capacidad calorifica del gas a volumen constante(gas ideal monoatomico): Cv = 3/2 nR\n Capacidad calorifica del gas a volumen constante(gas ideal diatomico): Cv = 5/2 nR \n Capacidad calorifica del gas a presion constante: Cp = Cv + nR"

        t = tk.Toplevel(self)
        t.wm_title("Titulo")
        l = tk.Label(t, text=texto)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)


class MenuPrincipal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Menu Principal", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Calculos", command=lambda: controller.show_frame("MenuCalculos"))
        button2 = tk.Button(self, text="Conversiones", command=lambda: controller.show_frame("MenuConversiones"))
        button3 = tk.Button(self, text="Grafico", command=lambda: controller.show_frame("Grafico"))
        button4 = tk.Button(self, text="Salir", command=quit)

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


class MenuCalculos(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Seleccione el calculo que desea realizar", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Calculo Calor(Q) ", command=lambda: controller.show_frame("CalculoCalor"))
        button2 = tk.Button(self, text="Calculo Calor cambio de fase", command=lambda:
                controller.show_frame("CalculoCalorLatente"))
        button3 = tk.Button(self, text="Calculo Temperatura", command=lambda:
                controller.show_frame("CalculoTemperatura"))
        button4 = tk.Button(self, text="Calculo Trabajo presion constante ",
                command=lambda: controller.show_frame("CalculoTrabajoPresionConstante"))
        button5 = tk.Button(self, text="Calculo trabajo temperatura constante",
                command=lambda: controller.show_frame("CalculoTrabajoTemperaturaConstante"))
        return_button = tk.Button(self, text="Volver", command=lambda: controller.show_frame("MenuPrincipal"))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        return_button.pack()


class CalculoCalor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.texto_resultado = tk.Label(self, text="", fg="blue")

        label = tk.Label(self, text="Complete los datos requeridos", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        texto_masa = tk.Label(self, text="Masa(en kg)")
        entrada_masa = tk.Entry(self)

        texto_calor_especifico = tk.Label(self, text="Calor especifico(En kJ/kg*K)")
        entrada_calor_especifico = tk.Entry(self)

        texto_temperatura = tk.Label(self, text="Temperatura en (En K)")
        entrada_temperatura = tk.Entry(self)

        button1 = tk.Button(self, text="Calcular",
                            command=lambda: self.obtener_calor(entrada_masa.get(), entrada_calor_especifico.get(), entrada_temperatura.get()))

        self.texto_resultado = tk.Label(self, text="", fg="blue")
        return_button = tk.Button(self, text="Volver", command=lambda: controller.show_frame("MenuPrincipal"))

        texto_masa.pack()
        entrada_masa.pack()
        texto_calor_especifico.pack()
        entrada_calor_especifico.pack()
        texto_temperatura.pack()
        entrada_temperatura.pack()
        button1.pack()
        self.texto_resultado.pack()
        return_button.pack()

    def obtener_calor(self, masa, calor_especifico, temperatura):

        resultado = calc.obtener_calor(float(masa), float(calor_especifico), float(temperatura))
        self.texto_resultado["text"] = "Q total: " + str(resultado)+" kJ"


class CalculoCalorLatente(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Complete los datos requeridos", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        texto_masa = tk.Label(self, text="Masa(en kg)")
        entrada_masa = tk.Entry(self)

        texto_calor_latente = tk.Label(self, text="Calor latente fusion/vaporizacion(En kJ/kg*K)")
        entrada_calor_latente = tk.Entry(self)

        button1 = tk.Button(self, text="Calcular",
                            command=lambda: self.obtener_calor_latente(entrada_masa.get(), entrada_calor_latente.get()))

        self.texto_resultado = tk.Label(self, text="", fg="blue")
        return_button = tk.Button(self, text="Volver", command=lambda: controller.show_frame("MenuPrincipal"))

        texto_masa.pack()
        entrada_masa.pack()
        texto_calor_latente.pack()
        entrada_calor_latente.pack()
        button1.pack()
        self.texto_resultado.pack()
        return_button.pack()

    def obtener_calor_latente(self, masa, calor_latente):

        resultado = calc.calor_de_cambio_fase(float(masa), float(calor_latente))
        self.texto_resultado["text"] = "Q total: " + str(resultado)+" kJ"


class ConversionCelcius(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            label = tk.Label(self, text="Complete los datos requeridos", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)

            texto_celcius = tk.Label(self, text="Temperatura(en Celcius)")
            entrada_celcius = tk.Entry(self)

            button1 = tk.Button(self, text="Calcular",
                                command=lambda: self.obtener_temperatura_kelvin(entrada_celcius.get(), ))

            self.texto_resultado = tk.Label(self, text="", fg="blue")
            return_button = tk.Button(self, text="Volver", command=lambda: controller.show_frame("MenuPrincipal"))

            texto_celcius.pack()
            entrada_celcius.pack()

            button1.pack()
            self.texto_resultado.pack()
            return_button.pack()

        def obtener_temperatura_kelvin(self, temp_celcius):

            resultado = calc.convertir_celcius_a_kelvin(float(temp_celcius))
            self.texto_resultado["text"] = "Temperatura en kelvin: " + str(resultado)+" K"


class CalculoTemperatura(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Complete los datos requeridos", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        texto_moles = tk.Label(self, text="Numero de moles")
        entrada_moles = tk.Entry(self)

        texto_presion = tk.Label(self, text="Presion del gas(En atm)")
        entrada_presion = tk.Entry(self)

        texto_volumen = tk.Label(self, text="Volumen(En Litros)")
        entrada_volumen = tk.Entry(self)

        button1 = tk.Button(self, text="Calcular",
                            command=lambda: self.obtener_temperatura(entrada_moles.get(), entrada_presion.get(), entrada_volumen.get()))

        self.texto_resultado = tk.Label(self, text="", fg="blue")
        return_button = tk.Button(self, text="Volver", command=lambda: controller.show_frame("MenuPrincipal"))

        texto_moles.pack()
        entrada_moles.pack()
        texto_presion.pack()
        entrada_presion.pack()
        texto_volumen.pack()
        entrada_volumen.pack()
        button1.pack()
        self.texto_resultado.pack()
        return_button.pack()

    def obtener_temperatura(self, nmoles, presion, volumen):
        resultado = calc.obtener_temperatura_gas_ideal(float(nmoles), float(presion), float(volumen))
        self.texto_resultado["text"] = "Temperatura: " + str(resultado) + "kJ"


class CalculoTrabajoPresionConstante(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.texto_resultado = tk.Label(self, text="", fg="blue")

        label = tk.Label(self, text="Complete los datos requeridos", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        texto_presion = tk.Label(self, text="Presion(En ATM)")
        entrada_presion = tk.Entry(self)

        texto_volumen_final = tk.Label(self, text="Volumen final (En Litros)")
        entrada_volumen_final = tk.Entry(self)

        texto_volumen_inicial = tk.Label(self, text="Volumen inicial(En Litros)")
        entrada_volumen_inicial = tk.Entry(self)

        button1 = tk.Button(self, text="Calcular", command=lambda: self.obtener_trabajo_presion_constante(entrada_presion.get(),
                entrada_volumen_final.get(),
                entrada_volumen_inicial.get()))

        return_button = tk.Button(self, text="Volver",
                                  command=lambda: controller.show_frame("MenuPrincipal"))

        texto_presion.pack()
        entrada_presion.pack()
        texto_volumen_final.pack()
        entrada_volumen_final.pack()
        texto_volumen_inicial.pack()
        entrada_volumen_inicial.pack()
        button1.pack()

        self.texto_resultado.pack()
        return_button.pack()

    def obtener_trabajo_presion_constante(self, presion, volumen_final, volumen_inicial):
        resultado = calc.obtener_trabajo_presion_constante(float(presion), float(volumen_final), float(volumen_inicial))
        self.texto_resultado["text"] = "W: " + str(resultado) + "Atm * L"


class CalculoTrabajoTemperaturaConstante(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.texto_resultado = tk.Label(self, text="", fg="blue")

        label = tk.Label(self, text="Complete los datos requeridos", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        texto_moles = tk.Label(self, text="Numero de moles")
        entrada_moles = tk.Entry(self)

        texto_temperatura = tk.Label(self, text="Temperatura (En Kelvin)")
        entrada_temperatura = tk.Entry(self)

        texto_volumen_final = tk.Label(self, text="Volumen final (En Litros)")
        entrada_volumen_final = tk.Entry(self)

        texto_volumen_inicial = tk.Label(self, text="Volumen inicial(En Litros)")
        entrada_volumen_inicial = tk.Entry(self)

        button1 = tk.Button(self, text="Calcular", command=lambda: self.obtener_trabajo_temperatura_constante(
                entrada_moles.get(), entrada_temperatura.get(), entrada_volumen_final.get(),
                entrada_volumen_inicial.get()))

        return_button = tk.Button(self, text="Volver",
                                  command=lambda: controller.show_frame("MenuPrincipal"))

        texto_moles.pack()
        entrada_moles.pack()
        texto_temperatura.pack()
        entrada_temperatura.pack()
        texto_volumen_final.pack()
        entrada_volumen_final.pack()
        texto_volumen_inicial.pack()
        entrada_volumen_inicial.pack()
        button1.pack()

        self.texto_resultado.pack()
        return_button.pack()

    def obtener_trabajo_temperatura_constante(self, nmoles, temperatura, volumen_final, volumen_inicial):
        resultado = calc.obtener_trabajo_temperatura_constante(float(nmoles), float(temperatura), float(volumen_final),
                                                               float(volumen_inicial))
        self.texto_resultado["text"] = "W: " + str(resultado) + "Atm * L"


class MenuConversiones(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Menu conversiones", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button0 = tk.Button(self, text="Conversion de Celcius a Kelvin: ", command=lambda: controller.show_frame("ConversionCelcius"))
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("MenuPrincipal"))
        button0.pack()
        button.pack()


class Grafico(tk.Frame):

    line_counter = 7
    point_index = 1

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        titulo0 = tk.Label(self, text="Numero de moles (Obligatorio)")
        self.entrada_moles = tk.Entry(self)

        titulo1 = tk.Label(self, text="Agregar PUNTO(MINIMO 2)")

        titulo_presion = tk.Label(self, text="Presion(En ATM)")
        titulo_volumen = tk.Label(self, text="Volumen(En Litros)")
        titulo_presion2 = tk.Label(self, text="Presion(En ATM)")
        titulo_volumen2 = tk.Label(self, text="Volumen(En Litros)")

        entrada_presion = tk.Entry(self)
        entrada_volumen = tk.Entry(self)
        var_0 = tk.IntVar()
        var_0.set(0)
        var_0_int = var_0.get()

        titulo2 = tk.Label(self, text="Agregar PUNTO(MINIMO 2)")
        entrada_presion2 = tk.Entry(self)
        entrada_volumen2 = tk.Entry(self)
        var_1 = tk.IntVar()
        var_1.set(0)
        var_1_int = var_1.get()
        self.entry_list = [[titulo1, entrada_presion, entrada_volumen, var_0_int], [titulo2, entrada_presion2, entrada_volumen2, var_1_int]]
        self.answer_list = [var_0, var_1]
        print("Valor del entry list: " + str(self.entry_list[1][2]))

        radio_isoterma = tk.Radiobutton(self, text="Isoterma", command= lambda : self.change(1, 1))
        radio_noisoterma = tk.Radiobutton(self, text="Volumen/Presion constante", command= lambda : self.change(1, 0))
        radio_adiabatica = tk.Radiobutton(self, text="Adiabatica", command=lambda: self.change(1, 2))

        button_add = tk.Button(self, text="Agregar otro punto", command=self.clone)
        boton_resultado = tk.Button(self, text="Generar grafico", command=self.resultado)
        button_return = tk.Button(self, text="Volver", command= self.reset)

        button_add.grid(row=0, column=0)
        boton_resultado.grid(row=0, column=1)
        button_return.grid(row=0, column=2)

        titulo0.grid(row=1, column=0)
        self.entrada_moles.grid(row=1, column= 1)

        titulo1.grid(row=2, column=0)
        titulo_presion.grid(row=3, column=0)
        titulo_volumen.grid(row=3, column=1)
        entrada_presion.grid(row=4, column=0)
        entrada_volumen.grid(row=4, column=1)

        titulo2.grid(row=5, column=0)
        titulo_presion2.grid(row=6, column=0)
        titulo_volumen2.grid(row=6, column=1)
        entrada_presion2.grid(row=7, column=0)
        entrada_volumen2.grid(row=7, column=1)
        radio_isoterma.grid(row=7, column=2)
        radio_noisoterma.grid(row=7, column=3)
        radio_adiabatica.grid(row=7, column=4)

    def change(self, index, value):
        self.entry_list[index][3] = value
        print("Lista de puntos")
        for entry in self.entry_list:
            print("("+str(type(entry[1]))+" , " + str(type(entry[2])) + " , " + str(type(entry[3])))
            print(str(entry[1].get()) + str(entry[2].get()) + str(entry[3]))

    def clone(self):
        self.point_index = self.point_index + 1
        instance_titulo = tk.Label(self, text="Agregar PUNTO")

        instance_titulo_presion = tk.Label(self, text="Presion(En ATM)")
        instance_titulo_volumen = tk.Label(self, text="Volumen(En Litros)")

        instance_presion = tk.Entry(self)
        instance_volumen = tk.Entry(self)

        instance_radio_isoterma = tk.Radiobutton(self, text="Isoterma",
                                                 command=lambda: self.change(self.point_index, 1))
        instance_radio_noisoterma = tk.Radiobutton(self, text="Presion / volumen constante",
                                                   command=lambda: self.change(self.point_index, 0))
        instance_radio_adiabatica = tk.Radiobutton(self, text="Adiabatica",
                                                   command=lambda: self.change(self.point_index, 2))
        ivar = tk.IntVar()
        ivar.set(0)
        ivar_int = ivar.get()

        point_elements = [instance_titulo, instance_presion, instance_volumen, ivar_int, instance_titulo_presion,
                instance_titulo_volumen, instance_radio_isoterma, instance_radio_noisoterma, instance_radio_adiabatica]

        self.entry_list.append(point_elements)
        self.line_counter = self.line_counter + 1
        self.answer_list.append(ivar)

        instance_titulo.grid(row= self.line_counter, column= 0)
        self.line_counter = self.line_counter + 1

        instance_titulo_presion.grid(row= self.line_counter, column=0)
        instance_titulo_volumen.grid(row= self.line_counter, column=1)

        self.line_counter = self.line_counter + 1
        instance_presion.grid(row= self.line_counter, column= 0)
        instance_volumen.grid(row= self.line_counter, column= 1)
        instance_radio_isoterma.grid(row= self.line_counter, column=2)
        instance_radio_noisoterma.grid(row= self.line_counter, column=3)
        instance_radio_adiabatica.grid(row= self.line_counter, column=4)

    def reset(self):
        for point in range(2, len(self.entry_list)):
            self.entry_list[point][0].grid_forget()
            self.entry_list[point][1].grid_forget()
            self.entry_list[point][2].grid_forget()
            self.entry_list[point][4].grid_forget()
            self.entry_list[point][5].grid_forget()
            self.entry_list[point][6].grid_forget()
            self.entry_list[point][7].grid_forget()
            self.entry_list[point][8].grid_forget()

        self.entry_list = [self.entry_list[0], self.entry_list[1]]

        self.controller.show_frame("MenuPrincipal")

    def resultado(self):
        resultados = []

        for point in range(0, len(self.entry_list)):
            print("Es isotermico: " + str(self.entry_list[point][3]))

            if self.entry_list[point][3] is 1:

                print("Es un proceso isotermico")

                temperatura = calc.obtener_temperatura_gas_ideal(float(self.entry_list[point][1].get()),
                        float(self.entry_list[point][2].get()), float(self.entrada_moles.get()))
                print("Temperatura durante el proceso isotermico: ", str(temperatura))

                puntos = graf.generar_puntos_isoterma(float(self.entrada_moles.get()), float(self.entry_list[point][2].get()),
                                                      float(self.entry_list[point-1][2].get()), float(self.entry_list[point][1].get()),
                                                      float(self.entry_list[point-1][1].get()), 25, temperatura)

                for punto in puntos:
                    tupla = (punto[0], punto[1])
                    resultados.append(tupla)

            elif self.entry_list[point][3] is 2:

                print("Es un proceso adiabatico")

                puntos = graf.generar_puntos_adiabatica(float(self.entry_list[point][1].get()),
                        float(self.entry_list[point-1][1].get()), float(self.entry_list[point][2].get()),
                        float(self.entry_list[point-1][2].get()), False, 25)

                for punto in puntos:
                    tupla = (punto[0], punto[1])
                    resultados.append(tupla)

            else:

                print("No es un proceso isotermico")
                tupla = (float(self.entry_list[point][1].get()), float(self.entry_list[point][2].get()))
                print("Tupla: " + str(tupla))
                resultados.append(tupla)
        graf.generar_grafico(resultados)


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()