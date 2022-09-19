from libreria_vectores import *
import libcplx as lc
import matplotlib.pyplot as plot
import numpy as np



def ult_mati(mati):
    fila, columna = len( mati ), len( mati[0] )
    for i in range(fila):
        new = []
        for j in range(columna):
            new.append( [( lc.modulo( mati[i][j] )**2 ),0])   
        mati[i]= new
    return mati


def sistemaprobabilistico_comple(mati, vec, veces):
    if (veces >= 0) and (type(veces) is int):
        tamaño  = len(vec)
        #copia matriz
        igual = mati[:]
        for i in range(veces ):
            mati = multiplicacion(mati, igual)
        return ult_mati(mati)
    return -1


def sistemaprobabilistico(mati, vec, veces):
    if (veces >= 0) and (type(veces) is int):
        tamaño = len(vec)
        for i in range(veces):
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
    data = len(vector)
    x = np.array([ x for x in range( data )])
    y = np.array([ round(vector[x][0]*100,2) for x in range( data )])

    plot.bar(x,y, color ='g', align='centro')
    plot.title('Probabilidades del vector')
    plot.show()
