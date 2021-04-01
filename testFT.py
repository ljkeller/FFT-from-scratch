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
        Y = naive_fourier_transform(self.x)
        X = naive_inv_fourier_transform(Y)
        for observed, truth in zip(X, self.x):
            self.assertEqual(round(observed, 4), round(truth, 4))
    
    def test_fft(self):
        X = fast_fourier_transform(self.x)

        for impl, truth in zip(X, self.x_freqs):
            self.assertEqual(round(impl, 4), round(truth, 4))

    def test_naive_ifft(self):
        Y = fast_fourier_transform(self.x)
        X = fast_inv_fourier_transform(Y)
        for observed, truth in zip(X, self.x):
            self.assertEqual(round(observed, 4), round(truth, 4))

    def test_iter_fft(self):
        X = iterative_fft(self.x)

        for impl, truth in zip(X, self.x_freqs):
            self.assertEqual(round(impl, 4), round(truth, 4))

    def test_bit_reverse(self):
        # This is the recurssion tree leaf idx ordering from left -> right
        # So if input vector was [0, 1, ..., 7] the recursion leaf nodes 
        # are: [0, 4, 2, 6, 1, 5, 3, 7]
        leaf_ordering = [0, 4, 2, 6, 1, 5, 3, 7]
        x = list(range(0,8))

        x_rev = bit_reverse_copy(x)

        for observed, truth in zip(x_rev, leaf_ordering):
            self.assertEqual(observed, truth)

    def tearDown(self):
        x = []

if __name__ == "__main__":
    unittest.main()
