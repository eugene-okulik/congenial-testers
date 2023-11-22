class Flowers:
    def __init__(
        self, name: str, color: str, length: int = 1, price: int = 1, lifespan: int = 1
    ):
        self.name = name
        self.color = color
        self.price = price
        self.length = length
        self.lifespan = lifespan

    def __str__(self):
        return (
            f"Цветок {self.name} имеет: {self.color} цвет, "
            f"{self.length}см длины и продолжительность жизни = {self.lifespan} земных суток"
        )


class Rose(Flowers):
    def __init__(
        self,
        name: str,
        color: str,
        length: int = 12,
        price: int = 10,
        lifespan: int = 10,
    ):
        super().__init__(name, color, price, length, lifespan)


class Dandelion(Flowers):
    def __init__(
        self,
        name: str,
        color: str,
        length: int = 7,
        price: int = 2,
        lifespan: int = 4,
    ):
        super().__init__(name, color, price, length, lifespan)


class Edelweiss(Flowers):
    def __init__(
        self,
        name: str,
        color: str,
        length: int = 9,
        price: int = 20,
        lifespan: int = 7,
    ):
        super().__init__(name, color, price, length, lifespan)


class Bouquet:
    def __init__(self, flowers: list):
        self.flowers = flowers if flowers else []

    def add_flower(self, name: str, color: str):
        self.flowers.append(Flowers(name, color))

    def delete_flower(self, name: str, color: str):
        self.flowers = [
            flower
            for flower in self.flowers
            if not (flower.name == name and flower.color == color)
        ]

    def find_flower_by_name(self, name: str):
        print(
            *[
                f"В букете есть {flower}"
                for flower in self.flowers
                if flower.name == name
            ],
            sep="\n",
        )

    def count_price(self):
        return f"Общая стоимость букета составляет: {sum(flower.price for flower in self.flowers)} рублей \n"

    def sort_flowers(self, attribute: str):
        self.flowers.sort(key=lambda flower: getattr(flower, attribute))
        for number, new_flower in enumerate(self.flowers, 1):
            print(f"Теперь {new_flower.name} идёт под номером {number}")

    def count_death_of_bouquet(self):
        print(
            f"Среднее время жизни букета: {int(sum(flower.lifespan for flower in self.flowers)/len(self.flowers))} "
            f"дней \n"
        )


all_flowers = [
    Edelweiss("Edelweiss", "White"),
    Rose("Rose", "Red"),
    Dandelion("Dandelion", "Yellow"),
]

bouquet_for_sale = Bouquet(all_flowers)

# Count the average time of bouquet's life
bouquet_for_sale.count_death_of_bouquet()

# Sort flowers by attribute
bouquet_for_sale.sort_flowers("name")

# Find flower by name
bouquet_for_sale.find_flower_by_name("Edelweiss")
