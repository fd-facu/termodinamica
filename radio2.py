from tkinter import *

class App(object):
    def __init__(self, master):
        self.radio_var = StringVar()
        self.radio_var.set('python')

        lable1 = Label(master, text=' hovering over below radio buttons will cause them to look like they are selected')
        lable1.pack()

        runtimeFrame = Frame(master, relief=GROOVE, borderwidth=3)
        runtimeFrame.pack(fill=X, pady=5, padx=5)
        for mode in ['java', 'python', 'jython']:
            b = Radiobutton(runtimeFrame, text=mode, variable=self.radio_var, value=mode, indicatoron=1)
            b.pack(side=LEFT)

if __name__ == '__main__':
    master = Tk()
    app = App(master)
    mainloop()