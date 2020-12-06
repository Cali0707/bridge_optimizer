from src.second_moment_of_area.rectangle_i import rectangle_i


def i_pie_beam(width, height, thickness):
    top_bottom_area = width * thickness
    # mid_area = 2 * width * thickness
    main_centroid = thickness + (height / 2)
    top_centroid = height + (1.5 * thickness)
    top_bottom_i = rectangle_i(width, thickness)
    mid_i = rectangle_i(thickness * 2, height)
    return (2 * (top_bottom_i + (top_bottom_area * ((top_centroid - main_centroid) ** 2)))) + mid_i


if __name__ == "__main__":
    pass
