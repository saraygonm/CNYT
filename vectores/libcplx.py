#LIBRERIA OPERACIONES CON NUMEROS COMPLEJOS
#desarrollado por: Saray Alieth Mendivelso Gonzalez

import math

def sumacplx(c1,c2):
    return (c1[0] + c2[0], c1[1] + c2[1])
    
#OPERACION SUMA 
#ejemplo entrada 2+5,4+6
def suma(num1,num2):
    sumareal = num1[0] + num2[0]
    sumaimag = num1[1] + num2[1]
    return(sumareal,sumaimag)
#print(suma((2,3),(5,6)))

#OPERACION RESTA
def resta(num1,num2):
    restareal = num1[0] - num2[0]
    restaimag = num1[1] - num2[1]
    return(restareal,restaimag)

#OPERACION MULTIPLICACION 
def multi(num1,num2):
    multi1 = (num1[0] * num2[0]) - (num1[1] * num2[1])
    multi2 = (num1[0] * num2[1]) + (num1[1] * num2[0])
    return(multi1,multi2)

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
    conjugado = complex(num[0], num[1] * -1)
    return conjugado

#REPRESENTACION POLAR vec1 CARTESIANA
def polar_cart(num):
    amp = math.sqrt((((num[0]) ** 2) + (num[1]** 2))) #Python por defecto expresa ángulos en radianes
    angulo = math.atan((num[1] / num[0]))
   # print(amp,math.degrees(angulo)) #ángulo convertido vec1 radianes
    vec1 = (amp * math.cos(angulo))
    vec2 = (amp * math.sin(angulo))
    return(amp,math.degrees(angulo))

#REPRESENTACION CARTESIANA vec1 POLAR
def cart_polar(num):
    cuadrados = math.sqrt((num[0]**2) + (num[1]**2))
    angulo = fase(num)
    return(cuadrados, angulo)

#FASE DE UN NUMERO COMPLEJO
def fase(num):
    angulo = math.atan(num[1]/ num[0])
    return(angulo)
