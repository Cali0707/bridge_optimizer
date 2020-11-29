from src.second_moment_of_area.rectangle_i import rectangle_i


def I_I_beam(top_width, top_height, mid_width, mid_height, bottom_width, bottom_height):
    top_area = top_width * top_height
    mid_area = mid_width * mid_height
    bottom_area = bottom_width * bottom_height
    top_centroid = bottom_height + mid_height + (top_height / 2)
    mid_centroid = bottom_height + (mid_height / 2)
    bottom_centroid = (bottom_height / 2)
    main_centroid = ((top_area * top_centroid) + (mid_area * mid_centroid) + (bottom_area * bottom_centroid)) / (top_area + mid_area + bottom_area)
    top_i = rectangle_i(top_width, top_height)
    mid_i = rectangle_i(mid_width, mid_height)
    bottom_i = rectangle_i(bottom_width, bottom_height)
    return top_i + (top_area * ((top_centroid-main_centroid)**2)) + mid_i + (mid_area * ((mid_centroid-main_centroid)**2)) + bottom_i + (bottom_area * ((bottom_centroid-main_centroid)**2))


if __name__ == "__main__":
    print(I_I_beam(10, 10, 5, 5, 5, 5))
