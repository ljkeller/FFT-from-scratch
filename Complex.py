from math import atan2, sin, cos

pi = 3.141592653589793

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

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imag - other.imag
        return Complex(real, imaginary)

    def __neg__(self):
        real = -self.real
        imaginary = -self.imag

        return Complex(real, imaginary)

    def __mul__(self, other):
        theta = self.theta + other.theta
        radius = self.rad * other.rad
        return Complex.from_polar(radius, theta)

    def __truediv__(self, other):
        theta = self.theta - other.theta
        radius = self.rad / other.rad
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

    def __str__(self):
        return f"{self.real} + {self.imag}j"

    def polar_str(self):
        return f"Radius: {round(self.rad, 4)} , angle: {round(self.theta, 4)}"
