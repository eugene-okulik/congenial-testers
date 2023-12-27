import mysql.connector as mysql

db = mysql.connect(
    user='st4',
    passwd='AVNS_ANI6HFK07yLk4d9l4Nq',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st4'
)

cursor = db.cursor(dictionary=True)

# 1. Создаем группу
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ("Админы", "Январь 2020", "Февраль 2021"),
)
group_id = cursor.lastrowid  # Получаем id только что созданной группы


# 2. Добавляем студента в созданную группу
cursor.execute(
    "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)",
    ("Максим", "Богук", group_id),
)
student_id = cursor.lastrowid  # Получаем id только что созданного студента

# 3. Добавляем книги, взятые студентом
cursor.executemany(
    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
    [("Онегин", student_id), ("Капитан", student_id)],
)

# 4. Добавляем предметы и занятия
cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ("Зельеварение",))
subject_id = cursor.lastrowid
cursor.executemany(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
    [("Суббота", subject_id), ("Воскресенье", subject_id)],
)

# 5. Добавляем оценки студенту
cursor.executemany(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
    [("2", 1, student_id), ("3", 2, student_id)],
)

# Сохраняем изменения
db.commit()

# все оценки студента
select_sql1 = '''
select * from students join marks on students.id=marks.student_id 
where students.second_name = 'Boguk'
'''
cursor.execute(select_sql1)
print(cursor.fetchall())

# Все книги, которые находятся у студента
select_sql2 = '''
SELECT * from students join books on students.id=books.id
WHERE students.second_name = 'Boguk'
'''
cursor.execute(select_sql2)
print(cursor.fetchall())

# Для вашего студента выведите всё, что о нем есть в базе
select_sql3 = '''
SELECT s.id, s.name, s.second_name, g.title AS 'Group name', b.title AS 'Book name', l.title 
AS 'Lesson name', s2.title AS 'Subject name', m.value AS 'Оценка'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.id = '12'
'''

# Закрываем соединение
cursor.close()
db.close()