from Complex import *
from Constants import e, pi

e = 2.718281828459045

def root_of_unity(k, n):
    if n % 2 != 0:
        raise ValueError
    principal_root = Complex.from_polar(1, 2.0*pi/n)
    return principal_root ** k

# Wrapper that transforms input before fft call
def fast_fourier_transform(x):
    N = len(x)
    if N % 2 != 0:
        raise ValueError
    
    # make complex vector from real vector
    x = list(map(Complex.from_real, x))
    
    print(x)
    return fft(x)

def fft(x):
    N = len(x)
    if N == 1:
        return x
    # root of unity generator, the principal root
    rou_n = Complex.conjugate(Complex.from_polar(1, 2.0*pi/N))
    # current root of unity, starts at (0, 1i)
    rou_k = Complex.from_polar(1, 0)

    # Even odd split
    x_evens = x[::2]
    x_odds = x[1::2]

    # Perform FFT on even and half matrices (T(n/2) portion of recurrence)
    y_evens = fft(x_evens)
    y_odds = fft(x_odds)

    # generate output list up front
    y = [None] * N
    for k in range(0, N//2):
        y[k] = y_evens[k] + rou_k * y_odds[k]
        y[k + N//2] = y_evens[k] - rou_k * y_odds[k]
        rou_k = rou_k*rou_n
    print(y)
    return y

def naive_fourier_transform(x):
    N = len(x)
    if N % 2 != 0:
        raise ValueError

    # make complex vector from real vector
    x = list(map(Complex.from_real, x))

    # naive fourier transform
    return [ sum([x[k] * Complex.conjugate(root_of_unity(k*n, N)) for k in range(N)]) for n in range(N)]

def naive_inv_fourier_transform(x):
    N = len(x)
    if N % 2 != 0:
        raise ValueError
    
    return [sum([x[k] * root_of_unity(k*n, N) for k in range(N)]).real/N for n in range(N)]
