#PRUEBA EJERCICIOS_OBSERVABLE
#desarrollado por: Saray Alieth Mendivelso Gonzalez

import unittest
from ejercicios_observable import *

class Test_observables(unittest.TestCase):
    
    def test_ejercicio_4_3_1(self):
        self.assertEqual(ejercicio_4_3_1([[0,1],[0,0]]) ,[[[1.0, 0.0], [-1.0, 0.0]], [[0.0, 0.0], [2.004168360008973e-292, 0.0]]])
    def test_ejercicio_4_3_2(self):
        self.assertEqual(ejercicio_4_3_2([[0,1],[1,0]]) , [0.0, 0.0])
    def test_ejercicio_4_4_1(self):
        self.assertEqual(ejercicio_4_4_1([[[1,1],[1,0]],[[1,0],[0,0]]]), False)
    def test_ejercicio_441(self):
        self.assertEqual(ejercicio_441([[[1,1],[1,0]],[[1,0],[0,0]]],[[[1,1],[1,0]],[[1,0],[0,0]]]), False)   
    def test_ejercicio_4_4_2(self):
        vec = [[1,0], [0,0], [0,0], [0,0]]
        mati = [[[1, 0], [0, 0]],[[0, 1/math.sqrt(2)], [0, 0]]]
        self.assertEqual(ejercicio_4_4_2(mati,vec,3), [[1.0, 0.0], [0.4999999999999999, 0.0]])
if __name__ == '__main__':
    unittest.main()