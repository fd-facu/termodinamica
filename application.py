# Importing Python libraries
import json
import sys
import time
import webbrowser
import tkinter.messagebox as msj

from matplotlib import pyplot as plt
# Tkinter lib has a different name in python 2
if sys.version_info[0] < 3:
    import Tkinter as tk
    import tkFont as tkfont
else:
    import tkinter as tk
    from tkinter import font as tkfont

# Importing some project files
import calculations as calc
import graphic_pressure_volume as graf
import grafico_temp_calor as graf2


# Each page is represented by  a class


# Global variables
current_language = 'english'


# Validate if the input values for certain Entry widgets are numbers.
def global_validation(entry_list):
    try:
        print("Validating submitted values...")
        for entry in entry_list:
            value = float(entry)
            # print without new line
            print(value, end=' ')
        print('\n')
        return True
    except ValueError:
        print("\n")
        return False


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)

        # This is the application menubar
        self.menu = tk.Menu(container.master)

        container.master.config(menu=self.menu)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.edit = tk.Menu(self.menu)
        self.help = tk.Menu(self.menu)

        self.edit.add_command(label="Language", command=self.create_language_window)
        self.help.add_command(label='Help', command=self.create_help_window)
        self.help.add_command(label="About", command=self.create_about_popup)

        self.menu.add_cascade(label="Edit", menu=self.edit)
        self.menu.add_cascade(label="Help", menu=self.help)

        self.frames = {}
        for frame in (MainMenu, OperationsMenu, ConvertionsMenu, HeatCalculation, LatentHeatCalculation, TemperatureCalculation,
                      ConstantPressureWorkCalculation, ConstantTemperatureWorkCalculation, Graphic, HeatGraphic):
            page_name = frame.__name__
            frame = frame(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.title("Thermodinamics Application 0.4")
        self.geometry("1024x576")
        self.show_frame("MainMenu")

    # Show a frame for the given page name
    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()

    def create_help_window(self):

        # import the content of 'help.txt' text file
        import_text = open('help.txt', 'r')
        text = import_text.read()

        help_window = tk.Toplevel(self)
        # Keep the focus on the window.
        help_window.grab_set()
        help_window.wm_title("Help")
        l = tk.Label(help_window, text=text)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

    def go_to(self, event, href, tag_name):
        res = event.widget
        res.tag_config(tag_name, background='red')  # change tag text style
        res.update_idletasks()  # make sure change is visible
        time.sleep(.5)  # optional delay to show changed text
        print('Opening:', href)  # comment out
        webbrowser.open_new(href)  # uncomment out
        res.tag_config(tag_name, background='white')  # restore tag text style
        res.update_idletasks()

    def create_language_window(self):
        language_window = tk.Toplevel(self)
        # Keep the focus on the window.
        language_window.grab_set()
        language_window.wm_title("Change Language")
        language_window.geometry("480x160")
        english_radio = tk.Radiobutton(language_window, text="English", command=lambda: self.change_language("english"), state="normal")
        spanish_radio = tk.Radiobutton(language_window, text="Spanish", command=lambda: self.change_language("spanish"), state="active")

        english_radio.pack()
        spanish_radio.pack()

    def change_language(self, language):

        global current_language
        current_language = language
        print("Language changed to " + language)

        if current_language is 'spanish':
            self.edit.entryconfigure(1, label="Idioma")
            self.help.entryconfigure(1, label="Ayuda")
            self.help.entryconfigure(2, label="Acerca de")
        else:
            self.edit.entryconfigure(1, label="Language")
            self.help.entryconfigure(1, label="Docs")
            self.help.entryconfigure(2, label="About")

    def create_about_popup(self):

        print("Loading about popup...")
        about_window = tk.Toplevel(self)
        about_window.grab_set()

        if current_language is "spanish":
            about_window.wm_title("Acerca de")
            about_text = "\nAplicacion termodinamica version 0.4 \nCreado por Facundo Peña \nSoftware distribuido mediante licencia MIT\nVea el codigo fuente en:\n  "
        else:
            about_window.wm_title("About")
            about_text = "\nTermodynamics Application version 0.4 \nCreated by Facundo Peña \nThis software is distributed with MIT open source licence\nRead source code on:\n  "

        # Keep the focus on the window.

        tx = tk.Text(about_window)
        tx.insert(0.1, about_text)

        href = "https://github.com/fd-facu/termodinamica"
        tag_name = "link"   # create unique name for tag

        # shim to call real event handler with extra args
        callback = (lambda event, href=href, tag_name=tag_name:
                    self.go_to(event, href, tag_name))
        tx.tag_bind(tag_name, "<Button-1>", callback)  # just pass function
        # (don't call it)
        tx.insert(tk.INSERT, href , (tag_name,))  # insert tagged text

        tx.config(state='disabled')
        tx.pack(side="bottom", padx=20, anchor='w')


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller



        button_group = tk.Frame(self)

        operations_button = tk.Button(button_group, text="Calculations", command=lambda: controller.show_frame("OperationsMenu"))
        conversions_button = tk.Button(button_group, text="Conversions", command=lambda: controller.show_frame("ConvertionsMenu"))
        graphic_button = tk.Button(button_group, text="Graphic", command=lambda: controller.show_frame("Graphic"))
        heat_graphic_button = tk.Button(button_group, text="Heat Graphic", command=lambda: controller.show_frame("HeatGraphic"))
        exit_button = tk.Button(button_group, text="Exit", command=lambda: quit)


        operations_button.pack()
        conversions_button.pack()
        graphic_button.pack()
        heat_graphic_button.pack()
        exit_button.pack()
        button_group.pack(side="left", fill="y")


class OperationsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_label = tk.Label(self, text="Select an operation", font=controller.title_font)

        heat_button = tk.Button(self, text="Heat (Q) ", command=lambda: controller.show_frame("HeatCalculation"))
        latent_heat_button = tk.Button(self, text="Latent heat", command=lambda:
                controller.show_frame("LatentHeatCalculation"))
        temperature_button = tk.Button(self, text="Temperature", command=lambda:
                controller.show_frame("TemperatureCalculation"))
        isobaric_button = tk.Button(self, text="Work on isobaric process",
                command=lambda: controller.show_frame("ConstantPressureWorkCalculation"))
        isothermal_button = tk.Button(self, text="Work on isothermal process",
                command=lambda: controller.show_frame("ConstantTemperatureWorkCalculation"))
        return_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))

        title_label.pack(side="top", fill="x", pady=10)
        heat_button.pack()
        latent_heat_button.pack()
        temperature_button.pack()
        isobaric_button.pack()
        isothermal_button.pack()
        return_button.pack()


