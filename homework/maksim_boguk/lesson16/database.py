import mysql.connector as mysql

db = mysql.connect(
    user='st4',
    passwd='AVNS_ANI6HFK07yLk4d9l4Nq',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st4'
)

cursor = db.cursor(dictionary=True)

insert_query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        ('Гарри', 'Поттер', 1),
        ('Гарри1', 'Поттер2', 1),
        ('Гарри2', 'Поттер3', 1)
    ]
)

insert_query1 = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Война и мир', 48),
        ('Остров сокровищ', 49),
    ]
)

insert_query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        ('Lesson JavaScript', 'may 23', 'jun 23'),
    ]
)

insert_query = "INSERT INTO subjets (title) VALUES (%s)"
cursor.executemany(
    insert_query, [
        ('Химия',),
        ('Физика',),
        ('Музыка',)
    ]
)

insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Friday', 5),
        ('Wednesday', 4)
    ]
)

insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        (3, 25, 48),
        (3, 26, 49)
    ]
)

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

db.commit()
db.close()
