import mysql.connector as mysql

db = mysql.connect(
    user="st4",
    passwd="AVNS_ANI6HFK07yLk4d9l4Nq",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st4",
)

cursor = db.cursor(dictionary=True)
# Создайте студента
cursor.execute("INSERT INTO students (name, second_name) VALUES ('Ivan ', 'Ivanov')")
# store id of a new record in a variable
new_student_id = cursor.lastrowid

# Создайте несколько книг и укажите, что ваш созданный студент взял их
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('Python. Part 1', %s)", (new_student_id, ))
new_book_1 = cursor.lastrowid
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('Python. Part 2', %s)", (new_student_id, ))
new_book_2 = cursor.lastrowid

# Создайте группу
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Testers', 'Oct-2023', 'Oct-2024')")
new_group = cursor.lastrowid

# и определите своего студента туда
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (new_group, new_student_id))

# Создайте несколько учебных предметов
cursor.execute("INSERT INTO subjets (title) VALUES ('Programming')")
new_subject_1 = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) VALUES ('Math')")
new_subject_2 = cursor.lastrowid

# Создайте по два занятия для каждого предмета
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Python', %s)", (new_subject_1, ))
new_lesson_1 = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Java', %s)", (new_subject_1, ))
new_lesson_2 = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Algebra', %s)", (new_subject_2, ))
new_lesson_3 = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Geometry', %s)", (new_subject_2, ))
new_lesson_4 = cursor.lastrowid

# Поставьте своему студенту оценки  для всех созданных вами занятий
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES ('10', %s, %s)", (new_lesson_1, new_student_id)
)
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES ('7', %s, %s)", (new_lesson_2, new_student_id)
)
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES ('9', %s, %s)", (new_lesson_3, new_student_id)
)
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES ('8', %s, %s)", (new_lesson_4, new_student_id)
)

# Все оценки студента
cursor.execute("SELECT value FROM marks WHERE student_id = %s", (new_student_id, ))
print(cursor.fetchall())

# Все книги, которые находятся у студента
cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (new_student_id, ))
print(cursor.fetchall())

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
query = '''
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
'''
cursor.execute(query, (new_student_id, ))
print(cursor.fetchall())

# commit all changes to the DB
db.commit()
db.close()
