from random import randint

from faker import Faker

from homework_1 import Book

fake = Faker()
subjects = [
    "Math",
    "Biology",
    "Music",
    "Labour",
    "Culture",
    "Sport",
]


class SchoolBook(Book):
    def __init__(
        self,
        book_name,
        author,
        number_of_pages,
        isbn,
        subject,
        school_class,
        has_tasks=False,
        reserved=False,
    ):
        super().__init__(book_name, author, number_of_pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.has_tasks = has_tasks

    def __str__(self):
        has_text_status = ", есть задания" if self.has_tasks else ", заданий нет"
        reserve_status = ", зарезервирована" if self.reserved else ""
        return (
            f"Название: {self.book_name}, Автор: {self.author}, страниц: {self.number_of_pages},"
            f" предмет: {self.subject}, класс: {self.school_class}{reserve_status}{has_text_status}"
        )


def create_and_print_books():
    books = []
    for book in range(5):
        new_book = SchoolBook(
            book_name=fake.text()[:10],
            author=fake.last_name(),
            number_of_pages=fake.postcode()[:3],
            isbn=fake.isbn10(),
            subject=subjects[randint(0, len(subjects) - 1)],
            school_class=randint(1, 11),
        )
        books.append(new_book)

    books[0].reserved = True
    books[0].has_tasks = True

    for book in books:
        print(book)


if __name__ == "__main__":
    create_and_print_books()
