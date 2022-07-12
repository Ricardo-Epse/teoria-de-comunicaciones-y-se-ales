from  tkinter import *
import time
import wave
import struct
import Funciones
import numpy as np
import matplotlib.pyplot as plt
import os.path

suma=Funciones.suma
resta=Funciones.resta
convolucion=Funciones.convolucion
diezmacion=Funciones.diezmacion
desplazamiento=Funciones.desplazamiento
interpolacionZero=Funciones.interpolacionZ
interpolacionEsca=Funciones.interpolacionE
interpolacionLineal=Funciones.interpolacionL
ampliatenuacion=Funciones.amplitenuacion
ampliatenuacion2=Funciones.amplitenuacion2
desplazamiento2=Funciones.desplazamiento2

def Enviar():
    global resultado
    if(senal1.get() != "" and senal2.get()!=""):
        Funciones.xn,Funciones.centro_f=Funciones.string_int(senal1.get().split(","))
        Funciones.hn,Funciones.centro_h=Funciones.string_int(senal2.get().split(","))
        Funciones.c2=Funciones.todo(k.get())
        Funciones.c1=int(Funciones.c2)
        resultado=globals()[v.get()]()
        senals.set(Funciones.printSalida(resultado[0],resultado[1]))
        print("Señal Salida:"+str(resultado[0]))

    Funciones.c2=Funciones.todo(k.get())
    Funciones.c1=int(Funciones.c2)
    resultado=globals()[v.get()]()

    print("Señal 1:"+str(Funciones.xn))
    print("Centro:"+str(Funciones.centro_f))
    print("Señal 2:"+str(Funciones.hn))
    print("Centro:"+str(Funciones.centro_h))
    print("Constante k:"+str(Funciones.c1))

    #
    try:
        print("Centro:"+str(resultado[1]))
    except:
        a=0
    #
    Funciones.plotea(resultado[0],resultado[1])

def Graf1():

    Funciones.plotea(Funciones.xn,Funciones.centro_f)

def Graf2():
    Funciones.plotea(Funciones.hn,Funciones.centro_h)

t1=[]
t2=[]
raiz=Tk()
miFrame=Frame(raiz,bd=15)
miFrame.configure(bg="Tomato1")
miFrame.pack()
raiz.title("Práctica 2 - TEORÍA DE COMUNICACIONES Y SEÑALES - 3CV10")
raiz.configure(bg="Tomato1")
resultado=[]
senal1=StringVar()
k=StringVar()
senal2=StringVar()
senals=StringVar()

#Label Inicio
titulo = Label(miFrame,text = "- I N T E G R A N T E S -")
titulo.configure(fg="white",bg="Tomato2",font=("Arial",12))
titulo.pack()
titulo.grid(row=0,column=5) 
Integrantes = Label(miFrame,text="\n *GONZALES MORA JAVIER \n\n *PÉREZ SERENO RICARDO ERICK \n\n*VIORATO LOZADA OSMAR\n")
Integrantes.grid(row=1,column=5)
Integrantes.configure(fg="white",bg="Tomato3",font=("Helvetica",9))

#Label Funciones
label=Label(miFrame,text="\nF U N C I O N E S\n",padx=15)
label.configure(bg="Tomato1",font=("Arial",12))
label.grid(row=12,column=5)

#Label Instrucciones Central
Instrucciones1 = Label(miFrame,text = "\nIngrese las señales separadas por ','")
Instrucciones1.configure(bg="Tomato1",font=("Arial",12))
Instrucciones1.grid(row= 4,column = 5)

#Label Ejemplo
Instrucciones1 = Label(miFrame,text = "Ejemplo: 1,2,3,4,5")
Instrucciones1.configure(bg="Tomato1",font=("Arial",9))
Instrucciones1.grid(row= 5,column = 5)

#Señal1
labelSenal1=Label(miFrame,text=" x(n):")
labelSenal1.configure(fg="white",bg="Tomato2",font=("Arial",12))
labelSenal1.grid(row=6,column=3,padx=15)
cuadroSenal1=Entry(miFrame,textvariable=senal1)
cuadroSenal1.grid(row=6, column=4,padx=15)

#Señal2
labelCentro1=Label(miFrame,text="h(n):")
labelCentro1.configure(fg="white",bg="Tomato2",font=("Arial",12))
labelCentro1.grid(row=6,column=6)
cuadroSenal2=Entry(miFrame,textvariable=senal2)
cuadroSenal2.grid(row=6, column=7)

#Constante k
labelCentro2=Label(miFrame,text="k:")
labelCentro2.configure(fg="white",bg="Tomato2",font=("Arial",12))
labelCentro2.grid(row=7,column=3,pady=10)
cuadroCentro2=Entry(miFrame,textvariable=k)
cuadroCentro2.grid(row=7, column=4)

#Señal resultado
labelCentro1=Label(miFrame,text="Señal Resultado:")
labelCentro1.grid(row=7,column=6)
labelCentro1.configure(fg="white",bg="Tomato2",font=("Arial",12))
cuadroSenal2=Entry(miFrame,textvariable=senals)
cuadroSenal2.grid(row=7, column=7)


v = StringVar(raiz, "Suma")


values = {"Suma" : "suma",
          "Resta" : "resta",
          "Amplificacion h(n)":"ampliatenuacion",
          "Amplificacion x(n)":"ampliatenuacion2",
          "Diezmacion" : "diezmacion",
          "Desplazamiento x(n)":"desplazamiento",
          "Desplazamiento h(n)":"desplazamiento2",
          "Interpol (z)":"interpolacionZ",
          "Interpol(e)":"interpolacionE",
          "Interpol (l)":"interpolacionL",
          "Convolucion" : "convolucion"
          }

i=1
for (text, value) in values.items():
    rb=Radiobutton(miFrame, text = text, variable = v,
    value = value)
    rb.grid(row=16,column=i)
    i+=1

botonEnvio=Button(raiz,text="Enviar",command=Enviar);
botonEnvio.pack()
botonEnvio=Button(raiz,text="Grafica 1",command=Graf1);
botonEnvio.pack()
botonEnvio=Button(raiz,text="Grafica 2",command=Graf2);
botonEnvio.pack()

raiz.mainloop()