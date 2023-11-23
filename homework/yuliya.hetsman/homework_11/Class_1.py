class Book:
    paper_material = 'Бумага'
    text = True

    def __init__(self, book_name, author, pages_count, isbn, reserved):
        self.book_name = book_name
        self.author = author
        self.pages_count = pages_count
        self.isbn = isbn
        self.reserved = reserved


book1 = Book('Властелин колец', 'Толкин', 870, 478, False)
book2 = Book('Идиот', 'Достоевский', 347, 887, False)
book3 = Book('Собака Баскервилей', 'Дойл', 784, 16, False)
book4 = Book('Чернобыльская молитва', 'Алексиевич', 1847, 27, False)
book5 = Book('Восточный экспресс', 'Кристи', 856, 3373, False)

book3.reserved = True

books = [book1, book2, book3, book4, book5]
for book in books:
    is_reserved = 'Зарезервирована' if book.reserved else ''
    print(f'Название: {book.book_name}, Автор: {book.author}, Страниц: {book.pages_count}, '
          f'Материал: {book.paper_material}, {is_reserved}')


class SchoolBooks(Book):
    def __init__(self, book_name, author, pages_count, isbn, reserved, subject, group, tasks):
        super().__init__(book_name, author, pages_count, isbn, reserved)
        self.subject = subject
        self.group = group
        self.tasks = tasks


school_book1 = SchoolBooks('Алгебра 11', 'Арефьева', 181,
                           21, False, 'Математика', 11, bool)
school_book2 = SchoolBooks('История 9', 'Панов', 202,
                           31, False, 'История', 9, bool)
school_book3 = SchoolBooks('География 8', 'Сарычева', 154,
                           41, False, 'География', 8, bool)
school_book4 = SchoolBooks('Английский 6', 'Юхнель', 164,
                           51, False, 'Английский', 6, bool)

school_book2.reserved = True

school_books = [school_book1, school_book2, school_book3, school_book4]
for book in school_books:
    is_reserved = 'Зарезервирована' if book.reserved else ''
    print(f'Название: {book.book_name}, Автор: {book.author}, Страниц: {book.pages_count}, '
          f'Предмет: {book.subject}, Класс: {book.group}, {is_reserved}')
