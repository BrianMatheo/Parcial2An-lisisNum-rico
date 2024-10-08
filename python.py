import tkinter
import numpy
import math
from fractions import Fraction

ventana = tkinter.Tk()
ventana.geometry("800x800")

etiquetabase = tkinter.Label(ventana,text="Resolver matrices 3x3 metodo eliminacion", font="roboto 12")
etiquetabase.pack()

frame = tkinter.Frame(ventana)
frame.pack()

val = [[None for _ in range(4)] for _ in range(3)]
valor = [[None for _ in range(4)] for _ in range(3)]

for i in range(3):
    for j in range(4):
        val[i][j] = tkinter.Entry(frame)
        val[i][j].grid(row=i, column=j*2, padx=5, pady=5)
        
        if j == 3:
            igual = tkinter.Label(frame, text="=")
            igual.grid(row=i, column= (j*2-1))  

boton = tkinter.Button(ventana, text= "resolver", command=lambda: resolver())
boton.pack(padx=20,pady=20)


texto = tkinter.Text(ventana, height=10, width=50, bg="#ffffff", font=("Arial", 12))
texto.pack()

def mejorar(matriz):
    texto = ""
    
    for i in matriz:
        texto += " ".join([f"{elem: 8.4f}".rjust(10) for elem in i[:-1]]) + " = " + f"{i[-1]: 8.4f}".rjust(10) + "\n"
    return texto

def cambio(matriz, f1, f2):
    matriz[[f1,f2]] = matriz[[f2,f1]]

def resolver():
    
    error = False
    matriz = numpy.zeros((3,4))
    
    for i in range(3):
        for j in range(4):
            valor[i][j] = val[i][j].get()
            try:
                if valor[i][j].strip() == "e":
                    matriz[i][j] = math.e
                elif valor[i][j].strip() == "pi":
                    matriz[i][j] = math.pi
                elif valor[i][j] == "":
                    matriz[i][j] = 0
                elif "/" in valor[i][j]:                
                    matriz[i][j] = float(Fraction(valor[i][j]))
                else:
                    matriz[i][j] = float(valor[i][j])
            except ValueError:
                error = True
                
    if error is False:
        texto.delete(1.0,tkinter.END)
        
        A = matriz[:, :-1]
        b = matriz[:, -1]
        matrices = numpy.hstack((A, b.reshape(-1, 1)))

        rango = numpy.linalg.matrix_rank(A)
        rangoma = numpy.linalg.matrix_rank(matrices)
        
        if rango == rangoma == A.shape[1]:
            texto.insert(tkinter.END,"solo 1 solucion \n")
        elif rango == rangoma < A.shape[1]:
            texto.insert(tkinter.END,"infinitas soluciones \n")
        else:
            texto.insert(tkinter.END,"no tiene solución \n")
        
        if matriz[0][0] == 0:
            if matriz[1][0] != 0:
                cambio(matriz, 0, 1)
                texto.insert(tkinter.END,f"se intercambió la primera fila por la segunda \n {mejorar(matriz)} \n")
            elif matriz[2][0] != 0:
                cambio(matriz, 0, 2)
                texto.insert(tkinter.END,f"se intercambió la primera fila por la segunda \n {mejorar(matriz)} \n")
            elif numpy.all(matriz[:,0] == 0):
                texto.insert(tkinter.END,"todos los valores de la primer columna son cero (0) \n")
                return
            
        retornado = matriz[0][0]
        for i in range(4):
            matriz[0][i] = matriz[0][i]/retornado
        texto.insert(tkinter.END,f"fila 1 = fila 1 / {round(retornado,4)} \n {mejorar(matriz)} \n")
        
        retornado2 = round(matriz[1][0], 4)
        for i in range(4):
            matriz[1][i] = matriz[1][i] - (retornado2*matriz[0][i])
        texto.insert(tkinter.END,f"fila 2 = fila 2 - {round(retornado2,4)} * fila 1 \n {mejorar(matriz)} \n")
        
        retornado3 = round(matriz[2][0], 4)
        for i in range(4):
            matriz[2][i] = matriz[2][i] - (matriz[0][i]*retornado3)
        texto.insert(tkinter.END,f"fila 3 = fila 3 - {round(retornado3,4)} * fila 1\n {mejorar(matriz)} \n")
        
        if matriz[1][1] == 0:
            if matriz[2][1] != 0:
                cambio(matriz, 1, 2)
                texto.insert(tkinter.END,f"se intercambió la segunda fila por la tercera \n {mejorar(matriz)} \n")
            elif numpy.all(matriz[:,1] == 0):
                texto.insert(tkinter.END,"los valores de la segunda y tercera fila en la segunda columna son cero (0) \n")
                return

        retornado4 = matriz[1][1]
        for i in range(4):
            matriz[1][i] = matriz[1][i]/retornado4
        texto.insert(tkinter.END,f" fila 2 / {round(retornado4,4)} \n {mejorar(matriz)} \n")
        
        retornado5 = matriz[2][1]
        for i in range(4):
            matriz[2][i] = matriz[2][i] - matriz[1][i]*retornado5
        texto.insert(tkinter.END,f" fila 3 - {round(retornado5,4)} * fila 2 \n {mejorar(matriz)} \n")
        
        if matriz[2][2] == 0:
            cambio(matriz, 1, 2)
            texto.insert(tkinter.END,f"el valor de la ultima columna y fila es cero \n {mejorar(matriz)} \n")
            return
        
        retornado6 = matriz[2][2]
        for i in range(4):
            matriz[2][i] = matriz[2][i]/retornado6
        texto.insert(tkinter.END,f" fila 3 / {round(retornado6,4)} \n {mejorar(matriz)} \n")

        
        
    else:
        texto.insert(tkinter.END,"valor no válido en algun espacio \n")
        


    
ventana.mainloop()