from Complex import *

def naive_fourier_transform(x):
    if len(x) % 2 != 0:
        raise ValueError
    X = [Complex.from_real(r) for r in x]
    return X
