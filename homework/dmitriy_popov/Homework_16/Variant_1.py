import mysql.connector as mysql

db = mysql.connect(
    user='st4',
    passwd='AVNS_ANI6HFK07yLk4d9l4Nq',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st4'
)


cursor = db.cursor(dictionary=True)

query_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(query_group, (input('name of group: '), input('date start: '), input('date end: ')))
group_id = cursor.lastrowid


query_student = f'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, {group_id})'
cursor.execute(query_student, (input('student_name: '), input('student_second_name: ')))
student_id = cursor.lastrowid


query_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    query_books, [
        (input('name of book1: '), student_id),
        (input('name of book2: '), student_id)
    ]
)


cursor.execute(f"INSERT INTO subjets (title) VALUES ('{input("subject1_name: ")}')")
subject1_id = cursor.lastrowid
cursor.execute(f"INSERT INTO subjets (title) VALUES ('{input("subject2_name: ")}')")
subject2_id = cursor.lastrowid
cursor.execute(f"SELECT * from subjets where id in ({subject1_id}, {subject2_id})")


lesson1_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.execute(lesson1_query, (input('name of lesson1: '), subject1_id))
lesson1_id = cursor.lastrowid
lesson2_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.execute(lesson2_query, (input('name of lesson2: '), subject2_id))
lesson2_id = cursor.lastrowid


marks_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    marks_query, [
        (5, lesson1_id, student_id),
        (3, lesson2_id, student_id)
    ]
)

# Сохраняем изменения
db.commit()


select_query_marks = f"SELECT * FROM marks WHERE student_id = {student_id}"
cursor.execute(select_query_marks)
print('Все оценки студента')
print(cursor.fetchall())


select_query_books = f"SELECT * FROM books WHERE taken_by_student_id = {student_id}"
cursor.execute(select_query_books)
print('Все книги у студента')
print(cursor.fetchall())


select_query = f'''
SELECT s.id,
    s.name,
    s.second_name,
    g.title AS 'Group name',
    b.title AS 'Book name',
    l.title AS 'Lesson name',
    s2.title AS 'Subject name',
    m.value AS 'Оценка'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.id = {student_id};
'''

cursor.execute(select_query)
print('Все по студенту')
print(cursor.fetchall())

cursor.close()
db.close()
