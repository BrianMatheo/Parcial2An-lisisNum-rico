import tkinter
import numpy
import math
from fractions import Fraction

ventana = tkinter.Tk() #ventana
ventana.geometry("800x600") #limites de la pantalla
ventana.title("Resolver matrices 3x3 - Método de eliminación de Gauss Jordan")
ventana.option_add("*Button.Background", "#ff100c")
ventana.option_add("*Button.Foreground", "#FFFFFF")

etiquetabase = tkinter.Label(ventana,text="Resolver Matrices 3x3 - Método eliminación de Gauss Jordan", font="Roboto 12") #titulo
etiquetabase.pack(pady=20)

variables = tkinter.Label(ventana,text="ㅤㅤㅤㅤXㅤㅤㅤㅤㅤㅤYㅤㅤㅤㅤㅤㅤZㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", font="Roboto 12")
variables.pack()

frame = tkinter.Frame(ventana) #parte de la ventana
frame.pack()

val = [[None for _ in range(4)] for _ in range(3)]
valor = [[None for _ in range(4)] for _ in range(3)]

for i in range(3):
    for j in range(4):
        
        val[i][j] = tkinter.Entry(frame, font=("Consolas", 12), width=10, justify="center", relief="solid", bd=1)
        val[i][j].grid(row=i, column=j*2, padx=5, pady=5) #matriz que se muestra en pantalla
        
        if j == 3:
            igual = tkinter.Label(frame, text="=")
            igual.grid(row=i, column= (j*2-1))

frame2 = tkinter.Frame(ventana)
frame2.pack(pady=10)

boton = tkinter.Button(frame2, text= "Resolver", command=lambda: resolver(), font="Roboto 12") #boton resolver
boton.pack(padx=20,side=tkinter.LEFT)

boton2 = tkinter.Button(frame2, text= "Limpiar", command=lambda: limpiar(), font="Roboto 12") #boton limpiar
boton2.pack(padx=20,side=tkinter.LEFT)

boton3 = tkinter.Button(frame2, text= "Manual", command=lambda: manual(), font="Roboto 12")
boton3.pack(padx=20,side=tkinter.LEFT)

texto = tkinter.Text(ventana, height=10, width=48, bg="#ffffff", font=("Roboto 12"), relief="solid",bd=1) #caja de texto
texto.pack(pady=10)

def mejorar(matriz):
    texto = "        X                Y                Z\n"
    
    for i in matriz:
        texto += " ".join([f"{elem: 8.4f}".rjust(10) for elem in i[:-1]]) + " = " + f"{i[-1]: 8.4f}".rjust(10) + "\n" #mostrar en caja de texto
    return texto

def limpiar():
    texto.delete(1.0,tkinter.END) #vacia la caja de texto
    for i in range(3):
        for j in range(4):
            val[i][j].delete(0,tkinter.END) #vacia las cuadriculas

def cambio(matriz, f1, f2):
    matriz[[f1,f2]] = matriz[[f2,f1]] #cambio de filas

