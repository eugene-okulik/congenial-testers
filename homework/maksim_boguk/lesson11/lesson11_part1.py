class Book:
    text = "Yes"
    material = 'Paper'

    def __init__(self, name, author, pages, isbn, reserve):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserve = reserve


books = [
    Book('Hobbit', 'Tolkin', 500, 1, False),
    Book('Harry Potter', 'Rouling', 400, 2, False),
    Book('Master and Margarita', "Bulgakov", 350, 3, True),
    Book('Gamlet', 'Shekspeer', 600, 4, False),
    Book('Onegin', 'Pushkin', 300, 5, False)
]

for book in books:
    reserved = ', Зарезервирована' if book.reserve else ""
    print(f"Название: {book.name}, Автор: {book.author}, Страниц: {book.pages}, "
          f"Материал: {book.material} {reserved}"
          )


class School_book(Book):
    def __init__(self, name, author, pages, isbn, reserve, predmet, group, quest):
        super().__init__(name, author, pages, isbn, reserve)
        self.predmet = predmet
        self.group = group
        self.quest = quest


school_books = [
    School_book('Алгебра', "Ivanov", 200, 1, False, 'Математика', 9, True),
    School_book('Геометрия', 'Ivanov', 400, 2, True, 'Матеатика', 8, True),
    School_book('Английский', 'Sidorov', 100, 3, False, "Иностранный язык", 6, True)
]

for book in school_books:
    reserved = ', Зарезервирована' if book.reserve else ""
    print(f"Название: {book.name}, Автор: {book.author}, Страниц: {book.pages}, Предмет: {book.predmet}, "
          f"Класс: {book.group}, Материал: {book.material} {reserved}"
          )