class HeatCalculation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Complete the required fields", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        mass_label = tk.Label(self, text="Mass(kg)")
        mass_entry = tk.Entry(self)

        specific_heat_label = tk.Label(self, text="Specific heat(kJ/kg*K)")
        specific_heat_entry = tk.Entry(self)

        temperature_label = tk.Label(self, text="Temperature (K)")
        temperature_entry = tk.Entry(self)

        calculate_button = tk.Button(self, text="Calculate",
                                     command=lambda: self.get_heat(mass_entry.get(), specific_heat_entry.get(), temperature_entry.get()))

        self.result_label = tk.Label(self, text="", fg="blue")

        return_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("OperationsMenu"))

        mass_label.pack()
        mass_entry.pack()
        specific_heat_label.pack()
        specific_heat_entry.pack()
        temperature_label.pack()
        temperature_entry.pack()
        calculate_button.pack()
        self.result_label.pack()
        return_button.pack()

    def get_heat(self, masa, calor_especifico, temperatura):
        if global_validation([masa, calor_especifico, temperatura]) is True:
            resultado = calc.obtener_calor(float(masa), float(calor_especifico), float(temperatura))
            print("Result: " + str(resultado))
            resultado = round(resultado,2)
            self.result_label["text"] = "total Q: " + str(resultado) + " kJ"
            self.result_label["fg"] = "blue"

        else:
            print("One on the submited values is not valid.")
            self.result_label["text"] = "One of the submited values is not valid."
            self.result_label["fg"] = "red"


class LatentHeatCalculation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_label = tk.Label(self, text="Complete the required fields", font=controller.title_font)

        mass_label = tk.Label(self, text="Mass(kg)")
        mass_entry = tk.Entry(self)

        latent_heat_label = tk.Label(self, text="Latent heat fusion/vaporization(In kJ/kg*K)")
        latent_heat_entry = tk.Entry(self)

        button1 = tk.Button(self, text="Calculate",
                            command=lambda: self.get_latent_heat(mass_entry.get(), latent_heat_entry.get()))

        self.result_label = tk.Label(self, text="", fg="blue")
        return_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainMenu"))

        title_label.pack(side="top", fill="x", pady=10)
        mass_label.pack()
        mass_entry.pack()
        latent_heat_label.pack()
        latent_heat_entry.pack()
        button1.pack()
        self.result_label.pack()
        return_button.pack()

    def get_latent_heat(self, mass, latent_heat):

        result = calc.calor_de_cambio_fase(float(mass), float(latent_heat))
        self.result_label["text"] = "Q total: " + str(result) + " kJ"


