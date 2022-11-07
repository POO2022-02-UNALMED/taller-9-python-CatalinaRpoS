from tkinter import Tk, Button, Entry, Label, StringVar

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("285x250")

# Para modificar el texto de salida
operation = ""
stringVar = StringVar()

# Configuración pantalla de salida 
pantalla = Entry(root, width = 40, bg = "black", fg = "white", borderwidth = 0, font = ("arial", 18, "bold"))
pantalla.grid(row = 0, column = 0, columnspan = 4, padx = 1, pady = 1)
margen = Label(pantalla, width = 40, height = 2, bg = "black", fg = "white", borderwidth = 0, textvariable = stringVar)
margen.grid(row = 0, column = 0)

# Función para capturar los eventos
def doClick(value):
    global operation 
    operation += str(value)
    stringVar.set(operation)

# Función para mostrar el total
def doOperation():
    global operation
    try:
        total = str(eval(operation))
        stringVar.set(total)
        operation = ""
    except:
        stringVar.set("")

# Configuración botones

# Botones para los números
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: doClick(1)).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: doClick(2)).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: doClick(3)).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: doClick(4)).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: doClick(5)).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: doClick(6)).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: doClick(7)).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: doClick(8)).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: doClick(9)).grid(row=3, column=2, padx=1, pady=1)

# Botón para hacer la operación
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=lambda: doOperation()).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

# Botones para los operadores
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", command=lambda: doClick("."), borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: doClick("+")).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: doClick("-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: doClick("*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: doClick("/")).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()