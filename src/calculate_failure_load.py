from src.second_moment_of_area.i_pie_beam import i_pie_beam
from src.second_moment_of_area.q_i_beam import q_i_beam
from src.tensile_failure import tensile_failure
from src.compressive_failure import compressive_failure
from src.shear_matboard_failure import shear_matboard_failure
from src.shear_glue_failure import shear_glue_failure
from src.buckling import buckling
from src.shear_buckling import shear_buckling


def calculate_failure_load(width, height, spacing, thickness):
    i = i_pie_beam(width, height, thickness)
    q_cent, q_glue = q_i_beam(height / 2, thickness * 2, thickness, width)
    y_bottom_or_top = thickness + (height / 2)
    failure_ten = tensile_failure(i, y_bottom_or_top)
    failure_comp = compressive_failure(i, y_bottom_or_top)
    failure_matboard_shear = shear_matboard_failure(i, 2, thickness, q_cent)
    failure_glue_shear = shear_glue_failure(i, 2, thickness, q_glue)
    failure_buckling = buckling(width, spacing, i, y_bottom_or_top, height)
    failure_buckling_shear = shear_buckling(280, height, i, q_cent, thickness * 2)
    return min(failure_ten, failure_comp, failure_matboard_shear, failure_glue_shear, failure_buckling, failure_buckling_shear)


