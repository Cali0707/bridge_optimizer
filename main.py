from src.find_combos_sum import sum_less_than_area


def main():
    dimensions = sum_less_than_area(100, 813, 813*1016)
    for dimension in dimensions:
        for spacing in range(1, dimension[0] - 2):
            calculate_failure_stress(dimension[0], dimension[1], spacing)