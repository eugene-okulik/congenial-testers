class Counter:
    def __init__(self, number_1: float = 1, number_2: float = 2):
        self.number_1 = float(number_1)
        self.number_2 = float(number_2)

    def count_to_formula(self):
        result = self.number_1 - self.number_2 / 1 + self.number_1 * self.number_2
        print(f"Результат подсчёта = {result}")


count_maker = Counter(20, 10)
count_maker.count_to_formula()
