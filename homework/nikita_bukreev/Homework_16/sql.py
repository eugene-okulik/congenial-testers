from connect import db_query


# Создайте студента (student)
query1 = "INSERT INTO students (name, second_name, group_id) values ('Nikita1', 'Bukreev1', 1)"
db_query(query1)
query0 = "SELECT id FROM students order by id desc limit 1"
last_user_id = [item['id'] for item in db_query(query0)][0]
print(last_user_id)

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
query2 = f'''INSERT INTO books (title, taken_by_student_id) values ('SQL for beginners1', {last_user_id}),
('AZBYKA1', {last_user_id}), ('C#1', {last_user_id})'''
db_query(query2)

# Создайте группу (group) и определите своего студента туда
query3_1 = "INSERT INTO `groups` (title, start_date, end_date) values ('st4_1', 'october 2123', 'february 2124')"
query3_2 = f'''update students set group_id = (select id from `groups` where title = 'st4_1')
where id = {last_user_id}'''
db_query(query3_1)
db_query(query3_2)

# Создайте несколько учебных предметов (subjects)
query4 = "INSERT INTO subjets (title) values ('QA1'), ('Dev1'), ('PM1')"
db_query(query4)

# Создайте по два занятия для каждого предмета (lessons)
query5 = '''INSERT INTO lessons (title, subject_id) values
('Весь нобрь1', (select id from subjets where title = 'QA1')),
('Весь декабрь1', (select id from subjets where title = 'QA1')),
('Весь январь1', (select id from subjets where title = 'Dev1')),
('Весь февраль1', (select id from subjets where title = 'Dev1')),
('Весь март1', (select id from subjets where title = 'PM1')),
('Весь апрель1', (select id from subjets where title = 'PM1'))'''
db_query(query5)

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
query6 = f'''INSERT INTO marks (value, lesson_id, student_id)
values ('100500', (select id from lessons where title = 'Весь нобрь1'), {last_user_id}),
('8', (select id from lessons where title = 'Весь декабрь1'), {last_user_id}),
('800', (select id from lessons where title = 'Весь январь1'), {last_user_id}),
('555', (select id from lessons where title = 'Весь февраль1'), {last_user_id}),
('35', (select id from lessons where title = 'Весь март1'), {last_user_id}),
('53', (select id from lessons where title = 'Весь апрель1'), {last_user_id})'''
db_query(query6)

# Все оценки студента
query7 = f'''SELECT l.title as 'Занятие', s.title as 'Предмет', m.value as 'Оценка' from marks m
JOIN lessons l on m.lesson_id = l.id
JOIN subjets s on l.subject_id = s.id
WHERE m.student_id = {last_user_id}'''
print(db_query(query7))

# Все книги, которые находятся у студента
query8 = f"select title as 'Книги' from books where taken_by_student_id = {last_user_id}"
print(db_query(query8))

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
WHERE s.id = {last_user_id}'''
print(db_query(query9))
