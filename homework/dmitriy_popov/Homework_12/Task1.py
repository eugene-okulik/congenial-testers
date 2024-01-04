class Flower:
    def __init__(self, name, color, stem_length, freshness, price):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.price = price


class Rose(Flower):
    def __init__(self, color, stem_length, freshness, price):
        super().__init__("Rose", color, stem_length, freshness, price)

    def __repr__(self):
        return (f"Rose(color={self.color}, stem_length={self.stem_length}, freshness={self.freshness}, "
                f"price={self.price})")


class Tulip(Flower):
    def __init__(self, color, stem_length, freshness, price):
        super().__init__("Tulip", color, stem_length, freshness, price)

    def __repr__(self):
        return (f"Tulip(color={self.color}, stem_length={self.stem_length}, freshness={self.freshness}, "
                f"price={self.price})")


class Lily(Flower):
    def __init__(self, color, stem_length, freshness, price):
        super().__init__("Lily", color, stem_length, freshness, price)

    def __repr__(self):
        return (f"Lily(color={self.color}, stem_length={self.stem_length}, freshness={self.freshness}, "
                f"price={self.price})")


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_cost(self):
        total_cost = 0
        for flower in self.flowers:
            total_cost += flower.price
        return total_cost

    def average_lifespan(self):
        total_lifespan = sum([flower.freshness for flower in self.flowers])
        return total_lifespan / len(self.flowers)

    def sort_by_parameter(self, parameter):
        sorted_flowers = sorted(self.flowers, key=lambda x: getattr(x, parameter))
        return [flower.name for flower in sorted_flowers]

    def search_by_parameter(self, parameter, value):
        found_flowers = [flower for flower in self.flowers if getattr(flower, parameter) == value]
        return [flower.name for flower in found_flowers]


# Создаем цветы
rose1 = Rose("red", 40, 5, 100)
tulip1 = Tulip("pink", 30, 4, 60)
lily1 = Lily("white", 35, 6, 85)

# Создаем букет, добавляем цветы и определяем их стоимость
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(tulip1)
bouquet.add_flower(lily1)
print(bouquet.calculate_cost())

# Определяем среднее время увядания букета
print(bouquet.average_lifespan())

# Сортируем цветы в букете по длине стебля
print(bouquet.sort_by_parameter("stem_length"))

# Ищем цветы в букете по цвету
print(bouquet.search_by_parameter("color", "pink"))
