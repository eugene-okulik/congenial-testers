class Flowers:
    def __init__(self, freshness, color, stem_length, price, lifespan):
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan


class Rose(Flowers):
    def __init__(self, freshness, color, stem_length, price, lifespan):
        super().__init__(freshness, color, stem_length, price, lifespan)


class Chamomile(Flowers):
    def __init__(self, freshness, color, stem_length, price, lifespan):
        super().__init__(freshness, color, stem_length, price, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_withing_time(self):
        if not self.flowers:
            return 0
        total_lifespan = sum(flower.lifespan for flower in self.flowers)
        return total_lifespan / len(self.flowers)

    def sort_by_parameter(self, parameter):
        if parameter == 'freshness':
            self.flowers.sort(key=lambda x: x.freshness, reverse=True)
        elif parameter == 'color':
            self.flowers.sort(key=lambda x: x.color)
        elif parameter == 'stem_length':
            self.flowers.sort(key=lambda x: x.stem_length, reverse=True)
        elif parameter == 'cost':
            self.flowers.sort(key=lambda x: x.cost, reverse=True)

    def find_flower_by_parameter(self, parameter, value):
        found_flowers = []
        if parameter == 'lifespan':
            for flower in self.flowers:
                if flower.lifespan == value:
                    found_flowers.append(flower)
        return found_flowers


rose1 = Rose('red', 90, 25, 10, 7)
rose2 = Rose('white', 95, 30, 12, 6)
chamomile1 = Chamomile('pink', 80, 20, 8, 5)

# Создаем букет
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(chamomile1)

# Расчет времени увядания
print(f"Время увядания букета: {bouquet.calculate_withing_time()} дней")

# Сортировка цветов в букете
bouquet.sort_by_parameter('color')
for flower in bouquet.flowers:
    print(flower.color)

# Поиск цветов в букете по параметру
found_flowers = bouquet.find_flower_by_parameter('lifespan', 6)
for flower in found_flowers:
    print(f"Найден цветок с временем жизни {flower.lifespan} дней")