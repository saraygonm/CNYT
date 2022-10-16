#LIBRERIA OPERACIONES CON NUMEROS COMPLEJOS
#desarrollado por: Saray Alieth Mendivelso Gonzalez

import math

#OPERACION SUMA 
#ejemplo entrada 2+5,4+6
def suma(  num_1, num_2 ):
	res = [ num_1[ 0 ] + num_2[ 0 ],
			 num_1[ 1 ] + num_2[ 1 ] ]
	return res


#OPERACION RESTA
def resta(num_1, num_2):
	res = [num_1[0]-num_2[0],num_1[1]-num_2[1]]

	return res

def resta_vect(vect1,vect2):
    tam = len(vect1)
    if ( tam == len(vect2)): 
        for x in range(tam):
                vect1[x] = resta(vect1[x],vect2[x])    
        return vect1


#OPERACION MULTIPLICACION 
def multi_vectors(num1, num2):
	answ = [num1[0] * num2[0] - num1[1] * num2[1],num1[1] * num2[0] + num1[0] * num2[1]]
	return answ

def multi( vect1, vect2 ):
    cont = [0,0]
    for c in range( len( vect1) ):
        cont = suma(cont, multi_vectors(vect1[c] , vect2[c]))
    return cont

#OPERACION DIVISION
def div(num1,num2):
    numreal = (num1[0] * num2[0]) + (num1[1] * num2[1])
    denomreal = ((num2[0]**2) + (num2[1]**2))
    partereal = (numreal/denomreal)
    numimg = (num1[1] * num2[0]) - (num1[1] * num2[1])
    denomimg = ((num2[0]**2) + (num2[1]**2))
    parteimg = (numimg/denomimg)  
    return (partereal,parteimg)


#MODULO NUMERO COMPLEJO
def modulo(num):
    cuadrados = ((num[0]**2) + (num[1]**2))
    modulo = math.sqrt(cuadrados)
    return(modulo)

#CONJUGADO NUMERO COMPLEJO
def conjugado(num):
    conjugado = (num[0], -num[1])
    return conjugado

#REPRESENTACION POLAR A CARTESIANA
def polar_cart(num):
    amp = math.sqrt((((num[0]) ** 2) + (num[1]** 2))) #Python por defecto expresa ángulos en radianes
    angulo = math.atan((num[1] / num[0]))
   # print(amp,math.degrees(angulo)) #ángulo convertido a radianes
    a = (amp * math.cos(angulo))
    b = (amp * math.sin(angulo))
    return(amp,math.degrees(angulo))

#REPRESENTACION CARTESIANA A POLAR
def cart_polar(num):
    cuadrados = math.sqrt((num[0]**2) + (num[1]**2))
    angulo = fase(num)
    return(cuadrados, angulo)

#FASE DE UN NUMERO COMPLEJO
def fase(num):
    angulo = math.atan(num[1]/ num[0])
    return(angulo)
