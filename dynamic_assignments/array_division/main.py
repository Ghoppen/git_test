class ArrayDivider(object):
    brackets = {}

    def __init__(self, numbers: tuple, amount_of_brackets: int) -> None:
        self.numbers = numbers
        self.amount_of_brackets = amount_of_brackets
        self.sum_of_numbers = self.calculate_sum_of_array_members()
        self.bracket_size = self.round_number(
            self.sum_of_numbers / self.amount_of_brackets
        )
        self.number_of_brackets = 0

    def calculate_sum_of_array_members(self) -> int:
        sum = 0
        for number in self.numbers:
            sum = sum + number
        return int(sum)

    def calculate_brackets(self) -> int:
        number_of_brackets = 0
        bracket_numbers = []
        sum = 0
        for number in self.numbers:
            sum = sum + number
            bracket_numbers.append(number)
            if sum % self.bracket_size == 0 and sum != 0:
                number_of_brackets = number_of_brackets + 1
                self.add_brackets(sum, bracket_numbers)
                bracket_numbers = []
        return number_of_brackets

    def add_brackets(self, sum, brackets):
        self.brackets[sum] = brackets

    def round_number(self, number: int) -> int:
        return int(round(number))

    def check_if_it_enough_brackets(self) -> bool:
        return self.number_of_brackets == self.amount_of_brackets

    def print_brackets(self):
        for key, value in self.brackets.items():
            print(f"bracket equals to {key}: {value}")


nums = [1, 3, 6, 2, 7, 1, 2, 8]

divider = ArrayDivider(nums, 3)

print(divider.calculate_brackets())
print(divider.print_brackets())
