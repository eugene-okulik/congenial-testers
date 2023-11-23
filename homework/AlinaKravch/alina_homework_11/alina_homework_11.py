class Book:
    material = 'материал: бумага'
    text_exist = True

    def __init__(self, title, author, number_of_pages, isbn, reserve):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserve = reserve


book_1 = Book('Название: Идиот', 'Автор: Достаевский', 'страниц: 500', 123, True)
book_2 = Book('Название: Божественная комедия', 'Автор: Данте Алигьери', 'страниц: 786', 124, False)
book_3 = Book('Название: Тошнота', 'Автор: Жан-Поль Сартр', 'страниц: 320', 125, False)
book_4 = Book('Название: Это началось не с тебя', 'Автор: Марк Уолинн', 'страниц: 304', 126, False)
book_5 = Book('Название: Чума', 'Автор: Альберт Камю', 'страниц: 384', 127, False)

books = [book_1, book_2, book_3, book_4, book_5]
for book in books:
    if book.reserve:
        print(f'{book.title}, {book. author}, {book.number_of_pages}, {book.material}, зарезервирована')
    else:
        print(f'{book.title}, {book.author}, {book.number_of_pages}, {book.material}')


class TutorialBook(Book):
    def __init__(self, title, author, number_of_pages, isbn, reserve, subject, group, tasks):
        super().__init__(title, author, number_of_pages, isbn, reserve)
        self.subject = subject
        self.group = group
        self.tasks = tasks


tutorial_1 = TutorialBook(
    'Название: Алгебра', 'Автор: Иванов', 'страниц: 200', 321, True, 'предмет: Математика', 'класс: 9', True
)
tutorial_2 = TutorialBook(
    'Название: Геометрия', 'Автор: Петров', 'страниц: 250', 322, False, 'предмет: Математика', 'класс: 8', True
)
tutorial_3 = TutorialBook(
    'Название: География', 'Автор: Сидоров', 'страниц: 300', 323, False, 'предмет: География', 'класс: 7', False
)
tutorial_4 = TutorialBook(
    'Название: Литература', 'Автор: Кулибин', 'страниц: 350', 324, False, 'предмет: Литература', 'класс: 10', False
)
tutorial_5 = TutorialBook(
    'Название: Английский', 'Автор: Комербеч', 'страниц: 400', 325, False, 'предмет: Иностранный язык', 'класс: 6', True
)

tutorials = [tutorial_1, tutorial_2, tutorial_3, tutorial_4, tutorial_5]
for tutorial in tutorials:
    if tutorial.reserve:
        print(
            f'{tutorial.title}, {tutorial. author}, {tutorial.number_of_pages}, {tutorial.subject}, {tutorial.group}, '
            f'зарезервирована'
        )
    else:
        print(f'{tutorial.title}, {tutorial.author}, {tutorial.number_of_pages}, {tutorial.subject}, {tutorial.group}')
