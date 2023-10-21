import math


class Rectangle:
    def __init__(self, cathetus_1: int = 1, cathetus_2: int = 2):
        self.cathetus_1 = cathetus_1
        self.cathetus_2 = cathetus_2

    def findig_hypotenuse(self):
        print(f"Hypotenuse = {math.sqrt(self.cathetus_1**2 + self.cathetus_1**2)}")

    def findig_square(self):
        print(f"Square = {(self.cathetus_1 * self.cathetus_2) / 2}")


count_maker = Rectangle(20, 10)
count_maker.findig_hypotenuse()
count_maker.findig_square()
