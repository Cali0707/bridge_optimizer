from src.calculate_failure_load import calculate_failure_load
from src.find_combos_sum import sum_less_than_area
from math import inf


def main():
    dimensions = sum_less_than_area(100, 813, 813*1016)
    # print(dimensions)
    thickness = 1.27
    best_dimensions = []
    best_failure_load = -inf
    for dimension in dimensions:
        failure_load = calculate_failure_load(dimension[0], dimension[1], dimension[2], thickness)
        if failure_load > best_failure_load:
            print(dimension, failure_load)
            best_dimensions, best_failure_load = dimension, failure_load
    return best_dimensions, best_failure_load


if __name__ == '__main__':
    print(main())
