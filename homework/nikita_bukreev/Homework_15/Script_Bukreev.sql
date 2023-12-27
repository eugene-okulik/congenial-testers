-- Создайте студента (student)
INSERT INTO students (name, second_name, group_id) 
values ('Nikita', 'Bukreev', 1)

-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books (title, taken_by_student_id) 
values ('SQL for beginners', 90),
('AZBYKA', 90),
('C#', 90)

-- Создайте группу (group) и определите своего студента туда
INSERT INTO `groups` (title, start_date, end_date) 
values ('st4', 'october 2023', 'february 2024')

update students 
set group_id = (select id from `groups` where title = 'st4')
where name = 'Nikita' and second_name = 'Bukreev'

-- Создайте несколько учебных предметов (subjects)
INSERT INTO subjets (title) values ('QA'), ('Dev'), ('PM')

-- Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id)
values ('Весь нобрь', (select id from subjets where title = 'QA')),
('Весь декабрь', (select id from subjets where title = 'QA')),
('Весь январь', (select id from subjets where title = 'Dev')),
('Весь февраль', (select id from subjets where title = 'Dev')),
('Весь март', (select id from subjets where title = 'PM')),
('Весь апрель', (select id from subjets where title = 'PM'))

-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT INTO marks (value, lesson_id, student_id)
values ('100500', (select id from lessons where title = 'Весь нобрь'), 90),
('100500', (select id from lessons where title = 'Весь декабрь'), 90),
('100500', (select id from lessons where title = 'Весь январь'), 90),
('100500', (select id from lessons where title = 'Весь февраль'), 90),
('100500', (select id from lessons where title = 'Весь март'), 90),
('100500', (select id from lessons where title = 'Весь апрель'), 90)

-- Все оценки студента
SELECT l.title as 'Занятие', s.title as 'Предмет', m.value as 'Оценка' from marks m 
JOIN lessons l on m.lesson_id = l.id 
JOIN subjets s on l.subject_id = s.id 
WHERE m.student_id = 90

-- Все книги, которые находятся у студента
select title as 'Книги' from books 
where taken_by_student_id = 90

-- Для вашего студента выведите всё, что о нем есть в базе: группа, книги, 
-- оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
SELECT DISTINCT  s.name as 'Имя', s.second_name as 'Фамилия', g.title as 'Название группы', 
b.title as 'Книги студента', m.value as 'Оценка', l.title as 'Занятие', s2.title as 'Предмет'
FROM students s 
JOIN `groups` g on g.id = s.group_id 
JOIN books b on b.taken_by_student_id = s.id 
JOIN marks m on m.student_id = s.id 
JOIN lessons l on l.id = m.lesson_id 
JOIN subjets s2 on s2.id = l.subject_id 
WHERE s.id = 90
-- вот тут у меня что-то не получилось, не смог сделать так, чтобы вывелись только уникальные значения((

