from src.i_pie_beam import i_pie_beam
from src.q_i_beam import q_pie_beam
from src.tensile_failure import tensile_failure
from src.compressive_failure import compressive_failure
from src.shear_matboard_failure import shear_matboard_failure
from src.shear_glue_failure import shear_glue_failure
from src.buckling import buckling
from src.shear_buckling import shear_buckling


def calculate_failure_load(width, height, spacing, thickness):
    # Calculate I
    i = i_pie_beam(width, height, thickness)
    # Calculate Q
    q_cent, q_glue = q_pie_beam(height / 2, thickness * 2, thickness * 2, width, thickness, 20)
    # Calculate y from centroid to bottom/top
    y_bottom_or_top = (2 * thickness) + (height / 2)
    # Calculate failure loads
    failure_ten = tensile_failure(i, y_bottom_or_top)
    failure_comp = compressive_failure(i, y_bottom_or_top)
    failure_matboard_shear = shear_matboard_failure(i, 2, thickness, q_cent)
    failure_glue_shear = shear_glue_failure(i, 2, 10, q_glue)
    failure_buckling = buckling(width, spacing, i, y_bottom_or_top, height, thickness)
    failure_buckling_shear = shear_buckling(125, height, i, q_cent, thickness * 2)
    # Return the lowest of the failure loads i.e. the load at which it will actually fail
    return min(failure_ten, failure_comp, failure_matboard_shear, failure_glue_shear, failure_buckling, failure_buckling_shear)


if __name__ == '__main__':
    load1 = calculate_failure_load(129, 93, 50, 1.27)
    print('design 2:')
    load2 = calculate_failure_load(129, 93, 51, 1.27)
    print(load1, load2)
    print(load1 == load2)
