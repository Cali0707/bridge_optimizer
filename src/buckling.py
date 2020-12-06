from math import pi


def buckling(w_top, spacing, I, y, web_height):
    P = (140 * y) / I
    denom = (12 * (1 - (0.1 ** 2)))
    stress_a = ((16000 * (pi ** 2)) / denom) * ((1.27/spacing)**2)
    b = (w_top - spacing) / 2
    stress_b = ((1700 * (pi ** 2)) / denom) * ((1.27/b) ** 2)
    stress_web = ((24000 * (pi ** 2)) / denom) * ((1.27/web_height)**2)
    flange_failure_a = stress_a / P
    flange_failure_b = stress_b / P
    web_failure = stress_web / P
    return min(flange_failure_a, flange_failure_b, web_failure)