class TemperatureCalculation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Complete los datos requeridos", font=controller.title_font)

        texto_moles = tk.Label(self, text="Numero de moles")
        entrada_moles = tk.Entry(self)

        texto_presion = tk.Label(self, text="Presion del gas(En atm)")
        entrada_presion = tk.Entry(self)

        texto_volumen = tk.Label(self, text="Volumen(En Litros)")
        entrada_volumen = tk.Entry(self)

        button1 = tk.Button(self, text="Calcular",
                            command=lambda: self.obtener_temperatura(entrada_moles.get(), entrada_presion.get(), entrada_volumen.get()))

        self.texto_resultado = tk.Label(self, text="", fg="blue")
        return_button = tk.Button(self, text="Volver", command=lambda: controller.show_frame("MainMenu"))

        label.pack(side="top", fill="x", pady=10)
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
        try:
            resultado = calc.obtener_temperatura_gas_ideal(float(nmoles), float(presion), float(volumen))
            print("resultado: " + str(resultado))
            self.texto_resultado["text"] = "Temperatura: " + str(resultado) + "kJ"

        except ValueError:
            print("Uno de los valores ingresados no es valido")
            self.texto_resultado["text"] = "Uno de los valores ingresados no es valido"


class ConstantPressureWorkCalculation(tk.Frame):

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

        return_button = tk.Button(self, text="Back",
                                  command=lambda: controller.show_frame("MainMenu"))

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


class ConstantTemperatureWorkCalculation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.result_label = tk.Label(self, text="", fg="blue")

        title_label = tk.Label(self, text="Complete the required fields", font=controller.title_font)

        moles_label = tk.Label(self, text="Number of moles")
        moles_entry = tk.Entry(self)

        temperature_label = tk.Label(self, text="Temperature (In Kelvin)")
        temperature_entry = tk.Entry(self)

        final_volume_label = tk.Label(self, text="Final volume(In Litres)")
        final_volume_entry = tk.Entry(self)

        initial_volume_label = tk.Label(self, text="Initial volume(In Litres)")
        initial_volume_entry = tk.Entry(self)

        submit_button = tk.Button(self, text="Submit", command=lambda: self.obtener_trabajo_temperatura_constante(
                moles_entry.get(), temperature_entry.get(), final_volume_entry.get(),
                initial_volume_entry.get()))

        return_button = tk.Button(self, text="Volver",
                                  command=lambda: controller.show_frame("MainMenu"))

        title_label.pack(side="top", fill="x", pady=10)
        moles_label.pack()
        moles_entry.pack()
        temperature_label.pack()
        temperature_entry.pack()
        final_volume_label.pack()
        final_volume_entry.pack()
        initial_volume_label.pack()
        initial_volume_entry.pack()
        submit_button.pack()

        self.result_label.pack()
        return_button.pack()

    def obtener_trabajo_temperatura_constante(self, nmoles, temperatura, volumen_final, volumen_inicial):
        resultado = calc.obtener_trabajo_temperatura_constante(float(nmoles), float(temperatura), float(volumen_final),
                                                               float(volumen_inicial))
        self.result_label["text"] = "W: " + str(resultado) + "Atm * L"


class ConvertionsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.temperature_type = 0

        label = tk.Label(self, text="Conversion de medidas", font=controller.title_font)
        label.grid(row=0, column=0)

        self.label_temperature = tk.Label(self, text="De Celcius a Kelvin")

        self.label_temperature.grid(row=1, column=0)

        entry_temperature = tk.Entry(self)

        entry_temperature.grid(row=1, column=1)

        button_reverse_temperature = tk.Button(self, text="Invertir", command=lambda: self.reverse_temperature())

        button_reverse_temperature.grid(row=1, column=2)

        button_temperature = tk.Button(self, text="Convertir", command=lambda: self.conversion(entry_temperature.get()))

        button_temperature.grid(row=1, column=3)

        self.label_result = tk.Label(self, text='', fg="blue")

        self.label_result.grid(row=1, column=4)

        button = tk.Button(self, text="Volver",
                           command=lambda: controller.show_frame("MainMenu"))

        button.grid(row=2, column=0)

    def conversion(self, temperature):

        if self.temperature_type is 0:
            result = calc.convertir_celcius_a_kelvin(float(temperature))
            self.label_result["text"] = "Temperature on Kelvin: " + str(result)
        else:
            result = calc.convertir_kelvin_a_celcius(float(temperature))
            self.label_result["text"] = "Temperature on Celcius: " + str(result)

    def reverse_temperature(self):
        if self.temperature_type is 0:
            self.temperature_type = 1
            self.label_temperature["text"] = "From Kelvin to Celcius"

        else:
            self.temperature_type = 0
            self.label_temperature["text"] = "From Celcius to kelvin"


