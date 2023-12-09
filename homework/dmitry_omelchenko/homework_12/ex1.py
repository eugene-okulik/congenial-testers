class Flower:
    def __init__(self, name, freshness, color, stem_length, price, lifespan):
        self.name = name
        self.freshness = freshness  # оценка свежести цветка
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan  # среднее время жизни цветка в днях


class Rose(Flower):
    def __init__(self, color, stem_length, price, lifespan):
        super().__init__("Rose", 9, color, stem_length, price, lifespan)


class Tulip(Flower):
    def __init__(self, color, stem_length, price, lifespan):
        super().__init__("Tulip", 7, color, stem_length, price, lifespan)


class Lily(Flower):
    def __init__(self, color, stem_length, price, lifespan):
        super().__init__("Lily", 8, color, stem_length, price, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_wilting_time(self):
        total_lifespan = sum(flower.lifespan for flower in self.flowers)
        average_lifespan = total_lifespan / len(self.flowers) if self.flowers else 0
        return average_lifespan

    def sort_by_parameter(self, parameter):
        if parameter == 'freshness':
            self.flowers.sort(key=lambda x: x.freshness)
        elif parameter == 'color':
            self.flowers.sort(key=lambda x: x.color)
        elif parameter == 'stem_length':
            self.flowers.sort(key=lambda x: x.stem_length)
        elif parameter == 'price':
            self.flowers.sort(key=lambda x: x.price)

    def search_by_parameter(self, parameter):
        if parameter == 'lifespan':
            return sorted(self.flowers, key=lambda x: x.lifespan, reverse=True)


# Создание объектов цветов
rose = Rose("Red", 30, 10, 10)
tulip = Tulip("White", 25, 12, 7)
lily = Lily("Pink", 28, 8, 5)

# Создание букета и добавление цветов
bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(lily)

# Получение среднего времени увядания букета
avg_wilting_time = bouquet.calculate_wilting_time()
print(f"Среднее время увядания букета: {avg_wilting_time} дней")

# Сортировка букета по параметру
bouquet.sort_by_parameter('price')
for flower in bouquet.flowers:
    print(f"{flower.name} - Цена: {flower.price}.")

# Поиск цветов в букете по параметру
result = bouquet.search_by_parameter('lifespan')
for flower in result:
    print(f"Продолжительность жизни {flower.name}, {flower.lifespan} дней.")
