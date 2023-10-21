import math


class Counter:
    def __init__(self, number_1: int = 1, number_2: int = 2):
        self.number_1 = number_1
        self.number_2 = number_2

    def finding_arithmetic_mean(self):
        print((self.number_1 + self.number_2) / 2)

    def finding_geometric_mean(self):
        print(math.sqrt(self.number_1 * self.number_2))


count_maker = Counter(20, 10)
count_maker.finding_arithmetic_mean()
count_maker.finding_geometric_mean()
