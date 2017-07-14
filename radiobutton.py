import sys

if sys.version_info[0] < 3:
    import Tkinter as tk
    import tkFont as tkfont
else:
    import tkinter as tk
    from tkinter import font as tkfont

def sel():
    print("entro")
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)

root = tk.Tk()
var = tk.IntVar()
label = tk.Label(root)
R1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = tk.W )

R2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = tk.W )

R3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = tk.W)

varb = tk.IntVar()
R1b = tk.Radiobutton(root, text="Option 1", variable=varb, value=1,
                  command=sel)
R1b.pack( anchor = tk.W )

R2b = tk.Radiobutton(root, text="Option 2", variable=varb, value=2,
                  command=sel())
R2b.pack( anchor = tk.W )

R3b = tk.Radiobutton(root, text="Option 3", variable=varb, value=3,
                  command=sel)
R3b.pack( anchor = tk.W)


label.pack()
root.mainloop()