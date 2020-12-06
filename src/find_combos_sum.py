from itertools import combinations_with_replacement
from itertools import product


def find_combos_sum(sum_to, max_val, length):
    lst = []
    for i in range(max_val):
        lst.append(i + 1)
    return [combo for combo in combinations_with_replacement(lst, length) if sum(combo) == sum_to]


def sum_less_than_area(min_width, max_width, max_area):
    # Assume length of 950mm
    length = 950
    widths = []
    heights = []
    for i in range(min_width, (max_width // 2) - 2):
        widths.append(i)
    for i in range(1, (max_width - (2 * min_width)) // 2):
        heights.append(i)
    return [p for p in product(widths, heights) if sum([p[0] * 2 * length, p[1] * 2 * length]) < max_area]


if __name__ == '__main__':
    l1 = find_combos_sum(10, 10, 2)
    l2 = find_combos_sum(10, 10, 3)
    print(l1)
    print(l2)
