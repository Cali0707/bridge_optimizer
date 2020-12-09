from math import pi


def shear_buckling(a, h, I, Q, b):
    # Calculate tau - 20000 comes from 5 * 4000 (Young's Modulus for Matboard)
    tau = ((20000*(pi**2)) / 12 * (1-(0.2**2))) * ((1.27 / a)**2 + (1.27 / h)**2)
    # Return the load associated with shear buckling
    return (2 * tau * I * b) / Q
