import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x800")

etiquetabase = tkinter.Label(ventana,text="Resolver matrices 3x3 metodo eliminacion", font="roboto 12")
etiquetabase.pack()

frame = tkinter.Frame(ventana)
frame.pack(pady=20)

val00 = tkinter.Entry(frame)
val01 = tkinter.Entry(frame)
val02 = tkinter.Entry(frame)
val03 = tkinter.Entry(frame)
val10 = tkinter.Entry(frame)
val11 = tkinter.Entry(frame)
val12 = tkinter.Entry(frame)
val13 = tkinter.Entry(frame)
val20 = tkinter.Entry(frame)
val21 = tkinter.Entry(frame)
val22 = tkinter.Entry(frame)
val23 = tkinter.Entry(frame)

val00.grid(row=0, column=0)
val01.grid(row=0, column=1)
val02.grid(row=0, column=2)
val03.grid(row=0, column=3)
val10.grid(row=1, column=0)
val11.grid(row=1, column=1)
val12.grid(row=1, column=2)
val13.grid(row=1, column=3)
val20.grid(row=2, column=0)
val21.grid(row=2, column=1)
val22.grid(row=2, column=2)
val23.grid(row=2, column=3)

boton = tkinter.Button(ventana, text= "resolver", command=lambda: resolver())
boton.pack()

etiqueta1 = tkinter.Label(ventana, text = "")
etiqueta1.pack()

def resolver():
    valor00 = val00.get()
    try:
        retorno01 = int(valor00)
        etiqueta1.config(text= f"pusiste  {retorno01}")
    except ValueError:
        etiqueta1.config(text="numero no entero")
        
        

ventana.mainloop()