class Graphic(tk.Frame):

    line_counter = 7
    point_index = 1

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        moles_label = tk.Label(self, text="Number of moles (Obligatory)")
        self.moles_entry = tk.Entry(self)

        title_label = tk.Label(self, text="Add Point(At least 2)")

        pressure_label = tk.Label(self, text="Pressure")
        volume_label = tk.Label(self, text="Volume")
        pressure_2_label = tk.Label(self, text="Pressure")
        volume_2_label = tk.Label(self, text="Volume")

        pressure_entry = tk.Entry(self)
        volume_entry = tk.Entry(self)

        var_0 = tk.IntVar()
        var_0.set(0)
        var_0_int = var_0.get()

        title2_label = tk.Label(self, text="Add Point(At least 2)")
        entrada_presion2 = tk.Entry(self)
        entrada_volumen2 = tk.Entry(self)

        self.var_1 = tk.IntVar()
        self.var_1.set(0)
        var_1_int = self.var_1.get()

        self.entry_list = [[pressure_entry, volume_entry, var_0_int], [entrada_presion2, entrada_volumen2, var_1_int]]
        self.answer_list = [var_0, self.var_1]
        print("valor del entry list: " + str(self.entry_list[1][2]))

        process_label = tk.Label(self, text=" Process type")
        isothermal_radius = tk.Radiobutton(self, text="Isothermal", command= lambda : self.change(1, 1))
        non_isothermal_radius = tk.Radiobutton(self, text="Constant Volume/Pressure", command= lambda : self.change(1, 0))
        adiabatic_radius = tk.Radiobutton(self, text="Adiabatic", command=lambda: self.change(1, 2))

        button_add = tk.Button(self, text="Add another point", command=self.clone)
        boton_resultado = tk.Button(self, text="Submit", command=self.resultado)
        button_return = tk.Button(self, text="Back", command= self.reset)

        button_add.grid(row=0, column=0)
        boton_resultado.grid(row=0, column=1)
        button_return.grid(row=0, column=2)

        moles_label.grid(row=1, column=0)
        self.moles_entry.grid(row=1, column= 1)

        title_label.grid(row=2, column=0)
        pressure_label.grid(row=3, column=0)
        volume_label.grid(row=3, column=1)
        pressure_entry.grid(row=4, column=0)
        volume_entry.grid(row=4, column=1)

        title2_label.grid(row=5, column=0)
        pressure_2_label.grid(row=6, column=0)
        volume_2_label.grid(row=6, column=1)
        entrada_presion2.grid(row=7, column=0)
        entrada_volumen2.grid(row=7, column=1)
        process_label.grid(row=7, column=2)
        isothermal_radius.grid(row=7, column=3)
        non_isothermal_radius.grid(row=7, column=4)
        adiabatic_radius.grid(row=7, column=5)

    def change(self, index, value):
        self.entry_list[index][2] = value
        print("Lista de puntos")
        print(self.entry_list)
        for entry in self.entry_list:
            print("Presion: " + str(entry[0].get()) + "  Volumen: " + str(entry[1].get()) + "  Tipo de proceso: " +
                    str(entry[2]))

    def clone(self):
        self.point_index = self.point_index + 1
        instance_titulo = tk.Label(self, text="Agregar PUNTO")

        instance_titulo_presion = tk.Label(self, text="Presion")
        instance_titulo_volumen = tk.Label(self, text="Volumen")

        instance_presion = tk.Entry(self)
        instance_volumen = tk.Entry(self)

        instance_radio_isoterma = tk.Radiobutton(self, text="Isoterma",
                                                 command=lambda: self.change(self.point_index, 1))
        instance_radio_noisoterma = tk.Radiobutton(self, text="No isoterma",
                                                   command=lambda: self.change(self.point_index, 0))
        instance_radio_adiabatica = tk.Radiobutton(self, text="Adiabatica",
                                                   command=lambda: self.change(self.point_index, 2))
        ivar = tk.IntVar()
        ivar.set(0)
        ivar_int = ivar.get()

        point_elements = [instance_presion, instance_volumen, ivar_int, instance_titulo_presion,
                instance_titulo_volumen, instance_radio_isoterma, instance_radio_noisoterma, instance_radio_adiabatica]

        print(point_elements)
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

        self.controller.show_frame("MainMenu")

    def resultado(self):
        resultados = []

        for point in range(0, len(self.entry_list)):
            print("Es isotermico: " + str(self.entry_list[point][2]) )

            if self.entry_list[point][2] is 1:

                print("Es un proceso isotermico.")

                temperatura = calc.obtener_temperatura_gas_ideal(float(self.entry_list[point][0].get()),
                                                                 float(self.entry_list[point][1].get()), float(self.moles_entry.get()))
                print("Temperatura durante el proceso isotermico: ", str(temperatura))

                puntos = graf.generar_puntos_isoterma(float(self.moles_entry.get()), float(self.entry_list[point][1].get()),
                                                      float(self.entry_list[point-1][1].get()), float(self.entry_list[point][0].get()),
                                                      float(self.entry_list[point-1][0].get()), 25, temperatura)

                for punto in puntos:
                    tupla = (punto[0], punto[1])
                    resultados.append(tupla)

            elif self.entry_list[point][2] is 2:

                print("Es un proceso adiabatico")

                puntos = graf.generar_puntos_adiabatica(float(self.entry_list[point][0].get()),
                        float(self.entry_list[point-1][0].get()), float(self.entry_list[point][1].get()),
                        float(self.entry_list[point-1][1].get()), False, 25)

                for punto in puntos:
                    tupla = (punto[0], punto[1])
                    resultados.append(tupla)

            else:

                print("No es un proceso isotermico")
                tupla = (float(self.entry_list[point][0].get()), float(self.entry_list[point][1].get()))
                print("Tupla: " + str(tupla))
                resultados.append(tupla)
        graf.generar_grafico(resultados)


