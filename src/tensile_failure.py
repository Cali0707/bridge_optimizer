def tensile_failure(I, y_bot):
    # P = sigma_tension * I/140y_bottom
    return (30 * I)/(140 * y_bot)