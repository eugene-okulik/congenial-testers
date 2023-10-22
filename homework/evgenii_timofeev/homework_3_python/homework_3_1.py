class Counter:
    def __init__(self, number_1: float = 1, number_2: float = 2):
        self.number_1 = float(number_1)
        self.number_2 = float(number_2)

    def addition(self):
        print(
            f"Cумма чисел {self.number_1} и {self.number_2} = {self.number_1 + self.number_2}"
        )

    def subtraction(self):
        print(
            f"Вычитание чисел {self.number_1} и {self.number_2} = {self.number_1 + self.number_2}"
        )

    def multiplication(self):
        print(
            f"Умножение чисел {self.number_1} и {self.number_2} = {self.number_1 + self.number_2}"
        )


count_maker = Counter(20, 10)
count_maker.addition()
count_maker.subtraction()
count_maker.multiplication()
