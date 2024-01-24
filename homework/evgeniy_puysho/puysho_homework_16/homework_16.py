import mysql.connector as mysql

db = mysql.connect(
    user='st4',
    passwd='AVNS_ANI6HFK07yLk4d9l4Nq',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st4'
)
cursor = db.cursor(dictionary=True)

# Создайте студента (student)
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('From', 'Pycharm', 1)")
student_id = cursor.lastrowid
print(f'айди студента - {student_id}')

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
insert_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_books, [
        ('Kibernetika1', student_id),
        ('Astrofizika1', student_id)
    ]
)

# Создайте группу (group) и определите своего студента туда
insert_group = "INSERT INTO  `groups` (title, start_date, end_date) VALUES ('Pycharm Group', 'jan 23', 'feb 23')"
cursor.execute(insert_group)
group_id = cursor.lastrowid
print(f'id группы - {group_id}')
update_student = f"UPDATE students SET group_id = 77 where id = {student_id}"
cursor.execute(update_student)

# Создайте несколько учебных предметов (subjects) -- Содал 1, так как могу достать только 1 subject_id для исп-ия дальше
insert_subject = "INSERT INTO subjets (title) VALUES (%s)"
cursor.execute(insert_subject, ('Astrokiberbulling',))
subject_id = cursor.lastrowid
print(f'id предмета - {subject_id}')


# Добавьте урок
insert_lesson = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.execute(insert_lesson, ('Autorak', subject_id))
lesson_id = cursor.lastrowid
print(f'id урока - {lesson_id}')

# Добавьте оценки
insert_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_marks,
    [
        (10, lesson_id, student_id),
        (4, lesson_id, student_id),
        (10, lesson_id, student_id)
    ]
)
db.commit()

query1 = f"SELECT value FROM marks WHERE student_id = (%s)"
cursor.execute(query1, (student_id,))
selected_marks = cursor.fetchall()
print(f'Оценки студента - {selected_marks}')

query2 = f"SELECT title FROM books WHERE taken_by_student_id = (%s)"
cursor.execute(query2, (student_id,))
selected_books = cursor.fetchall()
print(f'Книги взятые студентом - {selected_books}')

select_all_info = '''
SELECT DISTINCT
stu.name, stu.second_name,
g.title as Group_num,
g.start_date, g.end_date,
sub.title  as Subject,
m.value as Mark,
l.title as Lesson_day
from students as stu
left join `groups` as g on g.id = stu.group_id
left join books as b on stu.id = b.taken_by_student_id
left join marks as m on stu.id = m.student_id
left join lessons as l on m.lesson_id = l.id
left join subjets as sub on l.subject_id = sub.id
WHERE stu.id = (%s);
'''
cursor.execute(select_all_info, (student_id,))
all_info = (cursor.fetchall())
print(f'Вся информация о студенте - {all_info}')

cursor.close()
db.close()
