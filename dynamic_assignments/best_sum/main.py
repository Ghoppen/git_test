from typing import List


class BestSum(object):
    sums = {}
    shortest_path = None

    def best_sum(self, sum_total: int, additives: List) -> List:
        if sum_total in self.sums.keys():
            return self.sums[sum_total]
        if sum_total == 0:
            return []
        if sum_total < 0:
            return None
        for number in additives:
            remainder = sum_total - number
            remainder_path = self.best_sum(remainder, additives)
            self.set_shortest_path(remainder_path, number)
        self.sums[sum_total] = self.shortest_path
        return self.shortest_path

    def delete_sums(self) -> None:
        self.sums.clear()
        self.sums[0] = []

    def set_shortest_path(self, current_path: list, current_number: int) -> None:
        if current_path is not None:
            current_path.append(current_number)
            if self.shortest_path is None or len(current_path) < len(
                self.shortest_path
            ):
                self.shortest_path = current_path


sums = BestSum()


print(sums.best_sum(7, [2, 3, 7]))
print(sums.best_sum(9, [1, 2, 3, 4, 5, 6, 7, 8]))
