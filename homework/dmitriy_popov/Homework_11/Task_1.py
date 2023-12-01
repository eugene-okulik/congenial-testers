class Book:
    paper_material = 'бумага'
    text = True

    def __init__(self, book_name, author, pages_count, isbn, reserved):
        self.book_name = book_name
        self.author = author
        self.pages_count = pages_count
        self.isbn = isbn
        self.reserved = reserved


book1 = Book('Мастер и Маргарита', 'Михаил Булгаков', 777, 4478, False)
book2 = Book('Собачье сердце', 'Михаил Булгаков', 347, 8874, False)
book3 = Book('Двенадцать стульев', 'Илья Ильф', 784, 1156, False)
book4 = Book('Мёртвые души', 'Николай Гоголь', 1847, 2276, False)
book5 = Book('Отверженные', 'Виктор Гюго', 856, 3378, False)

book1.reserved = True

books = [book1, book2, book3, book4, book5]
for book in books:
    is_reserved = 'зарезервирована' if book.reserved else ''
    print(f'Название: {book.book_name}, Автор: {book.author}, страниц: {book.pages_count}, '
          f'материал: {book.paper_material}, {is_reserved}')


class SchoolBook(Book):
    def __init__(self, book_name, author, pages_count, isbn, reserved, subject, group, tasks):
        super().__init__(book_name, author, pages_count, isbn, reserved)
        self.subject = subject
        self.group = group
        self.tasks = tasks


school_book1 = SchoolBook('Алгебра 1', 'Пупкин А.В.', 200,
                          2201, False, 'Математика', 1, bool)
school_book2 = SchoolBook('История 2', 'Васин Т.Г.', 300,
                          3301, False, 'История', 2, bool)
school_book3 = SchoolBook('География 5', 'Жуков И.А.', 400,
                          4401, False, 'География', 5, bool)

school_book1.reserved = True

school_books = [school_book1, school_book2, school_book3]
for book in school_books:
    is_reserved = 'зарезервирована' if book.reserved else ''
    print(f'Название: {book.book_name}, Автор: {book.author}, страниц: {book.pages_count}, '
          f'предмет: {book.subject}, класс: {book.group}, {is_reserved}')
