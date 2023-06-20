import tkinter as tk

win = tk.Tk()

at = tk.Label(win,text="koeficient a:")
at.pack()
a=tk.Entry(win)
a.pack()

bt = tk.Label(win,text="koeficient b:")
bt.pack()
b=tk.Entry(win)
b.pack()

ct = tk.Label(win,text="koeficient c:")
ct.pack()
c=tk.Entry(win)
c.pack()

x = tk.Label(win,text="Výsledok:")
x.pack()
xx = tk.Entry(win)
xx.pack()

def executor():
    print(a.get(),b.get(),c.get())
    ka = int(a.get())
    kb = int(b.get())
    kc = int(c.get())
    d = kb**2 - 4*ka*kc
    d = kb ** 2 - 4 * ka * kc
    if d < 0:
        xx.insert(0, "Nemá riešenie v R")
    elif d == 0:
        x = -kb / (2 * ka)
        xx.insert(0, x)
        xx.insert(0, "x = ")
    elif d>0:
        x1 = round(((-kb + d ** 0.5) / (2 * ka)), 4)
        x2 = round(((-kb - d ** 0.5) / (2 * ka)), 4)
        xx.insert(0, x2)
        xx.insert(0, " ; x2= ")
        xx.insert(0, x1)
        xx.insert(0, "x1= ")
button = tk.Button(win, text="click me", command=executor)
button.pack()
win.mainloop()