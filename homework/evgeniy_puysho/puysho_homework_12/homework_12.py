class Flowers:
    def __init__(self, name, color, freshness, length, cost):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.length = length
        self.cost = cost


class Rose(Flowers):
    def __init__(self, name, color, freshness, length, cost):
        super().__init__(name, color, freshness, length, cost)


class Tulip(Flowers):
    def __init__(self, name, color, freshness, length, cost):
        super().__init__(name, color, freshness, length, cost)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def average_lifespan(self):
        return sum(flower.freshness for flower in self.flowers) / len(self.flowers)

    def sort_by_freshness(self):
        (self.flowers.sort(key=lambda x: x.freshness))

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda x: x.cost, reverse=True)

    def search_by_lifespan(self, lifespan):
        return [flower for flower in self.flowers if flower.freshness == lifespan]


rose1 = Rose('Roza', 'red', 4, 228, 1500)
rose2 = Rose('Rozo4ka', 'black_red', 10, 22, 2200)
tulip1 = Tulip('Beliy tulpan', 'white', 3, 10, 500)
tulip2 = Tulip('Jeltiy tulpan', 'yellow', 8, 14, 777)

bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(tulip2)
bouquet.add_flower(tulip1)

print('средняя свежесть =', bouquet.average_lifespan())
print('цена букета =', bouquet.calculate_cost())
search = bouquet.search_by_lifespan(8)
for y in search:
    print(f'цветок свежестью 8 это - {y.name}')
