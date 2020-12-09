from math import pi


def buckling(w_top, spacing, I, y, web_height, thickness):
    # Calculate load in terms of y and I
    P = (140 * y) / I
    # Calculate denominator of first part of buckling equation
    denom = (12 * (1 - (0.2 ** 2)))
    # Calculate stress of the restrained top flange (16000 =  4 * 4000)
    stress_a = ((16000 * (pi ** 2)) / denom) * ((thickness * 2/spacing)**2)
    # Calculate the width of the unrestrained portion of the flange
    b = (w_top - spacing) / 2
    # Calculate stress of unrestrained top flange (1700 = 0.425 * 4000)
    stress_b = ((1700 * (pi ** 2)) / denom) * ((thickness * 2/b) ** 2)
    # Calculate the stress in the web
    stress_web = ((24000 * (pi ** 2)) / denom) * ((thickness/y)**2)
    # Calculate the restrained flange failure load
    flange_failure_a = stress_a / P
    # Calculate the unrestrained flange failure load
    flange_failure_b = stress_b / P
    # Calculate the web failure load
    web_failure = stress_web / P
    # Return the lowest load
    return min(flange_failure_a, flange_failure_b, web_failure)
