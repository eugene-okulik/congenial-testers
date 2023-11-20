class Books:
    page_material = 'Бумага'
    is_containing_text = True

    def __init__(self, book_name, author, pages_count, isbn_num, is_reserved):
        self.book_name = book_name
        self.author = author
        self.pages_count = pages_count
        self.isbn_num = isbn_num
        self.is_reserved = is_reserved


knigi = [
    Books('Веселая Рассказ', 'Мэри Петрова', 234, 123, False),
    Books('Забавное Путешествие', 'Боб Смит', 34, 432, False),
    Books('Необычная Книга', 'Анна Иванова', 111, 7321, False),
    Books('Сумасшедшая История', 'Питер Джонсон', 99, 7321, False),
    Books('Забавная Приключение', 'Анна Петрова', 99, 7321, True)
    ]

for book in knigi:
    if book.is_reserved:
        print(f"Название: {book.book_name}, Автор: {book.author}, cтраниц: {book.pages_count}, "
              f"материал: {book.page_material}, зарезервирована"
              )
    else:
        print(f"Название: {book.book_name}, Автор: {book.author}, cтраниц: {book.pages_count}, "
              f"материал: {book.page_material}"
              )


class Schoolbook(Books):

    def __init__(self, book_name, author, pages_count, isbn_num, is_reserved, subject, grade, task):
        super().__init__(book_name, author, pages_count, isbn_num, is_reserved)
        self.subject = subject
        self.grade = grade
        self.task = task


school_books = [
    Schoolbook('Алгебра 8-й класс', 'Евклид', 222, 9876, False, 'Математика', 8, True),
    Schoolbook('Писатели 20-го века', 'Абоба', 222, 9876, False, 'Русская литература', 5, True),
    Schoolbook('Оптика', 'Автор', 222, 9876, False, 'Физика', 11, True),
    Schoolbook('Спина болеть не будет', 'А. Невский', 123, 9876, True, 'Физкультура', 7, True),
    ]
for school_book in school_books:
    if school_book.is_reserved:
        print(f"Название: {school_book.book_name}, Автор: {school_book.author}, cтраниц: {school_book.pages_count}, "
              f"предмет: {school_book.subject}, класс: {school_book.grade}, зарезервирована"
              )
    else:
        print(f"Название: {school_book.book_name}, Автор: {school_book.author}, cтраниц: {school_book.pages_count}, "
              f"предмет: {school_book.subject}, класс: {school_book.grade}"
              )
