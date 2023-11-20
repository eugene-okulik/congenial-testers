class Books:
    page_material = 'Бумага'
    is_containing_text = True

    def __init__(self, book_name, author, pages_count, isbn_num, is_reserved, subject=None, grade=None):
        self.book_name = book_name
        self.author = author
        self.pages_count = pages_count
        self.isbn_num = isbn_num
        self.is_reserved = is_reserved
        self.subject = subject
        self.grade = grade

    def display_info(self):
        reserved_status = ', зарезевирована' if self.is_reserved else ''
        additional_info = (f', Предмет: {self.subject}, Класс: {self.grade}' if self.subject and self.grade else '')
        print(f'Название: {self.book_name}, Автор: {self.author}, Страниц: {self.pages_count}, '
              f'Материал: {self.page_material}{additional_info}{reserved_status}'
              )


class Schoolbook(Books):

    def __init__(self, book_name, author, pages_count, isbn_num, is_reserved, subject, grade, task):
        super().__init__(book_name, author, pages_count, isbn_num, is_reserved, subject, grade)
        self.task = task


knigi = [
    Books('Веселая Рассказ', 'Мэри Петрова', 234, 123, False),
    Books('Забавное Путешествие', 'Боб Смит', 34, 432, False),
    Books('Необычная Книга', 'Анна Иванова', 111, 7321, False),
    Books('Сумасшедшая История', 'Питер Джонсон', 99, 7321, False),
    Books('Забавная Приключение', 'Анна Петрова', 99, 7321, True)
]

school_books = [
    Schoolbook('Алгебра 8-й класс', 'Евклид', 222, 9876, False, 'Математика', 8, True),
    Schoolbook('Писатели 20-го века', 'Абоба', 222, 9876, False, 'Русская литература', 5, True),
    Schoolbook('Оптика', 'Кто-то', 222, 9876, False, 'Физика', 11, True),
    Schoolbook('Спина болеть не будет', 'А. Невский', 123, 9876, True, 'Физкультура', 7, True),
]
for book in knigi:
    book.display_info()
for school_book in school_books:
    school_book.display_info()
