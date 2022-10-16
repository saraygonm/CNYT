'''LIBRERIA CUANTICA  BASICA, OBSERVABLES Y MEDIDAS
desarrollado por: Saray Alieth Mendivelso Gonzalez
'''
import numpy as num
import math 
from numpy import linalg as lin 
from libreria_vectores import *
from libcplx import *


def modulo(num):
    sumi = (num[0])**2 + (num[1]) **2
    resp = math.sqrt(sumi)
    return resp


def longitud_vector(vec):
    '''Funcion que calcula la longitud de un vector '''
    cont = 0
    for i in range(len(vec)):
        cont += (modulo(vec[i]))**2
        raiz = math.sqrt(cont)
    return raiz 
#print(longitud_vector([[1,7],[2,2]]))
        
def normalizacion(vec):
    """Funcion que normaliza un vector"""
    longitud = longitud_vector(vec)
    for i in range (len(vec)):
        imag = vec[i][0]/longitud
        real = vec[i][1]/longitud
        vec[i] = imag,real
    return vec
#print(normalizacion([[9, 5], [1, 6], [7, 0], [0, 1], [4, -6], [-2, 1], [0, -2], [9, 1], [-5, 1], [1, 1]]))

#Bra de un vector 
def bra(vec):
    return adjoint(vec)
#print((bra([[1,7],[2,2]])))
    

def transicion(vec1 ,vec2):
    '''Funcion que calcula la transicion entre un el vecto uno al dos'''
    return dot_prod(vec1,vec2)  

#vec1= normalizacion([[1,4], [-3, -2], [1, 1], [3, 4], [5, 2], [-1, 3], [0, -1], [0, 1], [2, -4], [-1, -1]])
#vec2= normalizacion([[2, 2], [3, 6], [-8,-4], [-1, -2], [3, -5], [-6, 4], [0, 1], [2, -4], [0, 1], [1, 3]])
#resp = transicion(vec1,vec2)
#print(resp)


def probability(vector, position):
    """Calcula la probabilidad de que un vector este en el estado dado( posicion )"""
    longi = longitud_vector(vector)
    if (0 <= position < len(vector)):
        return (modulo(vector[position])**2 / longi**2) 
#vector = [[-2,3],[5,5],[8,3],[4,9]]
#print(probability(vector,2))



#resta matrices 
def resta_mati(mat1, mat2):
    '''Funcion que resta dos matrices'''
    fila, columna  = len(mat1), len(mat1[0])
    for i in range(fila):
        mat1[i] = resta_vect(mat1[i], mat2[i])
    return mat1


def OmegaP(psi,omega):
    return dot_prod(action2(omega, psi),psi)[0]
    
#psi = normalizacion([[math.sqrt(2)/2,0], [0,math.sqrt(2)/2]])
#omega = [[[1,0],[0,-1]],[[0,1],[2,0]]]
#print(OmegaP(psi,omega))


def deltaP(omega,val):
    return resta_mati(omega ,multiEscalMat(val, identidad(omega)))


def dos_cifras(num, decima):
    '''Funcion que retorna de un numero sus dos cifras decimales'''
    num = "{:.2f}".format(num)
    num =  (num[:-1] if decima else num)
    return float(num)

def Matriz(mati, psi):
    '''Matriz que describa un observable y un vector ket'''
    action2(mati, adjoint(psi))
    vect = action2(mati, adjoint(psi))
    return dos_cifras(multi(vect,adjoint(psi))[0],False)

def variance(psi, omega):
    '''Funcion que calcula la varianza  del observable en el estado dado.'''
    val = dos_cifras(OmegaP(psi, omega),True)
    delta_1 = deltaP(omega,[val, 0.0])
    varianza = multiplicaMat(delta_1, delta_1)
    return Matriz(varianza,psi )
 
#psi = normalizacion([[math.sqrt(2)/2,0], [0,math.sqrt(2)/2]])
#omega = [[[1,0],[-1,-1] ], [ [1,1],[2,1]]]
#print(variance(psi,omega))

def describir(pssi,mati):
    '''Funcion que describe un observable'''
    if (isHermitian(mati)):
        mean = dos_cifras(OmegaP(pssi,mati),True)
        return[variance(pssi,mati),mean]
    return None

#pssi = normalizacion([[math.sqrt(2)/2,0],[0,math.sqrt(2)/2]])
#omega = [[[-1,0],[0,-1]], [[1,0],[0,1]]]
#print(describir(pssi,omega))


