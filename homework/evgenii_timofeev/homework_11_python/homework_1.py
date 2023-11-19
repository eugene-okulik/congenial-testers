from random import randint

from faker import Faker

fake = Faker()


class Book:
    material = "paper"
    has_text = True

    def __init__(self, book_name, author, number_of_pages, isbn, reserved=False):
        self.book_name = book_name
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        reserve_status = ", зарезервирована" if self.reserved else ""
        return (
            f"Название: {self.book_name}, Автор: {self.author}, страниц: {self.number_of_pages},"
            f" материал: {self.material}{reserve_status}"
        )


def create_and_print_books():
    books = []
    for book in range(5):
        new_book = Book(fake.color_name(), fake.name(), randint(1, 1000), fake.isbn10())
        books.append(new_book)

    books[0].reserved = True

    for book in books:
        print(book)


# It is needed to be written because if we launch the second file, it shows 10 prints
# (5 form the first file and 5 from the second file)
if __name__ == "__main__":
    create_and_print_books()
