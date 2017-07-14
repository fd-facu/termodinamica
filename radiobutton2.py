import tkinter as tk
root = tk.Tk()
var0 = tk.IntVar()
var0.set(0)
questionlist = ["es 1 isoterma", "es 2 isoterma", "es 3 isoterma"]
answers = [var0]
counter = 3


def clone():

    global counter
    counter = counter+1

    tk.Label(root, text="es isoterma").grid(row=counter, column=0)
    vari = tk.IntVar()

    button = tk.Radiobutton(root, text="si", variable=vari, value=1, command=ShowChoice)
    button.grid(row=counter, column=1)


    button = tk.Radiobutton(root, text="no", variable=vari, value=0, command=ShowChoice)
    button.grid(row=counter, column=2)
    answers.append(vari)


button_add = tk.Button(text="Agregar otro punto", command=clone)

button_add.grid(row=0, column = 3)

def ShowChoice():
    print("Respuestas: " + str(answers))
    lista_numerada = []

    for x in answers:
        lista_numerada.append(x.get())
    print("Respuestas: " + str(lista_numerada))


for counter, question in enumerate(questionlist, 1):
    tk.Label(root, text=question).grid(row=counter, column = 0)
    var = tk.IntVar()

    button = tk.Radiobutton(root, text = "si", variable = var, value = 1, command = ShowChoice)
    button.grid(row = counter, column = 1)

    button = tk.Radiobutton(root, text="no", variable=var, value=0, command=ShowChoice)
    button.grid(row=counter, column=2)


    answers.append(var)

root.mainloop()