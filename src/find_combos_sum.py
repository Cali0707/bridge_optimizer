from itertools import product


def sum_less_than_area(min_width, max_width, max_area):
    # Assume length of 950mm
    length = 950
    # make list containing every possible width
    # starts at min_width, and cant go above half of the total width - 2 because height has to be at least 1
    top_widths = []
    for i in range(min_width, (max_width // 2) - 2):
        top_widths.append(i)
    # make list containing every possible height
    # starts at 1, and goes to the half of the max width minus 2 * min width
    heights = []
    for i in range(1, (max_width - (2 * min_width)) // 2):
        heights.append(i)
    # Calculate cartesian product of widths and heights, making sure none violate constraints
    possible_dimensions = [p for p in product(top_widths, heights) if sum([p[0] * 4 * length,
                                                                           (p[1] + 20) * 2 * length]) < max_area]
    # Calculate all possible spacings that can be used with each (width, height) s.t. no constraints are violated
    usable_dimensions = []
    for dimension in possible_dimensions:
        for spacing in range(1, dimension[0] - 2):
            if sum([(spacing + 20), dimension[0] * 4, (dimension[1] + 20) * 2]) <= max_width:
                if sum([dimension[0] * 4 * length, (dimension[1] + 20) * 2 * length,
                        (spacing + 20) * dimension[1] * 8]) <= max_area:
                    usable_dimensions.append([dimension[0], dimension[1], spacing])
            elif spacing + 20 < 66 and sum([dimension[0] * 4 * length, (dimension[1] + 20) * 2 * length,
                                           (spacing + 20) * dimension[1] * 8]) <= max_area:
                usable_dimensions.append([dimension[0], dimension[1], spacing])
    # Return list of tuples of all usable dimensions [(width, height, spacing)]
    return usable_dimensions


if __name__ == '__main__':
    # l1 = find_combos_sum(10, 10, 2)
    # l2 = find_combos_sum(10, 10, 3)
    l = sum_less_than_area(100, 813, 813*1016)
    print(len(l))
