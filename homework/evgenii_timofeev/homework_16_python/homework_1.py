import mysql.connector as mysql

# Устанавливаем соединение
db = mysql.connect(
    user="st4",
    passwd="AVNS_ANI6HFK07yLk4d9l4Nq",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st4",
)
cursor = db.cursor()

# 1. Создаем группу
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ("УГА БУГА", "Декабрь 2023", "Май 2024"),
)
group_id = cursor.lastrowid  # Получаем id только что созданной группы


# 2. Добавляем студента в созданную группу
cursor.execute(
    "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)",
    ("Evgenii", "Timofeev", group_id),
)
student_id = cursor.lastrowid  # Получаем id только что созданного студента

# 3. Добавляем книги, взятые студентом
cursor.executemany(
    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
    [("Necronomicon. Part 2", student_id), ("Necronomicon. Part 3", student_id)],
)

# 4. Добавляем предметы и занятия
cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ("Угабугаведение",))
subject_id = cursor.lastrowid
cursor.executemany(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
    [("Воскресенье", subject_id), ("Понедельник", subject_id)],
)

# 5. Добавляем оценки студенту
cursor.executemany(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
    [("5", 1, student_id), ("4", 2, student_id)],
)

# Сохраняем изменения
db.commit()

query1 = "SELECT value FROM marks WHERE student_id = %s"
cursor.execute(query1, (student_id,))
print(*cursor.fetchall())

query2 = "SELECT title FROM books WHERE taken_by_student_id = %s"
cursor.execute(query2, (student_id,))
print(*cursor.fetchall())

query = """
SELECT
    s.name,
    s.second_name,
    g.title AS group_title,
    b.title AS book_title,
    m.value AS mark_value,
    l.title AS lesson_title,
    subj.title AS subject_title
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets subj ON l.subject_id = subj.id
WHERE s.id = %s;
"""

# Выполняем запрос с использованием student_id
cursor.execute(query, (student_id,))

# Получаем и выводим результаты
results = cursor.fetchall()
for row in results:
    print(row)

# Закрываем соединение
cursor.close()
db.close()
