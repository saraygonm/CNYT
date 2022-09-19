#RUEBA DE LIBRERIA OPERACIONES CON NUMEROS COMPLEJOS
#desarrollado por: Saray Alieth Mendivelso Gonzalez

import unittest
import math
import libreria_vectores as lcp

class Test_libcplx(unittest.TestCase):

    def test_suma_vectores8(self):
        vec1,vec2 = [1,2],[3,4]
        self.assertEqual(lcp.suma_vectores([4+5j,2+3j],[2+3j,1+2j]), [(6+8j), (3+5j)])
    def test_inverso_adi(self):
        self.assertEqual(lcp.inverso_adi([6+5j]), [-6-5j])
    def test_escalar_vec(self):
        self.assertEqual(lcp.inverso_adi([6+5j]), [-6-5j])
    def test_mat_comp_sum(self):
        self.assertEqual(lcp.mat_comp_sum([(4,5),(2,3)],[(1,3),(1,2)]), [[5, 8], [3, 5]])
    def test_mat_inversa(self):
        self.assertEqual(lcp.mat_inversa([(4,5),(2,3)]), [[-4, -5], [-2, -3]])
    def test_mat_inversa(self):
        self.assertEqual(lcp.mat_inversa([(4,5),(2,3)]), [[-4, -5], [-2, -3]])
    def test_esc_mat(self):
        self.assertEqual(lcp.esc_mat(6,[[4+5j,2+3j,4+2j],[4+9j,1+3j,5+3j]]),[[(24+30j), (12+18j), (24+12j)], [(24+54j), (6+18j), (30+18j)]])
    def test_mat_transpuesta(self):
        self.assertEqual(lcp.mat_transpuesta([[4+5j,2+3j],[1+3j,5+3j]]),[[(4+5j), (1+3j)], [(2+3j), (5+3j)]])
    def test_conj_mat(self):
        self.assertEqual(lcp.conj_mat([[4+5j,2+3j],[1+3j,5+3j]]), [[(4-5j), (2-3j)], [(1-3j), (5-3j)]])
    def test_multiplicacion(self):
        self.assertEqual(lcp.multiplicacion([(4,5),(2,3)],[(1,3),(1,2)]), [[8, 10], [12, 12]])
    def test_accion(self):
        self.assertEqual(lcp.accion([[(2,-3),(-5,0)] ], [[(9,6),(2,8)],[(4,9),(3,8)]]), [[(36, -15), (-10, -40)]])
    def test_dot_proud(self):
        self.assertEqual(lcp.dot_prod([4+5j,2+3j],[2+3j,1+2j]),(-8+16j))
    def test_norm_vec(self):
        self.assertEqual(lcp.norm_vec([4+5j,2+3j]),7.3484692283495345)
    def test_distance(self):
        self.assertEqual(lcp.distance([4+5j,2+3j],[2+3j,1+2j]), 3.1622776601683795)
    def check_unit(self):
        self.assertEqual(lcp.check_unit([[(0,1,3),(0,1,8)]]),'La matriz no es cuadrada, queda descartada automáticamente y no es unitarias')
    
if __name__ == '__main__':
    unittest.main()

