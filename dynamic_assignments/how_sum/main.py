from typing import List


class HowSum(object):
    sums = {0: []}

    def how_sum(self, sum_total: int, additives: List) -> List:

        if sum_total in self.sums.keys():
            return self.sums[sum_total]
        if sum_total < 0:
            return None
        for number in additives:
            remainder = sum_total - number
            remainder_path = self.how_sum(remainder, additives)
            if remainder_path is not None:
                remainder_path.append(number)
                self.sums[remainder] = remainder_path
                return remainder_path
        self.sums[sum_total] = None
        return None

    def delete_sums(self) -> None:
        self.sums.clear()
        self.sums[0] = []


sums = HowSum()


print(sums.how_sum(7, [2, 3]))
sums.delete_sums()
print(sums.how_sum(9, [5, 4, 3, 2, 1, 6, 7]))
