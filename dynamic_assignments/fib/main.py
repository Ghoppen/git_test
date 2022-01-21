# memoization using data structure for storing information
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ctypes import Union


class Fibonacci(object):
    __calculated_values = {}

    def __get_calculated_value(self, fibonnaci_number: int) -> Union[int, None]:
        if fibonnaci_number in self.__calculated_values.keys():
            return self.__calculated_values[fibonnaci_number]

    def calculate_fibonacci_value(self, fibonacci_number: int) -> int:
        calculated_value = self.__get_calculated_value(fibonacci_number)
        if fibonacci_number <= 2:
            return 1
        elif calculated_value is not None:
            return calculated_value
        else:
            self.__calculated_values[fibonacci_number] = self.calculate_fibonacci_value(
                fibonacci_number - 1
            ) + self.calculate_fibonacci_value(fibonacci_number - 2)
            return self.__calculated_values[fibonacci_number]


fib = Fibonacci()

calculated = fib.calculate_fibonacci_value(50)
print(calculated)
