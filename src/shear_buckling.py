from math import pi


def shear_buckling(a, h, I, Q, b):
    tau = ((20000*(pi**2)) / 12 * (1-(0.1**2))) * ((1.27 / a)**2 + (1.27 / h)**2)
    return (2 * tau * I * b) / Q
