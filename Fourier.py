from Complex import *
from Constants import e, pi

e = 2.718281828459045

def root_of_unity(k, n):
    if n % 2 != 0:
        raise ValueError
    principal_root = Complex.from_polar(1, 2.0*pi/n)
    return principal_root ** k

def naive_fourier_transform(x):
    N = len(x)

    if N % 2 != 0:
        raise ValueError

    # make complex vector from real vector
    x = [Complex.from_real(r) for r in x]

    # naive fourier transform
    X = [ sum([x[k] * Complex.conjugate(root_of_unity(k*n, N)) for k in range(N)]) for n in range(N)]

    return X
