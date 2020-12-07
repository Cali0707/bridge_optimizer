def q_pie_beam(half_mid_height, mid_width, top_height, top_width, tab_height, tab_width):
    mid_centroid = half_mid_height / 2
    top_centroid = half_mid_height + (top_height / 2)
    glue_tab_centroid = half_mid_height - (tab_height / 2)
    area_glue_tab = tab_height * tab_width
    area_mid = half_mid_height * mid_width
    area_top = top_height * top_width
    return (area_mid * mid_centroid) + (area_top * top_centroid) + (area_glue_tab * glue_tab_centroid), (area_top * top_centroid)


if __name__ == '__main__':
    pass