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
def esc_mat(esc, mati):
    mat_esc = []
    for i in range(len(mati)):
        vec_esc = []
        for j in range(len(mati[0])):
            vec_esc.append(esc*mati[i][j])
        mat_esc.append(vec_esc)
    return mat_esc


#8. Transpuesta de una matriz/vector
def mat_transpuesta(mati):
    '''Se recibe una matriz cuadrada y retorna una matriz transpuesta
    (matriz)--> matriz transpuesta 
    '''
    for i in range(len(mati)):
        for j in range(len(mati)):
             if j < i:
                 mat =mati[i][j]
                 mati[i][j]=mati[j][i]
                 mati[j][i]=mat
    return mati


#9. Conjugada de una matriz
def conj_mat(mat1):
    mat_inv = []
    for i in range(len(mat1)):
        fil_sum = []
        for j in range(len(mat1[0])):
            fil_sum.append(mat1[i][j].conjugate())
        mat_inv.append(fil_sum)
    return mat_inv


#10. Adjunta (daga) de una matriz/vector
def adjoint(mati):
    mat_transpose = mat_transpuesta(mati)
    adjunta = conj_mat(mat_transpose(mat_transpose))
    return adjunta


#11. Producto de dos matrices (de tamaños compatibles)
def multiplicacion (mat1,mat2):
    row1, col1 = len( mat1 ),len( mat1[ 0 ] )
    row2, col2 =  len( mat2 ), len( mat2[ 0 ] )
     
    if ( col1 == row2 ):
        answ = [ [  ( 0,0 )  for t in range( col2 ) ] for x in range( row1 ) ]
        for i in range( row1 ):
            for j in range( col2 ): 
                current = ( 0, 0 ) 
                for k in range( row2 ):
                    mult =  lc.multi( mat1[ i ][ k ], mat2[ k ][ j ]  ) 
                    current =  lc.suma( current , mult )    
                answ[ i ][ j ]  = current
        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")


#12. Función para calcular la "acción" de una matriz sobre un vector.
def accion( mati, vector ):
    fila, col  = len( mati ), len( mati [ 0 ] )
    tamaño = len( vector )

    if  ( col == tamaño ):
        answ = [ False for c in range( fila  ) ]
        for i in range( fila ):
            And = True
            for j in range( col ):
                And = mati[ i ][ j ] and vector[ j ]  
                answ [ i ] = answ[ i ] or And 
        return answ 
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")


#13. Producto interno de dos vectores
def dot_prod(vec1, vec2):
    prod = 0
    for i in range(len(vec1)):
        prod += vec2[i]*vec2[i]
    return prod


#14. Norma de un vector
def norm_vec(vec):
    operator = 0
    for i in range(len(vec)):
        operator += (abs(vec[i]))**2
    norm = math.sqrt(operator)
    return norm


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
def isHermitian(mati):
    adj = adjoint(mati)
    print(adj)
    if mati == adj:
        return True
    else:
        return False
    
#print(isHermitian([[(5,0),(3,7)],[(3,-7) , (2,0) ] ]))
