class Book:  # с атрибутами:
    page_material = ()  # материал страниц
    present_text = True  # наличие текста
    reserved = (True, False)  # флаг зарезервирована ли книга или нет (True/False)

    def __init__(self, book_name, author, number_of_pages, isbn, reserved):
        self.book_name = book_name  # название книги
        self.author = author  # автор
        self.number_of_pages = number_of_pages  # кол-во страниц
        self.isbn = isbn  # ISBN
        self.reserved = reserved


class SchoolBook(Book):  # класс для школьных учебников

    def __init__(self, book_name, author, number_of_pages, isbn, reserved, subject, school_class, exercise):
        super().__init__(book_name, author, number_of_pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.exercise = exercise


books = [
    Book('Записки Фараона', 'Тут Ан Хамон', 37489, 83495890329, False),
    Book('Сказки', 'Ханс Кристиян Андерсен', 759, 9385097948309, False),
    Book('Чорны замак Альшанскi', 'Уладзiмiр Караткевiч', 546, 8502, False),
    Book('Мы', 'Евгкний Замятин', 224, 83495890329, False),
    Book('1984', 'Джордж Оруэл', 345, 98095890329, False),
    Book('Matrix', 'br. or sist. Wachkowski', 1145, 980943890329, False)
]
books[0].reserved = True

for book in books:

    if book.author == 'Тут Ан Хамон':
        book.page_material = 'папирус'
    elif book.book_name == 'Matrix':
        book.page_material = 'пластик'
    else:
        book.page_material = 'бумага'
    # Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
    if book.reserved:
        print(f"Название: {book.book_name}, Автор: {book.author}, страниц: {book.number_of_pages}, "
              f"материал: {book.page_material}, зарезервирована"
              )
    else:
        print(f"Название: {book.book_name}, Автор: {book.author}, страниц: {book.number_of_pages},"
              f" материал: {book.page_material}"
              )


school_books = [
    SchoolBook('Алгебра', 'Иванов И.И.', 123, 98430977, False,
               'Математика', 7, True),
    SchoolBook('Геометрия', 'Петров П.П.', 450, 9347690934, False,
               'Математика', 10, True),
    SchoolBook('История Беларуси', 'Сидорик С.С.', 567, 437572320, False,
               'История', 11, True)
]

school_books[2].reserved = True
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
for book in school_books:
    if book.reserved:
        print(f"Название: {book.book_name}, Автор: {book.author}, страниц: {book.number_of_pages},"
              f"предмет: {book.subject}, класс: {book.school_class} зарезервирована"
              )
    else:
        print(f"Название: {book.book_name}, Автор: {book.author}, страниц: {book.number_of_pages},"
              f"предмет: {book.subject}, класс: {book.school_class}"
              )
