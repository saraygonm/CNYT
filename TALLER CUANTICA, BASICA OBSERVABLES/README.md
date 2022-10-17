# LIBRERIA CUÁNTICA BÁSICA, OBSERVABLES Y MEDIDAS
### _Creado por Saray Alieth Mendivelso Gonzalez_
La presente librería desarrollada en el lenguaje python le proporcionara una serie de operaciones con el fin de reconocer los observables de diferentes sitemas suministrados por el usuario.
Un observable se puede determinar gracias a las alteraciones que posee un estado en una serie de operaciones fisicas, diferenciando una cantidad y una cualidad.

Puede descargar una copia del proyecto mediante el linK del repositorio https://github.com/saraygonm/CNYT
###### OPERACIONES DE LA LIBRERIA
-  ###### Longitud del vector:

   Como su lo indica es una funcion que calcula la longitud de un vector cualquiera ingresado por el usuario
-   ###### Normalizacion:
    Esta Funcion permite normalizar al vector dividiendo su parte imaginaria y entera entre su longitud.
-   ###### Bra:
    Esta Funcion retorna la adjunta (transpuesta conjugada) de un vector
-   ###### Transicion:
    Permite calcular la transicion por medio del producto interno  que hay desde el primer vector suministrado al segundo

-   ###### Probability:
    Calcula la probabilidad de que un vector este en una posicion dada.

-   ###### Dos_cifras:
    Funcion que retorna de un numero sus dos cifras decimales.
-   ###### Matriz:
    Funcion que describe un observable y un vector ket.
-   ###### Variance:
    Permite calcular la varianza del observable en un estado en concreto
-   ###### describir:
    Funcion que describe un observable gracias a la varianza.

De igual modo se anexa la libreia titulada "ejercicios_observable" la cual da solucion a cuatro ejercicios relacionados con el tema del libro  Quantum computing  for computing scientists.

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







