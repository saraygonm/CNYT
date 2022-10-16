''''LIBRERIA OPERACIONES CON VECTORES Y MATRICES
Autora: Saray Alieth Mendivelso Gonzalez
'''
import libcplx as lc
import math

#1. Adicion de vectores complejos.
def suma_vectores(vec1, vec2):
    ''' 
    Funcion que permite efectuar la suma entre dos vectores complejo
    '''
    vec_suma = []
    if (len(vec1) == len(vec2)):
        for i in range(len(vec1)):
            vec_suma.append(vec1[i] + vec2[i])
        return vec_suma

    #else:
        #print("Para sumar dos vectores, sus dimensiones deben ser iguales")

#2. Inverso (aditivo) de un vector complejo.
def inverso_adi(vector):
    conj_vec = []
    for i in range(len(vector)):
        conj_vec.append((-1)*vector[i])
    return conj_vec


#3. Multiplicación de un escalar por un vector complejo.
def escalar_vec(esc, vec):
    vec_esc = []
    for i in range(len(vec)):
        vec_esc.append(esc*vec[i])
    return vec_esc


#5. Adición de matrices complejas.
def mat_comp_sum(mat1, mat2):
    mat_sum = []
    if (len(mat1) == len(mat2)) and (len(mat1[0]) == len(mat2[0])):
        for i in range(len(mat1)):
            fil_sum = []
            for j in range(len(mat1[0])):
                fil_sum.append(mat1[i][j]+mat2[i][j])
            mat_sum.append(fil_sum)
    return mat_sum


#6. Inversa (aditiva) de una matriz compleja.
def mat_inversa(mat1):
    mat_inv = []
    for i in range(len(mat1)):
        fil_sum = []
        for j in range(len(mat1[0])):
            fil_sum.append((-1)*mat1[i][j])
        mat_inv.append(fil_sum)
    return mat_inv

#7. Multiplicación de un escalar por una matriz compleja.
def multiEscalMat(complexNumber, mat):
    fila, columna = len(mat), len(mat[0])
    for i in range(fila):
        for j in range(columna):
            mat[i][j] = lc.multi_vectors(complexNumber , mat[i][j])

    return mat


#8. Transpuesta de una matriz/vector
def mat_transpuesta(mati):
    '''Se recibe una matriz cuadrada y retorna una matriz transpuesta
    (matriz)--> matriz transpuesta 
    '''
    fila,colum = len(mati), len(mati[0])
    if (type(mati[0][0]) is int):
        return mati
    resp= [[0 for rep in range (fila)] for i in range(colum)]
    for i in range(colum):
        for j in range(fila):
                resp[i][j] = mati[j][i]  
    return resp


#9. Conjugada de una matriz
def conjugated(num):
	res = [num[0], -num[1]]
	return res

def mat_conjugada(mat1):
    fila, colum = len(mat1), len(mat1[0])
    if (type(mat1[0][0]) is int):
        for i in range(fila):
            mat1[i] = conjugated(mat1[i])
        return mat1
    for i in range(fila):
        for j in range(colum):
            mat1[i][j] = conjugated(mat1[i][j])
    return mat1

#10. Adjunta (daga) de una matriz/vector
def adjoint( vector ):
    for x in range( len( vector )):
        vector[x] = conjugated( vector[x])
    return vector

#11. Producto de dos matrices (de tamaños compatibles)
def multiplicacion(mat1, mat2):
    '''se reciben dos matrices y retorna una matriz con el resultado de la multiplicacion ente las matrices suministradas 
    (matriz, matriz) -> matriz con el resultado de las multiplicaciones
    '''
    if len(mat1) == len(mat2[0]):
        mat_mult = []
        for i in range(len(mat1)):
            vect_mult = []
            for j in range(len(mat2[0])):
                multi = 0
                for k in range(len(mat2)):
                    multi += mat1[i][j]*mat2[j][i]
                vect_mult.append(multi)
            mat_mult.append(vect_mult)
        return mat_mult
    else:
        print("No puedo calcular el producto por la incompatibilidad de las filas y columnas")

def multiplicaMat(mat1, mat2):
    fila1,col1 =len(mat1),len(mat1[0])
    fila2,col2 = len(mat2), len(mat2[0])
    if (col1 == fila2):
        res = [[(0,0) for t in range(col2)] for x in range(fila1)]
        for i in range(fila2):
            for j in range(col2):
                actual = (0,0) 
                for k in range(fila2):
                    multipl = lc.multi_vectors(mat1[i][k], mat2[k][j] ) 
                    actual = lc.suma(actual, multipl) 
                    res[i][j] = actual
        return res

#12. Función para calcular la "acción" de una matriz sobre un vector.
def accion(vec1, vec2):
    fila = len(vec1)
    columna = len(vec1[0])
    mati = [(0, 0)] * columna
    respu = [mati] * fila
    for j in range(fila):
        mati = [(0, 0)] * columna
        respu[j] = mati
        for k in range(columna):
            respu[j][k] = lc.multi(vec1[j][k], vec2[j][k])
    return respu
#accion matriz sobre vect

def action2(mati, vector):
    fila, col  = len(mati), len(mati[0])
    tam = len(vector)
    if  (col == tam):
        answ = [[0,0] for x in range(fila)]
        for i in range(fila):
            for j in range(col):
                multip = lc.multi_vectors(mati[i][j], vector[j] )
                answ[i] = lc.suma(answ[i], multip)
        return answ
  



#13. Producto interno de dos vectores
def dot_prod(vect,vect2):
    return lc.multi(adjoint(vect),vect2)



#14. Norma de un vector
def norm_vec(vec):
    cont = 0
    for i in range(len(vec)):
        cont += (abs(vec[i]))**2
    norm = math.sqrt(cont)
    return norm
#print(norm_vec([2,3]))


#15. Distancia entre dos vectores
def distance(vec1, vec2):
    vec_rest = []
    for i in range(2):
        vec_rest.append(vec1[i]-vec2[i])
    dist = norm_vec(vec_rest)
    return(dist)



#16. Revisar si una matriz es unitaria
def check_unit(mati):
    if len(mati) == len(mati[0]):
        identity = [[0 for rep in range(len(mati))]for rep in range(len(mati))]
        for i in range(len(mati)):
            for j in range(len(mati)):
                if i == j:
                    identity[i][j] = 1
        for rep in range(len(identity)):
            print(identity[rep])
        checker = False
        adj = adjoint(mati)
        mat_mult = multiplicacion(mati, adj)
        for i in range(len(mati)):
            for j in range(len(mati)):
                if mati[i][j] == mat_mult[i][j]:
                    checker = True
        return checker
    else:
        print("La matriz no es cuadrada, queda descartada automáticamente y no es unitarias")


#17. Revisar si una matriz es Hermitiana
def adjointmat(mati):
    res = mat_conjugada(mat_transpuesta(mati))
    return res

def isHermitian(mati):
    res = adjointmat (mati)
    return  str(res) == str(mati)
    
#print(isHermitian([[(5,0),(3,7)],[(3,-7) , (2,0) ] ]))

#18) revisar si es identidad una matriz
def identidad(mati):
    fila,  columna  = len(mati),len(mati[0])
    mati=[[[] for i in range(columna)] for j in range(fila)]
    for i in range(fila):
        for j in range(columna):
            if i==j:
                mati[i][j]=[1,0]
            else:
                mati[i][j]=[0,0]
    return mati
