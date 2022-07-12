import re
import matplotlib.pyplot as plt
xn=[]
hn=[]
centro_h=0
centro_f=0
c1=0
c2=0.0


def todo(elemen):
    if(len(elemen.split("/"))>1):
        elemens=elemen.split("/")
        return int(elemens[0])/int(elemens[1])
    else:
        return float(elemen)


# Está función convierte los strings que entran a flotantes para poder manejarlos
def string_int(lista):  
    list1=[]
    centro=-1
    numero = re.compile(r'\d')
    for i in range(len(lista)):
        if(lista[i].find("*") != -1):
            centro=i
            lista[i]=lista[i][:-1]
        if(numero.match(str(abs(float(lista[i]))))):
            list1.append(todo(lista[i]))
    return list1,centro

def resta():
    global xn, hn, sonido1, sonido2
    list_y = []
    if( len(xn) >= len(hn)):
        for i in xn:
            list_y.append(float(i))
    else:
        for i in hn:
            list_y.append(float(i))

    cnt = 0
    if ( len(xn) >= len(hn) ):
        for i in hn:
            list_y[cnt] -= float(i)
            cnt = cnt + 1

    else:
        for i in xn:
            list_y[cnt] -= float(i)
            cnt = cnt + 1

    return list_y,centro_f   

def suma():
    #No afectan los valores ya obtenidos.
    global xn, hn
    #creamos una lista
    list_y = []
    #hacemos una comparación del tamaño de lo que obtuvimos
    if( len(xn) >= len(hn)):
        for i in xn:
            #agregamos a al arreglo
            list_y.append(float(i))
    
    else:
        for i in hn:
            #agregamos a al arreglo
            list_y.append(float(i))

    conta = 0
    if ( len(xn) >= len(hn) ):
        for i in hn:
            #aumentamos
            list_y[conta] += float(i)
            conta = conta + 1

    else:   
        for i in xn:
            #aumentamos
            list_y[conta] += float(i)
            conta = conta + 1
            #regresamos el valor y el centro
    return list_y,centro_f


"""Convolución"""
def convolucion():
    #variables globales
    global xn, centro_f, hn, centro_h
    arr = (len(xn) + len(hn)) - 1 # tamaño
    list_aux = []

    for i in range(arr):
        
        list_aux.append(float(0))

    for i in range(0, len(xn)):
        
        for j in range(0, len(hn)):
        
            list_aux[i + j] += (xn[i] * hn[j] )

    NuevoCentro = (-1)*((0-centro_f)+(0-centro_h))

    return list_aux,NuevoCentro

"""Diezmación, es una operación que reduce muestras, 
también conocido como compresión en tiempo discreto
"""
def diezmacion():
#No afectarán los valores que se tengan anteriores a estos ya que es global
    global xn, centro_f, c1
#Para manipular los valores en este caso fragmento1, centro_f
    tam = len(xn)
    aux = centro_f
#Se declara list_aux como array ya que podrá contener valores de la gráfica
#Una vez diezmada
    list_aux = []
#En este for se toma el tamaño del fragmento1 el cual representa la secuencia dada
    for i in range(tam):
        list_aux.append(float(0))
#En este for es donde se verá el resultado de la diezmación de la señal
#El cual se dara por const_k
    for i in range(centro_f, tam, c1):
        list_aux[aux] = xn[i]
        aux = aux + 1

    aux = centro_f - 1
#Se acomoda el resultado en este for para mostrar el resultado de la diezmación
    for i in range(centro_f - c1, -1, -c1):
        list_aux[aux] = xn[i]
        aux = aux - 1

    return list_aux,aux


def desplazamiento():
    global xn, centro_f, c1
    return xn,centro_f + c1

def desplazamiento2():
    global hn, centro_f, c2
    return hn,centro_f + c2

def interpolacionZ():
    global xn, centro_f, c1
    arr = len(xn)
    aux = 0
    centro_aux = 0
    list_aux = []

    for i in range(arr * c1):
        list_aux.append(float(0))

    for i in range(arr):
        if (i == centro_f):
            centro_aux = aux
        list_aux[aux] = xn[i]
        aux = aux + 1
        for j in range(c1 - 1):
            list_aux[aux + j] = float(0)

        aux = aux + (c1 - 1)

    #centro_aux es el nuevo centro
    return list_aux,centro_aux


def interpolacionE():
    global xn, centro_f, c1
    arr = len(xn)
    centro_aux = 0
    aux = 0
    list_aux = []

    for i in range(arr * c1):
        list_aux.append(float(0))

    for i in range(arr):
        if (i == centro_f):
            centro_aux = aux
        list_aux[aux] = xn[i]

        aux = aux + 1

        for j in range(c1 - 1):
            list_aux[aux + j] = xn[i]

        aux = aux + (c1 - 1)

    # centro_aux es el nuevo centro
    return list_aux,centro_aux

def interpolacionL():
    global xn, centro_f, c1
    arr = len(xn)
    aux1 = float(0)
    centro_aux = 0
    aux = 0
    list_aux = []

    for i in range(arr * c1):
        list_aux.append(float(0))

    for i in range(arr):
        if( i == centro_f ):
            centro_aux = aux

        list_aux[aux] = xn[i]
        aux = aux + 1

        if( i < arr - 1):
            aux1 = (xn[i + 1] - xn[i]) / c1

        if( i == arr - 1):
            aux1 = (0 - xn[i]) / c1

        list_aux[aux] = xn[i] + aux1
        for j in range(1, c1 - 1):
            list_aux[aux + j] = list_aux[aux] + aux1

        aux = aux + (c1 - 1)

    return list_aux,centro_aux

def amplitenuacion2():
    global xn, centro_f, c2
    arr = len(xn)
    list_aux = []

    for i in range(arr):
        list_aux.append(float(0))

    for i in range(arr):
        list_aux[i] = xn[i] * c2

    return list_aux,centro_f

def amplitenuacion():
    global hn, centro_f, c1

    arr = len(hn)
    
    list_aux = []

    for i in range(arr):
    
        list_aux.append(float(0))

    for i in range(arr):
    
        list_aux[i] = hn[i] * c1

    return list_aux,centro_f

    
def printSalida(serie,centro):
    
    if(centro+1>len(serie)):
    
        maxi=centro+1
    
    else:
    
        maxi=len(serie)
    
    cad=""
    
    for i in range(maxi):
    
        if(i!=0):
    
            cad+=","
    
        try:
    
            cad+=str(serie[i])
    
            #print(i)
    
        except:
            
            cad+="0"
        if(i==centro):
            cad+="*"
    return cad
#Graf
def plotea(senal,centro):
    x=[]
    y=[]
    for i in range(len(senal)):
        x.append(int(i-centro))
        y.append(senal[i])
    plt.stem(x,y,use_line_collection=True,markerfmt="None")
    plt.xlabel('  ')
    plt.ylabel('  ')
    plt.show()