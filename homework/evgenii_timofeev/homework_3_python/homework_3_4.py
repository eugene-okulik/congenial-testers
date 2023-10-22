import math


class Rectangle:
    def __init__(self, cathetus_1: float = 1, cathetus_2: float = 2):
        self.cathetus_1 = float(cathetus_1)
        self.cathetus_2 = float(cathetus_2)

    def findig_hypotenuse(self):
        print(f"Гипотенуза = {math.sqrt(self.cathetus_1**2 + self.cathetus_1**2)}")

    def findig_square(self):
        print(f"Площадь = {(self.cathetus_1 * self.cathetus_2) / 2}")


count_maker = Rectangle(20, 10)
count_maker.findig_hypotenuse()
count_maker.findig_square()
