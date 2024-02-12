import mysql.connector as mysql


db = mysql.connect(
    user='st4',
    passwd='AVNS_ANI6HFK07yLk4d9l4Nq',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st4'
)

cursor = db.cursor()

# Создание группы
cursor.execute("insert into `groups` (title, start_date, end_date) values ('DNA-4 group', '01/04/24', '01/04/25')")
group_id = cursor.lastrowid

# Добавление нового студента
cursor.execute(f"insert into students (name, second_name, group_id) values ('Robert', 'Alexander III', {group_id})")
student_id = cursor.lastrowid
# cursor.execute(f"select * from students where id = {student_id}")
# print(cursor.fetchone())

# Добавление новой книги
insert_many_books = "insert into books (title, taken_by_student_id) values (%s, %s)"
cursor.executemany(insert_many_books, [
    ('Идеальный программист-3 :)', student_id),
    ('1984-3', student_id),
    ('Lists-3', student_id),
    ('ASU-3', student_id)
])
# cursor.execute(f"select * from books where taken_by_student_id = {student_id}")
# print(cursor.fetchall())
# cursor.execute(f"select * from repr(groups) where id = {group_id}")
# print(cursor.fetchone())

# Создание учебных предметов
insert_many_subj = "insert into subjets (title) values (%s)"
subject = [
    ("Мат.анализ-5",),
    ("Труд-5",),
    ("Python.Основы-5",),
    ("JAVA.Basic-5",)
]
cursor.executemany(insert_many_subj, subject)
subj_id = cursor.lastrowid
# cursor.execute("select * from subjets order by id desc limit 4")
# print(cursor.fetchall())

# Создание занятии для предметов
insert_new_lessons = "INSERT INTO lessons (title, subject_id) values (%s, %s)"
cursor.executemany(
    insert_new_lessons, [
        ('Занятие в пн-5', subj_id),
        ('Занятие в вт-5', subj_id),
        ('Занятие в ср-5', subj_id),
        ('Занятие в чт-5', subj_id),
        ('Занятие в пт-5', subj_id),
        ('Занятие в сб-5', subj_id),
        ('Занятие в летом-5', subj_id),
        ('Занятие в весной-5', subj_id)
    ]
)
lesson_id = cursor.lastrowid
# cursor.execute("select * from lessons order by id desc limit 8")
# print(cursor.fetchall())

# Ставка оценки
insert_new_marks = "INSERT INTO marks (value, lesson_id, student_id) values (%s, %s, %s)"
cursor.executemany(
    insert_new_marks, [
        (11, lesson_id, student_id),
        (21, lesson_id, student_id),
        (31, lesson_id, student_id),
        (41, lesson_id, student_id),
        (51, lesson_id, student_id),
        (61, lesson_id, student_id),
        (71, lesson_id, student_id),
        (81, lesson_id, student_id)
    ]
)
# cursor.execute(f"select * from marks where student_id = {student_id} order by id desc limit 8")
# print(cursor.fetchall())

# Получите информацию из базы данных: Все оценки студента

cursor.execute(f"select * from marks m where m.student_id = {student_id}")
print(f'Все оценки студента: {cursor.fetchall()}')

# Получите информацию из базы данных: Все книги, которые находятся у студента
cursor.execute(f"select * from books b where b.taken_by_student_id = {student_id}")
print(f'Все книги, которые находятся у студента: {cursor.fetchall()}')

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги,
# оценки с названиями занятий и предметов (всё одним запросом с использованием Join)

cursor.execute(f'''
SELECT * FROM `groups` g
LEFT JOIN students s ON g.id = s.group_id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets s2 ON l.subject_id = s2.id
where s.id = {student_id}
''')
print(f'Данные по студенту: {cursor.fetchall()}')

db.commit()

db.close()
