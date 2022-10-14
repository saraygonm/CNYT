from libreria_vectores import *
import libcplx as lc
import matplotlib.pyplot as plot
import numpy as np



def ult_mati(mati):
    fila, columna = len( mati ), len( mati[0] )
    for tamaño in range(fila):
        new = []
        for j in range(columna):
            new.append( [( lc.modulo( mati[tamaño][j] )**2 ),0])   
        mati[tamaño]= new
    return mati


def sistemaprobabilistico_comple(mati, vec, veces):
    if (veces >= 0) and (type(veces) is int):
        tamaño  = len(vec)
        #copia matriz
        igual = mati[:]
        for tamaño in range(veces ):
            mati = multiplicacion(mati, igual)
        return ult_mati(mati)
    return -1


def sistemaprobabilistico(mati, vec, veces):
    if (veces >= 0) and (type(veces) is int):
        tamaño = len(vec)
        for tamaño in range(veces):
            vec = accion(mati, vec)
        return vec
    return -1

#experimento matriz booleana   
def experi_bolean_mat(veces,mat,vec):
    if (veces >= 0 and type(veces) is int):
        for rep in range(veces):
            vec = accion(mat, vec)      
        return vec

def multipleslitexperiment_cuantico(mati , vec, veces ):
    return sistemaprobabilistico_comple(mati , vec, veces ) 


def multipleslitexperimento(mati,vec,veces):
        return  sistemaprobabilistico(mati,vec,veces)
    

def grafico(vector):
    tamaño = len(vector)
    x = np.array([x for x in range(tamaño)])
    y = np.array([round(vector[x][0]*100,2) for x in range(tamaño)])

    plot.bar(x,y, color ='g', align='center')
    plot.title('Probabilidades del vector')
    plot.show()

    
matriz_doble_rendija = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
           [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
           [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
           [[0, 0], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
           [[0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
           [[0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [0, 0],[1, 0], [0, 0], [0, 0]],
           [[0, 0], [0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
           [[0, 0], [0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
       
estado_inicial = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

res = accion(multipleslitexperiment_cuantico(matriz_doble_rendija[:],estado_inicial[:], 2),  estado_inicial)
print(grafico( res))