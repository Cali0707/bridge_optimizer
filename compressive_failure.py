def compressive_failure(I, y_top):
    # P = sigma_compression * I/140y_top
    return (6 * I)/(140 * y_top)