class HeatGraphic(tk.Frame):
    line_counter = 7
    point_index = 1

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.data_frame = tk.Frame(self)
        self.bottom_frame = tk.Frame(self)

        self.data_frame.speed_label = tk.Label(self.data_frame, text="Speed (Kj per second)")

        self.data_frame.speed_label.grid(row=0, column=0)

        self.mass_label = tk.Label(self.data_frame, text="Mass(In Kg)")
        self.mass_entry = tk.Entry(self.data_frame)

        var = tk.StringVar(self.data_frame)
        var.set("water")  # initial value

        self.element_label = tk.Label(self.data_frame, text="Element")
        self.element_option = tk.OptionMenu(self.data_frame, var, "water", "gold", "sulfur", "copper")

        self.initial_temperature_label = tk.Label(self.data_frame, text="Initial temperature (In K)")
        self.initial_temperature_entry = tk.Entry(self.data_frame)

        self.final_temperature_label = tk.Label(self.data_frame, text="Final temperature (In K)")
        self.final_temperature_entry = tk.Entry(self.data_frame)

        self.bottom_frame.submit_button = tk.Button(self.bottom_frame, text="submit", command=self.result())
        self.bottom_frame.submit_button.grid(row=0, column=0)

        self.mass_label.grid(row=1, column=0)
        self.mass_entry.grid(row=1, column=1)
        self.element_label.grid(row=2, column=0)
        self.element_option.grid(row=2, column=1)
        self.initial_temperature_label.grid(row=3, column=0)
        self.initial_temperature_entry.grid(row=3, column=1)
        self.final_temperature_label.grid(row=4, column=0)
        self.final_temperature_entry.grid(row=4, column=1)

        self.data_frame.grid(row=0, column=0)
        self.bottom_frame.grid(row=1, column=0)

        '''self.speed_label = tk.Label(self, text="Kj por segundo")
        self.speed_entry = tk.Entry(self)
        
        self.specific_heat_label = tk.Label(self, text="Calor especifico")
        self.specific_heat_entry = tk.Entry(self)'''

        '''self.speed_label.grid(row=0, column=0)
        self.speed_entry.grid(row=0, column=1)
        
        self.specific_heat_label.grid(row=2, column=0)
        self.specific_heat_entry.grid(row=2, column=1)'''

    def result(self):
        # graf2.generate_points(60, float(self.mass_entry.get()), )
        file = open('heat_data.json', 'r')
        file_string = file.read()
        file_json = json.loads(file_string)
        print('Pending')
        print(file_json['water']['fusion point'])


if __name__ == "__main__":
    print("Starting application...\n")
    app = Application()
    app.mainloop()
