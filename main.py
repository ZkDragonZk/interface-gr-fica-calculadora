from tkinter import*

janela = Tk()

def bt_click():
    x = str(ed1.get())
    if "+" in x:
        x= x.split("x")
        if str(x[0]).isnumeric() and str(x[1]).isnumeric():
            lb["text"] = int(x[0]) + int(x[1])
    elif "-" in x:
        x = x.split("-")
        if str(x[0]).isnumeric() and str(x[1]).isnumeric():
            lb["text"] = int(x[0]) - int(x[1])
    elif "*" in x:
        x = x.split("*")
        if str(x[0]).isnumeric() and str(x[1]).isnumeric():
            lb["text"] = int(x[0]) * int(x[1])
    elif "/" in x:
        x = x.split("/")
        if str(x[0]).isnumeric() and str(x[1]).isnumeric():
            lb["text"] = int(x[0]) / int(x[1])
    else:
        lb["text"] = "cálculo invalido"


ed1 = Entry(janela)
ed1.place(x=100, y=80)

bt1 = Button(janela, width=5, text="=", command=bt_click)
bt1.place(x=100, y=120)

lb = Label(janela, text="total")
lb.place(x=100, y=140)


janela.geometry("300x300")
janela.mainloop()
