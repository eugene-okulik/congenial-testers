class Counter:
    def __init__(self, number_1: int = 1, number_2: int = 2):
        self.number_1 = number_1
        self.number_2 = number_2

    def addition(self):
        print(self.number_1 + self.number_2)

    def subtraction(self):
        print(self.number_1 - self.number_2)

    def multiplication(self):
        print(self.number_1 * self.number_2)


count_maker = Counter(20, 10)
count_maker.addition()
count_maker.subtraction()
count_maker.multiplication()
