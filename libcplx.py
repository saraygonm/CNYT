#LIBRERIA OPERACIONES CON NUMEROS COMPLEJOS
#desarrollado por: Saray Alieth Mendivelso Gonzalez

import math

#OPERACION SUMA 
def suma(num1,num2):
    sumareal = num1[0] + num2[0]
    sumaimag = num1[1] + num2[1]
    return(sumareal,sumaimag)

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
    conjugado = (num[0], num[1] * -1)
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

def main():
    a=(2,1)
    b=(1,4)
    print(polar_cart(a))
main()
