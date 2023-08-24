import unittest
from Libreria_Operaciones_Complejos import suma, producto, resta, division, modulo, conjugado, fase

class TestComplexMathOperations(unittest.TestCase):
    def test_suma(self):
        resultado = suma((3, 4), (1, 2))
        self.assertEqual(resultado, (4, 6))

        resultado = suma((-2, -5), (-3, -1))
        self.assertEqual(resultado, (-5, -6))

    def test_producto(self):
        resultado = producto((3, 4), (1, 2))
        self.assertEqual(resultado, (-5, 10))

        resultado = producto((-2, -5), (-3, -1))
        self.assertEqual(resultado, (1, 17))

    def test_resta(self):
        resultado = resta((3, 4), (1, 2))
        self.assertEqual(resultado, (2, 2))

        resultado = resta((-2, -5), (-3, -1))
        self.assertEqual(resultado, (1, -4))
    def test_division(self):
        resultado = division((3, 4), (1, 2))
        self.assertEqual(resultado, (4, 6))

        resultado = division((-2, -5), (-3, -1))
        self.assertEqual(resultado, (-5, -6))

    def test_modulo(self):
        resultado = modulo((3, 4))
        self.assertEqual(resultado, 5 )

        resultado = modulo((-2, -5))
        self.assertEqual(resultado, 29**(1/2))
        
    def test_conjugado(self):
        resultado = conjugado((3, 4))
        self.assertEqual(resultado, (3, -4))

        resultado = conjugado((-2, -5))
        self.assertEqual(resultado, (-2, 5))
    def test_fase(self):
        resultado = fase((3, 4))
        self.assertEqual(resultado, 59.03344707)

        resultado = fase((-2, -5))
        self.assertEqual(resultado, 75.77621168)


if __name__ == '__main__':
    unittest.main()
