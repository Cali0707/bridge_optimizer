from itertools import combinations_with_replacement


def find_combos_sum(sum_to, max_val, length):
    lst = []
    for i in range(max_val):
        lst.append(i + 1)
    return [combo for combo in combinations_with_replacement(lst, length) if sum(combo) == sum_to]


if __name__ == '__main__':
    l1 = find_combos_sum(10, 10, 2)
    l2 = find_combos_sum(10, 10, 3)
    print(l1)
    print(l2)
