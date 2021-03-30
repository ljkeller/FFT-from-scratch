from math import atan2, sin, cos
from Constants import pi

# Calulcates theta from real, imag
# output is in [0, pi/2)
def calculate_theta(real, imag):
    theta = atan2(imag, real)
    theta = theta if theta >= 0 else theta + 2*pi
    return theta

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        
        self.rad = (self.real**2 + self.imag**2) ** 0.5
        self.theta = calculate_theta(real, imaginary)

    # returns complex number from polar coords
    @classmethod
    def from_polar(cls, radius, theta):
        # Round off to allow cases like 0e-12 to become 0
        real, imag = round(radius*cos(theta), 12), round(radius*sin(theta), 12)
        return cls(real, imag)

    # Returns complex representation of purely real number
    @classmethod
    def from_real(cls, real):
        real, imag = real, 0
        return cls(real, imag)

    def theta(self):
        return round(self.theta, 5)

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imag + other.imag
        return Complex(real, imaginary)

    def __iadd__(self, other):
        self.real += other.real
        self.imag += other.imag
        return self

    # not great practice.... BUT lets us call sum on our complex class
    def __radd__(self, other):
        real = other + self.real
        imaginary = other + self.imag
        return Complex(real, imaginary)

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imag - other.imag
        return Complex(real, imaginary)

    def __isub__(self, other):
        self.real -= other.real
        self.imag -= other.imag
        return self

    def __neg__(self):
        real = -self.real
        imaginary = -self.imag

        return Complex(real, imaginary)

    def __mul__(self, other):
        theta = self.theta + other.theta
        radius = self.rad * other.rad
        return Complex.from_polar(radius, theta)

    def __truediv__(self, other):
        if isinstance(other, Complex):
            theta = self.theta - other.theta
            radius = self.rad / other.rad
        else:
            theta = self.theta
            radius = self.rad / other
        return Complex.from_polar(radius, theta)

    # utilizing De Moivre's theorem for simplified calculations
    def __pow__(self, exp):
        theta = self.theta * exp
        radius = self.rad ** exp
        return Complex.from_polar(radius, theta)

    # operator == 
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    # operator !=
    def __ne__(self, other):
        return self.real != other.real or self.imag != other.imag

    # unary abs()
    def __abs__(self):
        return self.rad

    def __float__(self):
        return Complex(self.real, self.imag)

    @staticmethod
    def conjugate(z):
        real, imaginary = z.real, -z.imag
        return Complex(real, imaginary)

    # Performs complex inner product between u & v, order matters
    @staticmethod
    def inner_product(U, V):
        return sum([z*Complex.conjugate(w) for z,w in zip(U, V)])

    def __str__(self):
        reduced = self.__round__(4)
        return f"{reduced.real} + {reduced.imag}j"

    def __repr__(self):
        reduced = self.__round__(4)
        return f"{reduced.real} + {reduced.imag}j"

    def __round__(self, n):
        return Complex(round(self.real, n), round(self.imag, n))

    def polar_str(self):
        return f"Radius: {round(self.rad, 4)} , angle: {round(self.theta, 4)}"
