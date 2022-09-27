'''LIBRERIA CUANTICA  BASICA, OBSERVABLES Y MEDIDAS
desarrollado por: Saray Alieth Mendivelso Gonzalez
'''
import math 
from libreria_vectores import *
from libcplx import *

def probabilidad(vector, posi):
    tamaño= norm_vec(vector)
    if (0 <= posi <= len(vector)):
        return modulo(vector[posi]**2/ tamaño**2, False)


def norm_vec(vec):
    operator = 0
    for i in range(len(vec)):
        operator += (abs(vec[i]))**2
    norm = math.sqrt(operator)
    return norm
print(norm_vec([2,3]))

def normalizar(vect):
    lista=[]
    for i in vect:
        value = (1/norm_vec(vect)) * i
        lista.append(value)
    return lista
print(normalizar([[2,3][1,2]]))


