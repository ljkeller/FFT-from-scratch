from Fourier import *
import unittest


class TestFourierTransforms(unittest.TestCase):
    def setUp(self):
        self.x = [0, 0.7071, 1, 0.7071, 0, -0.7071, -1, -0.7071];
        self.x_freqs = [Complex(0.0000, 0.0000), Complex(0.0000, 4.0000),\
                Complex(0.0000, 0.0000), Complex(0.0000, 0.0000),\
                Complex(0.0000, 0.0000), Complex(0.0000, 0.0000),\
                Complex(0.0000, 0.0000), Complex(0.0000, 4.0000)]

    # Assert fft fails on odd-length input
    def test_input_size(self):
        self.assertRaises(ValueError, naive_fourier_transform, [1])

    def test_naive_ft(self):
        X = naive_fourier_transform(self.x)
        for impl, truth in zip(X, self.x_freqs):
            self.assertEqual(impl, truth)

    def tearDown(self):
        x = []


if __name__ == "__main__":
    unittest.main()
