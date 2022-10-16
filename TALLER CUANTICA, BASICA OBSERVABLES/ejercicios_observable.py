'''LIBRERIA EJERCICIOS OBSERVABLES
desarrollado por: Saray Alieth Mendivelso Gonzalez
'''
import numpy as np
from numpy import linalg as Alg
from observables2 import *
from libcplx import *


def lectura(vector):
    """Funcion que lee de la libreria numpy los vectores propios  a la presente libreria"""
    psi = []
    for el in vector:
        psi.append([el.real, el.imag])
    return psi

def eigen_valu(omega):
    observable = np.array(omega)
    j, k = np.linalg.eig(observable)

    return j, k

def ejercicio_4_3_1(observable):
    '''Funcion que retorna los estados en los que puede transitar el spin'''
    j, k = eigen_valu(observable)
    psi = []
    for i in k:
        new = lectura(i)
        psi.append(new)
    return psi
#print(ejercicio_4_3_1([[0, 1],[0, 0]]))

def traductor(val):
    """Traduce todos los valores propios de la libreria numpy a nuestra libreria"""
    return [val.real, val.imag]



def ejercicio_4_3_2(observable):
    '''Funcion que retorna la media  de la distribucion del spin'''
    vecti = [[1, 0], [0, 0]]
    j, k = eigen_valu(observable)
    vvector_nul = [0, 0]
    for i in range(len(j)):
        tra = traductor(j[i])
        lec= lectura(k[:, i])
        prob = multi_vectors(tra, [longitud_vector([transicion(lec, vecti)]) ** 2, 0])
        vvector_nul = suma(vvector_nul, prob)
    return vvector_nul


#[0, 1],[1, 0]]))

def mat_unitaria(mati):
    fila, colum = len(mati), len(mati[0])
    if fila == colum:
        adjoint = adjointmat(mati)
        return (multiplicaMat(mati, adjoint) == identidad(mati)) or (multiplicaMat(mati, adjoint) == multiplicaMat(adjoint, mati))

def ejercicio_4_4_1(vect):
    '''Funcion que determina si el unico vector ingresado es unitario'''
    return mat_unitaria(vect)

def ejercicio_441(vect,vect2):
    '''Funcion que Verifica si dos vectores son unitarios'''
    return mat_unitaria(multiplicaMat(vect,vect2))

#u1 = [[[1,1],[1,0]],[[1,0],[0,0]]]
#print(ejercicio_441(u1,u1))

def ultima_mat(mati):
    fila, column = len(mati), len(mati[0])
    for i in range(fila):
        for j in range(column):
            mati[i][j] = modulo(mati[i][j]) ** 2
    return mati

def sistema_probabilistico(mati, vectIni, veces):
    if (veces > 0) and (type(veces) is int):
        tam = len(vectIni)
        mat = mati[:]

        for j in range(veces):
            mati = multiplicaMat(mati, mat)

        return ultima_mat(mati)
    return -1

def ejercicio_4_4_2(mat,vec,pos):
    '''Funcion que determina si el unico vector ingresado es unitario'''
    return sistema_probabilistico(mat,vec,pos)
raiz = 1 / math.sqrt(2)
vectIni = [[1, 0], [0, 0], [0, 0], [0, 0]]
mati = [[[1, 0], [0, 0]],[[0, 1/math.sqrt(2)], [0, 0]]]
print(ejercicio_4_4_2(mati,vectIni,3))