from Complex import *
import unittest

class TestComplexMethods(unittest.TestCase):
    def setUp(self):
        self.z = Complex(5, 3)
        self.z_conj = Complex(5, -3)
        self.v = Complex(1, 6)
        self.u = Complex(-1, -6)
        self.u_conj = Complex(-1, 6)
        self.z1 = Complex(5, 3)

    def tearDown(self):
        self.z = None
        self.v = None
        self.z1 = None
    
    def test_equality(self):
        self.assertEqual(self.z, self.z1)
        self.assertNotEqual(self.z, self.v)
        self.assertNotEqual(self.z, self.u)

    def test_conjugation(self):
        self.assertEqual(Complex.conjugate(self.z), self.z_conj)
        self.assertEqual(Complex.conjugate(self.u), self.u_conj)
        self.assertEqual(Complex.conjugate(self.u_conj), self.u)
    
    def test_arithmetic(self):
    # Simple arithmetic
        self.assertEqual(self.z + self.v, Complex(6, 9))
        self.assertEqual(self.z - self.v, Complex(4, -3))
    
    def test_unary(self):
        self.assertEqual(-self.v, self.u)
        self.assertNotEqual(-self.v, -self.u)
        self.assertNotEqual(-self.z, self.z1)
        self.assertEqual(-self.z, -self.z1)

    def test_power(self):
        self.assertEqual(self.z**2, Complex(16, 30))
        self.assertEqual(Complex(0,0)**2, Complex(0, 0))
        self.assertEqual(Complex(1,0)**2, Complex(1, 0))
        self.assertEqual(Complex(2,0)**2, Complex(4, 0))
        self.assertEqual(Complex(0,1)**2, Complex(-1, 0))

    def test_polar(self):
        self.assertEqual(round(self.z.rad, 3), 5.831)
        self.assertEqual(round(self.z.theta, 3), 0.540)
        self.assertEqual(round(self.u.rad, 3), 6.083)
        self.assertEqual(round(self.u.theta, 3), 4.547)
    
    def test_inner_product(self):
        A = [Complex(1,1), Complex(1,-1), Complex(-1,1), Complex(-1, -1)]
        B = [Complex(3,-4), Complex(6,-2), Complex(1,2), Complex(4,3)]

        c = Complex(1, 5)
        self.assertEqual(c, Complex.inner_product(A,B))

if __name__ == "__main__":
    unittest.main()
