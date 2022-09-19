# LIBRERIA SALTO DE LO CLASICO A LO CUANTICO 

### _Creada por Saray Alieth Mendivelso Gonzalez_
La presente librería desarrollada en el lenguaje python le proporcionara una simulacion en cuanto al salto de lo clasico a lo cuantico, mediante un experimento de canicas.

Puede descargar una copia del proyecto mediante el linK del repositorio https://github.com/saraygonm/CNYT/tree/master/classical%20to%20quantum%202

###### EXPLICACION DETALLADA DEL EXPERIMENTO 
-  ###### INICIO: Se colocaran diferentes cajas en donde se situaran n numero de canicas, las cuales se desplazaran entre las mismas cajas una cierta cantidad suminitrada por el usuario en un determinado lapso de tiempo 

-  ###### PALABRAS CLAVE:
    imaginemos la rrepresentacion de un grafo 
    
    
    ![image](https://user-images.githubusercontent.com/111905625/190961122-81af77b4-f466-40dd-aee5-96973a89a08e.png)g)

    1) Vertice o Nodo = caja
    2) Peso arco = cantidad de canicas que se desplazan
    3) Aristas = direccion hacia donde se desplazan las canicas
    4) Particulas= canicas
   
-  ###### REGLAS: 
    1) La sumatoria de Particulas debe ser el mismo.
    2) El peso del arco de un nodo a otro  debe sumar  1 exactamente, a excepcion de que el movimiento no se origine en el nodo
    3) se debe establecer un estado inicial el cual es un vector con las mismas dimensiones de la fila de la matriz 
  
  
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






