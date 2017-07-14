import tkinter as tk

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        self.help = tk.Menu(self.menu)

        self.help.add_command(label='Ayuda', command=self.create_help_window)
        self.help.add_command(label="acerca de")
        self.menu.add_cascade(label="Ayuda", menu=self.help)



    def create_help_window(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="This is window #%s\ndota es el mejor" % self.counter)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    root.geometry("800x450")
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()