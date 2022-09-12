# LIBRERIA OPERACIONES CON VECTORES COMPLEJOS 
### _Creado por Saray Alieth Mendivelso Gonzalez_
La presente librería desarrollada en el lenguaje python le proporcionara una serie de operaciones con Vectores complejos, los cuales se representan mediante la forma [a + bi] donde a es la parte real y b la imaginaria. 

Puede descargar una copia del proyecto mediante el linK del repositorio https://github.com/saraygonm/CNYT
###### OPERACIONES DE LA LIBRERIA DE VECTORES COMPLEJOS 
-  ###### SUMA VECTORES: esta operacion consta de sumar los terminos semejantes de cada uno de los vectores, es decir por un lado se efectua la suma de la parte real y por otro lado la parte imaginaria entre los vectores ingresados

-  ###### INVERSO(aditivo): Esta operacion consiste en cambiar por el signo contrario tanto de la parte real como de la parte imaginaria.
   
-  ###### MULTIPLICACION DE UN ESCALAR POR UN VECTOR: Para realizar dicha multiplicacion se debe multiplicar el escalar por cada termino del vector.
  
-  ###### ADICION DE MATRICES : consiste en sumar componente a componente los elementos de las matrices suministradas por el usuario
 
-  ###### INVERSA (aditiva ) DE UNA MATRIZ : Esta operacion consiste en cambiar por el signo contrario solamente la parte imaginaria del numero complejo 

-  ###### MULTIPLICACION DE UN ESCALAR POR UNA MATRIZ:  Para realizar dicha multiplicacion se debe multiplicar el escalar por cada termino de la matriz.
   
-  ###### TRANSPUESTA DE UNA MATRIZ/VECTOR: Esta operacion consiste en cambiar las filas por las columnas.
  

-  ###### CONJUGADA DE UNA MATRIZ /VECTOR: Esta operacion consiste en cambiar por el signo contrario solamente la parte imaginaria de la matriz.
  

-  ###### ADJUNTA(daga) DE UNA MATRIZ/ VECTOR: se debe aplicar la conjugada  y a lo obtenido aplicar la traspuesta 
 

-  ###### PRODUCTO DE DOS MATRICES : Consiste en multiplicar los elementos de las filas (primera matriz) por las columnas de la (segunda matriz) y sumar los resultados.


-  ###### PRODUCTO INTERNO DE DOS VECTORES: Consiste en multiplicar los componentes de los vectores posicion a posicion y posteriormente sumar los resultados obtenidos

-  ###### NORMA DE UN VECTOR: Consiste en elevar al cuadrado  unicamente los numeros del vector, omitiendo la "i" solamente, es decir la parte imaginaria 
 


-  ###### DISTANCIA ENTRE DOS VECTORES: Consiste en restar los vectores componente a componente y luego a el valor obtenido se debe realizar la norma 


-  ###### REVISAR SI UNA MATRIZ ES UNITARIA: ES  unitaria si tiene inversa igual a su traspuesta conjugada.  Es decir debe satisfacer la siguiente condicion: 
    U • U* = U* • U =I

-  ###### REVISAR SI UNA MATRIZ ES HERMITANIA: Es hermitania si la matriz es cuadrada  y debe satisfacer el hecho de ser igual a su transpuesta conjugada.
   A = A*


  
##### PREREQUISITOS 
En cuanto a los prerequisitos se debe tener el entorno de PyCharm, tambien se debe crear una cuenta en GitHub, pues alli se creara el repositorio que contendra principalmente la libreria, las pruebas de la misma y el read_me.

##### INSTALANDO 
- Instalación Pycharm:
1) ingresar al siguiente link  con el fin de descargar la app: https://www.jetbrains.com/es-es/pycharm/download/#section=windows
2) Elija la opcion de descargar que encuentra bajo 'Community
3) Una vez descargada la app, puede eligir el sistema operativo deseado.
4) Por ultimo abra el archivo descargado, ejecutelo y acepte las condiciones que le aparecen.

##### EJECUTANDO LAS PRUEBAS
Las pruebas se ejecutaran por medio de la libreri Unittest, ya que nos proporsiona si los datos suministrados concuerdan con el resultado deseado.

> Ejm: def test_nombre.funcion:
      self.assertEqual(nombre.libreria.nombre.funcion((parte real,parte imaginaria),(parte real, parte imaginaria)), (Resultado esperado))
      
> def test_modulo(self):
        self.assertEqual(lcp.modulo((8 , -13)), (15.264337522473747))
        
##### CONSTRUIDO CON
Pycharm Community Edition 

##### AUTORES
Creadora libreria: Saray Alieth Mendivelso Gonzales

##### LICENCIA
El presente proyecto se ampara con la licencia GNU General Public License






