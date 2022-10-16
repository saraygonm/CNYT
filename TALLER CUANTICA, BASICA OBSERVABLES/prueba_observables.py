#PRUEBA DE LIBRERIA  DE OBSERVABLES
#desarrollado por: Saray Alieth Mendivelso Gonzalez

import unittest
from observables2 import *

class Test_observables(unittest.TestCase):
    
    def testlongitud_vector(self):
        self.assertEqual(longitud_vector([[1,7],[2,2]]) ,7.615773105863909)
    def testnormalizacion(self):
        self.assertEqual(normalizacion([[9, 5], [1, 6], [7, 0], [0, 1], [4, -6], [-2, 1], [0, -2], [9, 1], [-5, 1], [1, 1]]) ,[(0.47172817652486326, 0.2620712091804796), (0.052414241836095915, 0.3144854510165755), (0.36689969285267143, 0.0), (0.0, 0.052414241836095915), (0.20965696734438366, -0.3144854510165755), (-0.10482848367219183, 0.052414241836095915), (0.0, -0.10482848367219183), (0.47172817652486326, 0.052414241836095915), (-0.2620712091804796, 0.052414241836095915), (0.052414241836095915, 0.052414241836095915)])
    def testbra(self):
        self.assertEqual(bra([[1,7],[2,2]]) ,[[1, -7], [2, -2]])
    def testtransicion(self):
        vec1= normalizacion([[1,4], [-3, -2], [1, 1], [3, 4], [5, 2], [-1, 3], [0, -1], [0, 1], [2, -4], [-1, -1]])
        vec2= normalizacion([[2, 2], [3, 6], [-8,-4], [-1, -2], [3, -5], [-6, 4], [0, 1], [2, -4], [0, 1], [1, 3]])
        self.assertEqual(transicion(vec1,vec2),[-0.13693063937629152, -0.19969051575709185])
    def testprobability(self):
        vector = [[-2,3],[5,5],[8,3],[4,9]]
        self.assertEqual(probability(vector,2), 0.3133047210300429)
    def testvariance(self):
        psi = normalizacion([[math.sqrt(2)/2,0], [0,math.sqrt(2)/2]])
        omega = [[[1,0],[-1,-1] ], [ [1,1],[2,1]]]
        self.assertEqual(variance(psi,omega), -0.25)
    def describir(self):
        pssi = normalizacion([[math.sqrt(2)/2,0],[0,math.sqrt(2)/2]])
        omega1 = [[[-1,0],[0,-1]], [[1,0],[0,1]]]
        self.assertEqual(variance(pssi,omega1), None)
if __name__ == '__main__':
    unittest.main()