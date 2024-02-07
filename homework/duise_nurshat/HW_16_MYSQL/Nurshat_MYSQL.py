import mysql.connector as mysql


db = mysql.connect(
    user='st4',
    passwd='AVNS_ANI6HFK07yLk4d9l4Nq',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st4'
)

cursor = db.cursor()

# Добавление нового студента
cursor.execute("insert into students (name, second_name, group_id) values ('Robert', 'Alexander III', 127)")

student_id = cursor.lastrowid
cursor.execute(f"select * from students where id = {student_id}")
print(cursor.fetchone())

# Добавление новой книги
insert_many_books = "insert into books (title, taken_by_student_id) values (%s, %s)"
cursor.executemany(insert_many_books, [
    ('Идеальный программист-3 :)', 196),
    ('1984-3', 196),
    ('Lists-3', 196),
    ('ASU-3', 196)
])

cursor.execute("select * from books where taken_by_student_id = 196")
print(cursor.fetchall())

# Создание группы
cursor.execute("insert into `groups` (title, start_date, end_date) values ('DNA-3 group', '01/04/24', '01/04/25')")

group_id = cursor.lastrowid
cursor.execute(f'select * from repr(groups) where id = {group_id}')
print(cursor.fetchone())

# Создание учебных предметов
insert_many_subj = "insert into subjets (title) values (%s)"
subject = [
    ("Мат.анализ-3",),
    ("Труд-3",),
    ("Python.Основы-3",),
    ("JAVA.Basic-3",)
]
cursor.executemany(insert_many_subj, subject)

cursor.execute("select * from subjets order by id desc limit 4")
print(cursor.fetchall())

# Создание занятии для предметов
insert_new_lessons = "INSERT INTO lessons (title, subject_id) values (%s, %s)"
cursor.executemany(
    insert_new_lessons, [
        ('Занятие в пн-2', 199),
        ('Занятие в вт-2', 199),
        ('Занятие в ср-2', 200),
        ('Занятие в чт-2', 200),
        ('Занятие в пт-2', 201),
        ('Занятие в сб-2', 201),
        ('Занятие в летом-2', 202),
        ('Занятие в весной-2', 202)
    ]
)

cursor.execute("select * from lessons order by id desc limit 8")
print(cursor.fetchall())

# Ставка оценки
insert_new_marks = "INSERT INTO marks (value, lesson_id, student_id) values (%s, %s, %s)"
cursor.executemany(
    insert_new_marks, [
        (11, 525, 196),
        (21, 526, 196),
        (31, 527, 196),
        (41, 528, 196),
        (51, 529, 196),
        (61, 530, 196),
        (71, 531, 196),
        (81, 532, 196)
    ]
)

cursor.execute("select * from marks where student_id = 184 order by id desc limit 8")
print(cursor.fetchall())

# Получите информацию из базы данных: Все оценки студента

cursor.execute("select * from marks m where m.student_id = 196")
print(f'Все оценки студента: {cursor.fetchall()}')

# Получите информацию из базы данных: Все книги, которые находятся у студента
cursor.execute("select * from books b where b.taken_by_student_id = 196")
print(f'Все книги, которые находятся у студента: {cursor.fetchall()}')

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги,
# оценки с названиями занятий и предметов (всё одним запросом с использованием Join)

cursor.execute('''
SELECT * FROM `groups` g
LEFT JOIN students s ON g.id = s.group_id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets s2 ON l.subject_id = s2.id
where s.id = 196
''')
print(f'Данные по студенту: {cursor.fetchall()}')

db.commit()

db.close()
