def shear_matboard_failure(I, num_webs, b_web, Q_cen):
    # b_web refers to the width of one wall
    # P = 2 * tau * I * centroid_width / Q_centroid
    return (2 * 4 * I * num_webs * b_web) / Q_cen
