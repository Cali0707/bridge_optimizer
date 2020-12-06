from src.second_moment_of_area.rectangle_i import rectangle_i


def i_pie_beam(width, height, thickness):
    top_bottom_area = width * thickness * 2
    # mid_area = 2 * width * thickness
    main_centroid = (thickness * 2) + (height / 2)
    top_centroid = height + (3 * thickness)
    top_bottom_i = rectangle_i(width, thickness * 2)
    mid_i = rectangle_i(thickness * 2, height)
    return (2 * (top_bottom_i + (top_bottom_area * ((top_centroid - main_centroid) ** 2)))) + mid_i


if __name__ == "__main__":
    pass
