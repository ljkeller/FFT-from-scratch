from Complex import *
from Constants import e, pi
from math import log2

e = 2.718281828459045

# Generates kth root of n roots of unity
def root_of_unity(k, n):
    if n % 2 != 0:
        raise ValueError
    principal_root = Complex.from_polar(1, 2.0*pi/n)
    return principal_root ** k

# Called before FFT calls to ensure valid input vector length.
# Returns Complex vector representation of real vector
def preprocessing(x):
    N = len(x)
    if N % 2 != 0:
        raise ValueError
    # make complex vector from real vector
    return list(map(Complex.from_real, x))

# Bit reverse k base 10, where n is bitSize
# Example 0001 -> 1000 for k_10 == 1 and n == 4
def rev(k_10, n):
    # negative inputs invalid
    # Integers that require more than n bits invalid
    if k_10 < 0 or len(bin(k_10)) - 2 > n:
        raise ValueError()

    # Python 3 binary representation has minimal trailing 0
    k_2 = bin(k_10)

    # reverses binary representation: doesnt keep '0b' that leads binary
    # value
    k_2_rev = k_2[-1:1:-1]

    # appends 0s to match n
    k_2_rev = k_2_rev + (n - len(k_2)+2)*'0'
    
    return (int(k_2_rev, 2))

def bit_reverse_copy(x):
    N = len(x)
    list_eles = int(log2(N))

    # Empty list
    A = [None] * N
    # Copy elements into new array by bit-reverse-copy
    for i, val in enumerate(x):
        i_rev = rev(i, list_eles)
        A[rev(i, list_eles)] = val
    return A

def iterative_fft(x):
    x = preprocessing(x)
    N = len(x)

    A = bit_reverse_copy(x)
    
    for s in range(1, int(log2(N) + 1)):
        m = 2**s
        rou_m = Complex.conjugate(Complex.from_polar(1, 2*pi/m))
        for k in range (0, N, m):
            rou = Complex.from_polar(1, 0)
            for j in range(0, m//2):
                t = rou * A[k + j + m//2]
                u = A[k + j]
                A[k + j] = u + t
                A[k + j + m//2] = u - t
                rou = rou*rou_m
    return A

# Wrapper that transforms input before fft call
def fast_fourier_transform(x):
    x = preprocessing(x)
    return fft(x)

# Performs FFT
# 2T(n/2) + O(n)
def fft(x):
    N = len(x)
    # Base case
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
    return y

# Wrapper that transforms input before ifft call
def fast_inv_fourier_transform(y):
    N = len(y)
    if N % 2 != 0:
        raise ValueError
    # Unwrap real from complex
    return [z.real for z in ifft(y)]

# Performs IFFT
# 2T(n/2) + O(n)
def ifft(y):
    N = len(y)
    if N == 1:
        return y

    # Even odd split
    y_evens = y[::2]
    y_odds = y[1::2]

    # Perform FFT on even and half matrices (T(n/2) portion of recurrence)
    x_evens = ifft(y_evens)
    x_odds = ifft(y_odds)

    # generate output list up front
    x = [None] * N
    for k in range(0, N//2):
        rou_k = Complex.from_polar(1, 2.0*pi*k/N)
        x[k] = (x_evens[k] + rou_k * x_odds[k]) / 2
        x[k + N//2] = (x_evens[k] - rou_k * x_odds[k]) / 2
    return x

def naive_fourier_transform(x):
    N = len(x)
    x = preprocessing(x)

    # naive fourier transform
    return [ sum([x[k] * Complex.conjugate(root_of_unity(k*n, N)) for k in range(N)]) for n in range(N)]

def naive_inv_fourier_transform(x):
    N = len(x)
    if N % 2 != 0:
        raise ValueError
    
    return [sum([x[k] * root_of_unity(k*n, N) for k in range(N)]).real/N for n in range(N)]
