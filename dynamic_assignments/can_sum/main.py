from array import array


class CanSum(object):
    sums = {0: True}

    def can_sum(self, sum_total: int, additives: array) -> bool:
        if sum_total < 0:
            return False
        if sum_total in self.sums.keys():
            return self.sums[sum_total]
        for number in additives:
            remainder = sum_total - number
            if self.can_sum(remainder, additives) is True:
                self.sums[remainder] = True
                return True
        self.sums[sum_total] = False
        return False


sums = CanSum()


print(sums.can_sum(9, [2, 6, 4]))
