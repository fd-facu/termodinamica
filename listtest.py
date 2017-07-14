import sys

from tkinter import *

# My frame for form
class simpleform_ap(Tk):

    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.grid()
    def initialize(self):

        # Dropdown Menu
        optionList = ["Yes","No"]
        self.dropVar=StringVar()
        self.dropVar.set("Yes") # default choice
        self.button1 = Button(self, text="calculo 1")
        self.dropMenu1.grid(column=1,row=4)

    def func(self,value):
        print(value)
        if value == "Yes" :


        elif value == "No":
            self.button2 = Button(self, text="Calculo 2")
            self.button2.pack()

def create_form(argv):
    form = simpleform_ap(None)
    form.title('My form')
    form.mainloop()

if __name__ == "__main__":
  create_form(sys.argv)