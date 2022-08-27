#RUEBA DE LIBRERIA OPERACIONES CON NUMEROS COMPLEJOS
#desarrollado por: Saray Alieth Mendivelso Gonzalez

import unittest
import math
import libcplx as lcp

class Test_libcplx(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(lcp.suma((3,-1),(1 , 4)), (4,3))
    def test_resta(self):
        self.assertEqual(lcp.resta((3,-1),(1 , 4)), (2,-5))    
    def test_multi(self):
        self.assertEqual(lcp.multi((-3,-5),(7 , -9)), (-66,-8))
    def test_div(self):
        self.assertEqual(lcp.div((4,2),(2 , -3)), (0.15384615384615385,0.7692307692307693))
    def test_modulo(self):
        self.assertEqual(lcp.modulo((8 , -13)), (15.264337522473747))
    def test_conjugado(self):
        self.assertEqual(lcp.conjugado((3,-1)), (3,1))
    def test_polar_cart(self):
        self.assertEqual(lcp.polar_cart((2,1)), (2.23606797749979, 26.56505117707799))  
    def test_cart_polar(self):
        self.assertEqual(lcp.cart_polar((6,6)), (8.48528137423857, 0.7853981633974483)) 
    def test_fase(self):
        self.assertEqual(lcp.fase((2,1)), (0.4636476090008061)) 
             
if __name__ == '__main__':
    unittest.main()

