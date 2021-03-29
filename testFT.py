from Fourier import *
from Complex import *
from math import sqrt
import unittest


class TestFourierTransforms(unittest.TestCase):
    def setUp(self):
        self.x = [0, sqrt(2)/2, 1, sqrt(2)/2, 0, -sqrt(2)/2, -1, -sqrt(2)/2];
        self.x_freqs = [Complex(0.0000, 0.0000), Complex(0.0000, -4.0000),\
                Complex(0.0000, 0.0000), Complex(0.0000, 0.0000),\
                Complex(0.0000, 0.0000), Complex(0.0000, 0.0000),\
                Complex(0.0000, 0.0000), Complex(0.0000, 4.0000)]

    # Assert fft fails on odd-length input
    def test_input_size(self):
        self.assertRaises(ValueError, naive_fourier_transform, [1])

    def test_naive_ft(self):
        X = naive_fourier_transform(self.x)

        for impl, truth in zip(X, self.x_freqs):
            self.assertEqual(round(impl, 4), round(truth, 4))

    def test_naive_idft(self):
        X = naive_fourier_transform(self.x)
        Y = naive_inv_fourier_transform(X)
        for observed, truth in zip(Y, self.x):
            self.assertEqual(round(observed, 4), round(truth, 4))
    
    def test_fft(self):
        X = fast_fourier_transform(self.x)

        for impl, truth in zip(X, self.x_freqs):
            self.assertEqual(round(impl, 4), round(truth, 4))

    def tearDown(self):
        x = []


if __name__ == "__main__":
    unittest.main()
