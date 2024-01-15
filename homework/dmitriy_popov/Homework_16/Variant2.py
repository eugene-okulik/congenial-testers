import mysql.connector as mysql

db = mysql.connect(
    user='st4',
    passwd='AVNS_ANI6HFK07yLk4d9l4Nq',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st4'
)


cursor = db.cursor(dictionary=True)


def query_execute(query_string, cursor_bd):
    cursor_bd.execute(query_string)
    return cursor_bd.lastrowid


group_id = query_execute(
    f"INSERT INTO `groups` (title, start_date, end_date) "
    f"VALUES ('Димасики', '12.01.24', '12.03.24')", cursor
)


student_id = query_execute(
    f"INSERT INTO students (name, second_name, group_id) "
    f"VALUES ('Аркаша', 'Пантелемонович', {group_id})", cursor
)


query_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    query_books, [
        ('Книга1', student_id),
        ('Книга2', student_id)
    ]
)


subject1_id = query_execute(f"INSERT INTO subjets (title) VALUES ('Предмет1')", cursor)
subject2_id = query_execute(f"INSERT INTO subjets (title) VALUES ('Предмет2')", cursor)


lesson1_id = query_execute(
    f"INSERT INTO lessons (title, subject_id) "
    f"VALUES ('Урок1', {subject1_id})", cursor
)
lesson2_id = query_execute(
    f"INSERT INTO lessons (title, subject_id) "
    f"VALUES ('Урок2', {subject2_id})", cursor
)


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


# Закрываем соединение
cursor.close()
db.close()
