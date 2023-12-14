class Book:
    material = "бумага"
    have_text = True

    def __init__(self, title, author, page_num, isbn, reserved):
        self.title = title
        self.author = author
        self.page_num = page_num
        self.isbn = isbn
        self.reserved = reserved


book1 = Book("Идиот", "Достоевский", 500, 123456, False)
book2 = Book("Война и мир", "Толстой", 555, 234567, False)
book3 = Book("Преступление и наказание", "Достоевский", 569, 345678, False)
book4 = Book("Абай жолы", "Мухтар Ауезов", 400, 456789, False)
book5 = Book("Запах жусана", "Сайын Муратбеков", 500, 567891, False)

book4.reserved = True

books = [book1, book2, book3, book4, book5]
for book in books:
    is_reserved = 'зарезервирована' if book.reserved else ''
    print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.page_num}, '
          f'материал: {book.material}, {is_reserved}')


class SchoolSubject(Book):
    def __init__(self, title, author, page_num, isbn, reserved, subject, klass, have_task):
        super().__init__(title, author, page_num, isbn, reserved)
        self.subject = subject
        self.klass = klass
        self.have_task = have_task


subject1 = SchoolSubject("Задачи по математике", "Автор1", 100, 5151, False,
                         "Математика", 5, True)
subject2 = SchoolSubject("Тесты по истории", "Автор2", 120, 4242, False,
                         "История", 7, True)
subject3 = SchoolSubject("Задачи по физике", "Автор3", 150, 6465, False,
                         "Физика", 9, True)

subject2.reserved = True

subjects = [subject1, subject2, subject3]
for subj in subjects:
    is_reserved = 'зарезервирована' if subj.reserved else ''
    print(f'Название: {subj.title}, Автор: {subj.author}, страниц: {subj.page_num}, '
          f'предмет: {subj.subject}, класс: {subj.klass}, {is_reserved}')
