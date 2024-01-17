import mysql.connector as mysql


db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st4',
    passwd='AVNS_ANI6HFK07yLk4d9l4Nq',
    database='st4'
)
cursor = db.cursor(dictionary=True)

# Создайте студента (student)
query1 = "INSERT INTO students (name, second_name, group_id) values ('Nikita2', 'Bukreev2', 1)"
cursor.execute(query1)
student_id = cursor.lastrowid

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
query2 = f'''INSERT INTO books (title, taken_by_student_id) values ('SQL for beginners2', {student_id}),
('AZBYKA2', {student_id}), ('C#2', {student_id})'''
cursor.execute(query2)

# Создайте группу (group) и определите своего студента туда
query3_1 = "INSERT INTO `groups` (title, start_date, end_date) values ('st4_2', 'october 2123_2', 'february 2124_2')"
cursor.execute(query3_1)
group_id = cursor.lastrowid

query3_2 = f'''update students set group_id = (select id from `groups` where id = {group_id})
where id = {student_id}'''
cursor.execute(query3_2)

# Создайте несколько учебных предметов (subjects)
query4_1 = "INSERT INTO subjets (title) values ('QA2')"
cursor.execute(query4_1)
subject_id_one = cursor.lastrowid

query4_2 = "INSERT INTO subjets (title) values ('Dev2')"
cursor.execute(query4_2)
subject_id_two = cursor.lastrowid

query4_3 = "INSERT INTO subjets (title) values ('PM2')"
cursor.execute(query4_3)
subject_id_three = cursor.lastrowid

# Создайте по два занятия для каждого предмета (lessons)
query5_1 = f"INSERT INTO lessons (title, subject_id) values ('Весь нобрь2', {subject_id_one})"
cursor.execute(query5_1)
lesson_id_one = cursor.lastrowid

query5_2 = f"INSERT INTO lessons (title, subject_id) values ('Весь декабрь2', {subject_id_one})"
cursor.execute(query5_2)
lesson_id_two = cursor.lastrowid

query5_3 = f"INSERT INTO lessons (title, subject_id) values ('Весь январь2', {subject_id_two})"
cursor.execute(query5_3)
lesson_id_three = cursor.lastrowid

query5_4 = f"INSERT INTO lessons (title, subject_id) values ('Весь февраль2', {subject_id_two})"
cursor.execute(query5_4)
lesson_id_four = cursor.lastrowid

query5_5 = f"INSERT INTO lessons (title, subject_id) values ('Весь март2', {subject_id_three})"
cursor.execute(query5_5)
lesson_id_five = cursor.lastrowid

query5_6 = f"INSERT INTO lessons (title, subject_id) values ('Весь апрель2', {subject_id_three})"
cursor.execute(query5_6)
lesson_id_six = cursor.lastrowid

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
query6 = f'''INSERT INTO marks (value, lesson_id, student_id)
values ('100500_2', {lesson_id_one}, {student_id}),
('8_2', {lesson_id_two}, {student_id}),
('800_2', {lesson_id_three}, {student_id}),
('555_2', {lesson_id_four}, {student_id}),
('35_2', {lesson_id_five}, {student_id}),
('53_2', {lesson_id_six}, {student_id})'''
cursor.execute(query6)

db.commit()

# Все оценки студента
query7 = f'''SELECT l.title as 'Занятие', s.title as 'Предмет', m.value as 'Оценка' from marks m
JOIN lessons l on m.lesson_id = l.id
JOIN subjets s on l.subject_id = s.id
WHERE m.student_id = {student_id}'''
cursor.execute(query7)
print(cursor.fetchall())

# Все книги, которые находятся у студента
query8 = f"select title as 'Книги' from books where taken_by_student_id = {student_id}"
cursor.execute(query8)
print(cursor.fetchall())

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги,
# оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
query9 = f'''SELECT DISTINCT  s.name as 'Имя', s.second_name as 'Фамилия', g.title as 'Название группы',
b.title as 'Книги студента', m.value as 'Оценка', l.title as 'Занятие', s2.title as 'Предмет'
FROM students s
JOIN `groups` g on g.id = s.group_id
JOIN books b on b.taken_by_student_id = s.id
JOIN marks m on m.student_id = s.id
JOIN lessons l on l.id = m.lesson_id
JOIN subjets s2 on s2.id = l.subject_id
WHERE s.id = {student_id}'''
cursor.execute(query9)
print(cursor.fetchall())

cursor.close()
db.close()