def resolver():
    
    error = False
    matriz = numpy.zeros((3,4)) #matriz de ceros
    
    for i in range(3): #obtener valores de la matriz de manera float y solo numeros
        for j in range(4):
            valor[i][j] = val[i][j].get()
            try:
                if valor[i][j].strip() == "e":
                    matriz[i][j] = math.e
                elif valor[i][j].strip() == "pi":
                    matriz[i][j] = math.pi
                elif valor[i][j].strip() == "":
                    matriz[i][j] = 0
                elif "/" in valor[i][j].strip():                
                    matriz[i][j] = float(Fraction(valor[i][j].strip()))
                else:
                    matriz[i][j] = float(valor[i][j].strip())
            except ValueError:
                error = True
                
    if error is False:
        texto.delete(1.0,tkinter.END) #borrar al inicio siempre
        
        if numpy.all(matriz == 0):
            texto.insert(tkinter.END,"Todos los valores son cero (0) \n")
            return
        
        if matriz[0][0] == 0:
            if matriz[1][0] != 0:
                cambio(matriz, 0, 1)
                texto.insert(tkinter.END,f"Se intercambió la primera fila por la segunda\n {mejorar(matriz)} \n")
            elif matriz[2][0] != 0:
                cambio(matriz, 0, 2)
                texto.insert(tkinter.END,f"Se intercambió la primera fila por la tercera\n {mejorar(matriz)} \n")
            else:
                texto.insert(tkinter.END,"Todos los valores de la primer columna son cero (0)\n")
                return
            
        retornado = matriz[0][0]
        for i in range(4):
            matriz[0][i] = matriz[0][i]/retornado
        texto.insert(tkinter.END,f"Fila 1 = Fila 1 / {round(retornado,4)} \n {mejorar(matriz)} \n")
        
        retornado2 = matriz[1][0]
        for i in range(4):
            matriz[1][i] = matriz[1][i] - (retornado2*matriz[0][i])
        texto.insert(tkinter.END,f"Fila 2 = Fila 2 - {round(retornado2,4)} * fila 1 \n {mejorar(matriz)} \n")
        
        retornado3 = matriz[2][0]
        for i in range(4):
            matriz[2][i] = matriz[2][i] - (retornado3*matriz[0][i])
        texto.insert(tkinter.END,f"Fila 3 = Fila 3 - {round(retornado3,4)} * fila 1\n {mejorar(matriz)} \n")
        
        if matriz[1][1] == 0:
            if matriz[2][1] != 0:
                cambio(matriz, 1, 2)
                texto.insert(tkinter.END,f"Se intercambió la segunda fila por la tercera \n {mejorar(matriz)} \n")
            else:
                texto.insert(tkinter.END,"Los valores de la segunda y tercera fila en la segunda columna son cero (0) \n")
                return

        retornado4 = matriz[1][1]
        for i in range(4):
            matriz[1][i] = matriz[1][i]/retornado4
        texto.insert(tkinter.END,f"Fila 2 / {round(retornado4,4)} \n {mejorar(matriz)} \n")
        
        retornado5 = matriz[2][1]
        for i in range(4):
            matriz[2][i] = matriz[2][i] - matriz[1][i]*retornado5
        texto.insert(tkinter.END,f"Fila 3 - {round(retornado5,4)} * fila 2 \n {mejorar(matriz)} \n")
        
        if matriz[2][2] == 0:
            texto.insert(tkinter.END,f"El valor del último pivote es cero (0) \n")
            return
        
        retornado6 = matriz[2][2]
        
        for i in range(4):
            matriz[2][i] = matriz[2][i]/retornado6
        texto.insert(tkinter.END,f"Fila 3 / {round(retornado6,4)} \n {mejorar(matriz)} \n")
        
        retornado7 = matriz[1][2]
        
        for i in range(4):
            matriz[1][i] = matriz[1][i] - matriz[2][i] * retornado7
        texto.insert(tkinter.END,f"Fila 2 = Fila 2 - Fila 3 * {round(retornado7,4)} \n {mejorar(matriz)} \n")

        retornado8 = matriz[0][2]
        
        for i in range(4):
            matriz[0][i] = matriz[0][i] - matriz[2][i] * retornado8
        texto.insert(tkinter.END,f"Fila 1 = Fila 1 - Fila3 * {round(retornado8,4)} \n {mejorar(matriz)} \n")
        
        retornado9 = matriz[0][1]
        
        for i in range(4):
            matriz[0][i] = matriz[0][i] - matriz[1][i] * retornado9
        texto.insert(tkinter.END,f"Fila 1 = Fila 1 - Fila2 * {round(retornado9,4)} \n {mejorar(matriz)} \n")

        texto.insert(tkinter.END,f"x = {round(matriz[0][3],4)} \ny = {round(matriz[1][3],4)} \nz = {round(matriz[2][3],4)} \n")

    else:
        texto.delete(1.0, tkinter.END)
        texto.insert(tkinter.END,"Valor no válido en algun espacio\n")

def manual():
    manual = tkinter.Toplevel(ventana)
    manual.title("Manual de usuario")
    
    mostrar = tkinter.Label(manual, text=(
        "Botones:\n"
        "'Resolver': Luego de haber ingresado los valores en la matriz\neste botón resuelve el sistema lineal por el método de\neliminacion de Gauss-Jordan\n"
        "'Limpiar': Limpia todo en pantalla\n\n"
        "Extras/valores aceptados:\n'pi','e',numeros enteros, fracciones y decimales\n"
    ), justify="left")
    mostrar.pack(pady=10, padx=10)


ventana.mainloop()