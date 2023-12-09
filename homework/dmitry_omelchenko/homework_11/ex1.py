class Book:
    def __init__(self, material, has_text, title, author, num_pages, ISBN):
        self.material = material
        self.has_text = has_text
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.ISBN = ISBN
        self.reserved = False

    def __str__(self):
        reserved_status = "зарезервирована" if self.reserved else ""
        return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, материал: {self.material} "
                f"{reserved_status}")


class Textbook(Book):
    def __init__(self, material, has_text, title, author, num_pages, ISBN, subject, school_class, has_exercises):
        super().__init__(material, has_text, title, author, num_pages, ISBN)
        self.subject = subject
        self.school_class = school_class
        self.has_exercises = has_exercises

    def __str__(self):
        reserved_status = "зарезервирована" if self.reserved else ""
        return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, "
                f"предмет: {self.subject}, класс: {self.school_class} {reserved_status}")


# Создание экземпляров книг
book1 = Book("бумага", True, "Идиот", "Достоевский", 500,
             "978-5-9909751-1-0")
book2 = Book("электронная", True, "Преступление и наказание", "Достоевский", 600,
             "978-5-9909751-2-0")
book3 = Book("бумага", True, "Война и мир", "Толстой", 1200,
             "978-5-9909751-3-0")
book4 = Book("электронная", True, "1984", "Оруэлл", 350,
             "978-5-9909751-4-0")
book5 = Book("бумага", True, "Мастер и Маргарита", "Булгаков", 400,
             "978-5-9909751-5-0")

# Помечаем одну книгу как зарезервированную
book3.reserved = True

# Создание экземпляров учебников
textbook1 = Textbook("бумага", True, "Алгебра", "Иванов", 200,
                     "978-5-9909751-6-0", "Математика", 9, True)
textbook2 = Textbook("бумага", True, "История", "Петров", 300,
                     "978-5-9909751-7-0", "История", 10, False)
textbook3 = Textbook("бумага", True, "География", "Сидоров", 250,
                     "978-5-9909751-8-0", "География", 8, True)
textbook4 = Textbook("бумага", True, "Физика", "Кузнецова", 180,
                     "978-5-9909751-9-0", "Физика", 11, False)
textbook5 = Textbook("бумага", True, "Биология", "Смирнов", 220,
                     "978-5-9909751-0-0", "Биология", 7, True)

# Помечаем один учебник как зарезервированный
textbook1.reserved = True

# Вывод информации о книгах
print(book1)
print(book2)
print(book3)
print(book4)
print(book5, '\n')

# Вывод информации о учебниках
print(textbook1)
print(textbook2)
print(textbook3)
print(textbook4)
print(textbook5)
