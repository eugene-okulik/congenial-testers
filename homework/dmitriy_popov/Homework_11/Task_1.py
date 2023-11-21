class Book:
    paper_material = 'бумага'
    text = True

    def __init__(self, book_name, author, pages_count, isbn, is_reserved):
        self.book_name = book_name
        self.author = author
        self.pages_count = pages_count
        self.isbn = isbn
        self.is_reserved = is_reserved


book1 = Book('Мастер и Маргарита', 'Михаил Булгаков', 777, 4478, False)
book2 = Book('Собачье сердце', 'Михаил Булгаков', '347', 8874, False)
book3 = Book('Двенадцать стульев', 'Илья Ильф', '784', 1156, False)
book4 = Book('Мёртвые души', 'Николай Гоголь', '1847', 2276, False)
book5 = Book('Отверженные', 'Виктор Гюго', '856', 3378, False)

book1.is_reserved = True

books = [book1, book2, book3, book4, book5]
for book in books:
    if book.is_reserved:
        print(f'Название: {book.book_name}, Автор: {book.author}, страниц: {book.pages_count}, '
              f'материал: {book.paper_material}, зарезервирована')
    else:
        print(f'Название: {book.book_name}, Автор: {book.author}, страниц: {book.pages_count}, '
              f'материал: {book.paper_material}')


#class SchoolBook(Book):