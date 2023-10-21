class Counter:
    def __init__(self, number_1: int = 1, number_2: int = 2):
        self.number_1 = number_1
        self.number_2 = number_2

    def count_to_formula(self):
        result = self.number_1 - self.number_2 / 1 + self.number_1 * self.number_2
        print(result)


count_maker = Counter(20, 10)
count_maker.count_to_formula()
