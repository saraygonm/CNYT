''''LIBRERIA OPERACIONES Classical to Quantum
Autora: Saray Alieth Mendivelso Gonzalez
'''
import libcplx as lc
import libreria_vectores as lib
import matplotlib as plot
import numpy as np
import math



def sisprobabilistico(vec, mati, veces):
    for i in range(veces):
        vec = lib.accion(mati, vec)
    return vec
print(sisprobabilistico([[2+5j,1+2j]], [[2+5j,1+1j],[1+1j,1+1j]], 2))


def matifinal(mati):
    for i in range(len(mati)):
        mat = []
        for j in range(len(mati[i])):
            mat.append([lc.modulo(mati[i][j]) ** 2, 0])
        mati[i] = mat
    return mati


def sistemaProbabilisticoCuantico(mati, vec, veces):
    cop = mati[:]
    for i in range(veces):
        mati = lib.multiplicacion(mati, cop)
    return matifinal(mati)


def accionBooleana(mati, vec):
    if len(vec) == len(mati[0]):
        mat = [False for i in range(len(mati))]
        for i in range(len(mati)):
            And = True
            for j in range(len(mati[i])):
                And = mati[i][j] and vec[j]
                mat[i] = mat[i] or And
        return mat


def experimento(mati, vec, veces):
    for i in range(veces):
        vec = accionBooleana(mati, vec)
    return vec


def multipleSlit(mati, vec, veces):
    return sisprobabilistico(mati, vec, veces)


def multipleSlitCuantico(mati, vec, veces):
    return sistemaProbabilisticoCuantico(mati, vec, veces)


