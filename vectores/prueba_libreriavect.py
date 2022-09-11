#RUEBA DE LIBRERIA OPERACIONES CON NUMEROS COMPLEJOS
#desarrollado por: Saray Alieth Mendivelso Gonzalez

import unittest
import math
import libreria_vectores as lcp

class Test_libcplx(unittest.TestCase):

    def test_suma_vectores8(self):
        #vec1,vec2 = [1,2],[3,4]
        self.assertEqual(lcp.suma_vectores([4+5j,2+3j],[2+3j,1+2j]), [(6+8j), (3+5j)])
    def testinvers()
             
if __name__ == '__main__':
    unittest.main()

