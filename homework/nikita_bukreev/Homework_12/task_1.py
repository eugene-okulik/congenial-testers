# дико запнулся на написании методов для класса букет, просидел очень долго и пошел домогаться до чатаГПТ....(

class Flowers:
    colour = True
    family = 'flowers'

    def __init__(self, colour, size, price):
        self.colour = colour
        self.size = size
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__}"


class Rose(Flowers):
    name = 'rose'
    smell = 'good'
    lifeday = 5


class Pion(Flowers):
    name = 'pion'
    smell = 'bad'
    lifeday = 6


class Tulpan(Flowers):
    name = 'tulpan'
    smell = 'nothing'
    lifeday = 8


class Buket(Flowers):

    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def cost(self):
        return sum(flower.price for flower in self.flowers)

    def lifetime(self):
        return sum(flower.lifeday for flower in self.flowers) / len(self.flowers)

    def sort_flowers(self, key):
        self.flowers.sort(key=lambda x: getattr(x, key))

    def find_flowers(self, key, value):
        return [flower for flower in self.flowers if getattr(flower, key) == value]


flower_1 = Rose('red', 80, 200)
flower_2 = Pion('pink', 50, 400)
flower_3 = Tulpan('yellow', 30, 100)

buket = Buket()
buket.add_flower(flower_1)
buket.add_flower(flower_2)
buket.add_flower(flower_3)

print(buket.lifetime())  # время увядания

buket.sort_flowers('price')  # сортировка по цене
print(buket.flowers)

buket.sort_flowers('size')  # сортировка по размеру
print(buket.flowers)

find = buket.find_flowers('colour', 'red')  # поиск по цвету
print(find)

find = buket.find_flowers('lifeday', 8)  # поиск по времени жизни
print(find)
