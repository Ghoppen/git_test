def is_sum_possible(target_sum: int, numbers: list) -> bool:
    target_sums = [False for i in range(target_sum + 1)]
    target_sums[0] = True

    for position in range(0, len(target_sums)):
        if target_sums[position] is True:
            for number in numbers:
                new_position = position + number
                if new_position <= target_sum:
                    target_sums[position + number] = True
    return target_sums[target_sum]


def sum_combination(target_sum: int, numbers: list) -> list:
    target_sums = [None for i in range(target_sum + 1)]
    target_sums[0] = []
    for position in range(0, target_sum):
        if target_sums[position] is not None:
            for number in numbers:
                new_position = position + number
                if new_position <= target_sum:
                    new_sums = target_sums[position].copy()
                    new_sums.append(number)
                    target_sums[new_position] = new_sums
    return target_sums[target_sum]


def find_shortest_sum_cobination(target_sum: int, numbers: list) -> list:
    target_sums = [None for i in range(target_sum + 1)]
    target_sums[0] = []

    for position in range(0, target_sum):
        if target_sums[position] is not None:
            for number in numbers:
                new_position = position + number
                if new_position <= target_sum:
                    combination = target_sums[position].copy()
                    combination.append(number)
                    if target_sums[new_position] is None or len(
                        target_sums[new_position]
                    ) > len(combination):
                        target_sums[new_position] = combination
    return target_sums[target_sum]


answer = sum_combination(7, [4, 3, 4, 7])
print(answer)
