import tkinter as tk
from tkinter import Tk as instance

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.number = 0
        self.widgets = []

        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.cloneButton = tk.Button(self, text='Clone', command=self.clone)
        self.resultButton = tk.Button(self, text="result", command=self.show_result)
        self.resultLabel = tk.Label(self)

        self.cloneButton.grid(row=0, column=0)
        self.resultButton.grid(row=0, column=1)
        self.resultLabel.grid(row=0, column=2)

    def clone(self):
        widget = tk.Label(self, text='%s' % self.number)
        widget.grid(row=self.number+1)
        self.widgets.append(widget)
        self.number += 1

    def show_result(self):
        resultado = 0
        for widget in self.widgets:
            resultado = resultado + int(widget['text'])
        print(resultado)
        self.resultLabel.config(text="resultado "+ str(resultado))

if __name__ == "__main__":
    app = Application()
    app.master.title("Sample application")
    app.mainloop()