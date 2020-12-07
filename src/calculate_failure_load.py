from src.second_moment_of_area.i_pie_beam import i_pie_beam
from src.second_moment_of_area.q_i_beam import q_pie_beam
from src.tensile_failure import tensile_failure
from src.compressive_failure import compressive_failure
from src.shear_matboard_failure import shear_matboard_failure
from src.shear_glue_failure import shear_glue_failure
from src.buckling import buckling
from src.shear_buckling import shear_buckling


def calculate_failure_load(width, height, spacing, thickness):
    i = i_pie_beam(width, height, thickness)
    q_cent, q_glue = q_pie_beam(height / 2, thickness * 2, thickness * 2, width, thickness, 20)
    y_bottom_or_top = (2 * thickness) + (height / 2)
    failure_ten = tensile_failure(i, y_bottom_or_top)
    failure_comp = compressive_failure(i, y_bottom_or_top)
    failure_matboard_shear = shear_matboard_failure(i, 2, thickness, q_cent)
    failure_glue_shear = shear_glue_failure(i, 2, 10, q_glue)
    failure_buckling = buckling(width, spacing, i, y_bottom_or_top, height, thickness)
    failure_buckling_shear = shear_buckling(250, height, i, q_cent, thickness * 2)
    # print(width, height, spacing)
    # print('i:', i, 'q:', q_cent, 'y:', y_bottom_or_top)
    # print('tension:', failure_ten)
    # print('compression:', failure_comp)
    # print('matboard shear:', failure_matboard_shear)
    # print('glue shear:', failure_glue_shear)
    # print('buckling:', failure_buckling)
    # print('shear buckling:', failure_buckling_shear)

    return min(failure_ten, failure_comp, failure_matboard_shear, failure_glue_shear, failure_buckling, failure_buckling_shear)


if __name__ == '__main__':
    calculate_failure_load(106, 110, 24, 1.27)
    print('design 2:')
    calculate_failure_load(134, 91, 55, 1.27)
