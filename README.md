# LIBRERIA OPERACIONES CON NUMEROS COMPLEJOS 
### _Creado por Saray Alieth Mendivelso Gonzalez_
La presente librería desarrollada en el lenguaje python le proporcionara una serie de operaciones con números complejos, los cuales son todas las raices cuadradas de los numeros primos y se representan mediante la forma (a + bi) donde a es la parte real y b la imaginaria. 

Puede descargar una copia del proyecto mediante el linK del repositorio https://github.com/saraygonm/CNYT
###### OPERACIONES DE LA LIBRERIA
-  ###### SUMA Y RESTA: esta operacion consta de sumar y/o restar los terminos semejantes, es decir por un lado se efectua la suma o resta de la parte real y por otro lado la parte imaginaria
   Ejm: (a ± c)  ± (b ± d)i
-  ###### MULTIPLICACIÓN: se requiere usar la propiedad distributiva del producto respecto de la suma teniendo en cuenta que   i =  √-1 
   Ejm: (a + bi) · (c + di) = (ac − bd) + (ad + bc)i
-  ###### DIVISIÓN: Para realizar la division se debe multiplicar por el conjugado del denominador  
   Ejm: (a + bi / c + di) =(a + bi/c + di) *( c - di/ c - di)
-  ###### MODULO: es un numero real, el cual mide el tamaño del numero complejo
   Ejm: |z|= √a^2 + b^2
-  ###### CONJUGADO: Esta operacion consiste en cambiar por el signo contrario solamente la parte imaginaria del numero complejo 
   Ejm: (a + bi) --> (a - bi)
-  ###### FASE: es el ángulo θ formado por el eje de las abscissas y el vector 
   Ejm: z = θ = atan( b/ a)
-  ###### REPRESENTACION POLAR A CARTESIANA: Para ello se debe usar la siguiente el modulo del numero complejo y multiplicar la parte real por el coseno del anguñlo y la parte imaginaria por el seno del angulo.
   Ejm: a = |z| * cos(θ); b = |z| * sen(θ)
-  ###### REPRESENTACION CARTESIANA A POLAR: Consiste en obtener el modulo para la parte real y la fase para la parte imaginaria,
   Ejm: a = |z|, b = θ = atan( b/ a)

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
