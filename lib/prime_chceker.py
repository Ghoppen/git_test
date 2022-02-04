import math


def is_number_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number <= 3:
        return True
    for dividend in range(2, int(math.sqrt(number))):
        if number % dividend == 0:
            return False


print(is_number_prime(10))
