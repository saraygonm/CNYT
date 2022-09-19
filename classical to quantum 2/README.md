# LIBRERIA SALTO DE LO CLASICO A LO CUANTICO 

### _Creada por Saray Alieth Mendivelso Gonzalez_
La presente librería desarrollada en el lenguaje python le proporcionara una simulacion en cuanto al salto de lo clasico a lo cuantico, mediante un experimento de canicas.

Puede descargar una copia del proyecto mediante el linK del repositorio https://github.com/saraygonm/CNYT/tree/master/classical%20to%20quantum%202

###### EXPLICACION DETALLADA DEL EXPERIMENTO 
-  ###### INICIO: Se colocaran diferentes cajas en donde se situaran n numero de canicas, las cuales se desplazaran entre las mismas cajas una cierta cantidad suminitrada por el usuario en un determinado lapso de tiempo 

-  ###### PALABRAS CLAVE:
    imaginemos la rrepresentacion de un grafo 
    ![image](https://user-images.githubusercontent.com/111905625/190960992-5657c524-eae3-4d26-9054-c638ac1db3dd.png)

    1) Nodo= caja
    2) Peso arco = cantidad de canicas que se desplazan
    3) arcos= direccion hacia donde se desplazan las canicas
   
-  ###### MULTIPLICACION DE UN ESCALAR POR UN VECTOR: Para realizar dicha multiplicacion se debe multiplicar el escalar por cada termino del vector.
  
-  ###### ADICION DE MATRICES : consiste en sumar componente a componente los elementos de las matrices suministradas por el usuario
 
-  ###### INVERSA (aditiva ) DE UNA MATRIZ : Esta operacion consiste en cambiar por el signo contrario solamente la parte imaginaria del numero complejo 

-  ###### MULTIPLICACION DE UN ESCALAR POR UNA MATRIZ:  Para realizar dicha multiplicacion se debe multiplicar el escalar por cada termino de la matriz.
   
-  ###### TRANSPUESTA DE UNA MATRIZ/VECTOR: Esta operacion consiste en cambiar las filas por las columnas.
  

-  ###### CONJUGADA DE UNA MATRIZ /VECTOR: Esta operacion consiste en cambiar por el signo contrario solamente la parte imaginaria de la matriz.
  

-  ###### ADJUNTA(daga) DE UNA MATRIZ/ VECTOR: se debe sacar los cofactores de la matriz/vector, revisar los signos y a lo obtenido aplicar la traspuesta 
 

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






