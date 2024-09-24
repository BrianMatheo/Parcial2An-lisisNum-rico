import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x800")

etiquetabase = tkinter.Label(ventana,text="Resolver matrices 3x3 metodo eliminacion", font="roboto 12")
etiquetabase.pack()

frame = tkinter.Frame(ventana)
frame.pack()

val = [[None for _ in range(4)] for _ in range(3)]
valor = [[None for _ in range(4)] for _ in range(3)]
retorno = [[None for _ in range(4)] for _ in range(3)]

for i in range(3):
    for j in range(4):
        val[i][j] = tkinter.Entry(frame)
        val[i][j].grid(row=i, column=j*2, padx=5, pady=5)
        
        if j == 3:
            igual = tkinter.Label(frame, text="=")
            igual.grid(row=i, column= (j*2-1))  

boton = tkinter.Button(ventana, text= "resolver", command=lambda: resolver())
boton.pack()

etiqueta1 = tkinter.Label(ventana, text = "")
etiqueta1.pack()

etiqueta2 = tkinter.Label(ventana, text = "")
etiqueta2.pack()

etiqueta3 = tkinter.Label(ventana, text = "")
etiqueta3.pack()

etiqueta4 = tkinter.Label(ventana, text = "")
etiqueta4.pack()

def resolver():
    error = False
    
    for i in range(3):
        for j in range(4):
            valor[i][j] = val[i][j].get()
            try:
                retorno[i][j] = float(valor[i][j])
            except ValueError:
                retorno[i][j] = None
                error = True
                
    if error is False:
        retornado = retorno[0][0]
        for i in range(4):
            retorno[0][i] = round(retorno[0][i]/retornado, 4)
        etiqueta1.config(text=f"primera fila dividida por {retornado} \n {retorno[0][0]}  {retorno[0][1]}  {retorno[0][2]}  =  {retorno[0][3]} \n {retorno[1][0]}  {retorno[1][1]}  {retorno[1][2]}  =  {retorno[1][3]} \n {retorno[2][0]}  {retorno[2][1]}  {retorno[2][2]}  =  {retorno[2][3]}")
        retornado2 = retorno[1][0]
        for i in range(4):
            retorno[1][i] = round(retorno[1][i] - (retorno[0][0]*retornado2), 4)
        etiqueta2.config(text=f" fila 2 - ({retornado2} * {retorno[0][0]}) \n {retorno[1][0]}  {retorno[1][1]}  {retorno[1][2]}  =  {retorno[1][3]}")
        
    else:
        etiqueta1.config(text="numero no entero en algun espacio")
    
ventana.mainloop()