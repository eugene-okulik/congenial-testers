INSERT INTO students (name, second_name, group_id) values ('Maksim', 'Bahuk', 1)

INSERT INTO books (title, taken_by_student_id) values ('JS', 22)
INSERT INTO books (title, taken_by_student_id) values ('Ruby', 12)

INSERT INTO `groups` (title, start_date, end_date) values ('Lesson Ruby', 'sep 23', 'nov 23')

INSERT INTO subjets (title) values ('Алгебра')
INSERT INTO subjets (title) values ('Геометрия')
INSERT INTO subjets (title) values ('География')

INSERT INTO lessons (title, subject_id) values ('Понедельник', 1)
INSERT INTO lessons (title, subject_id) values ('Вторник', 2)

INSERT INTO marks (value, lesson_id, student_id) values (5, 1, 12)
INSERT INTO marks (value, lesson_id, student_id) values (4, 2, 22)

все оценки студента
select * from students join marks on students.id=marks.student_id 
where students.second_name = 'Bahuk' 

Все книги, которые находятся у студента
SELECT * from students join books on students.id=books.id
WHERE students.second_name = 'Boguk'

Для вашего студента выведите всё, что о нем есть в базе: 
книги, оценки с названиями занятий и предметов 
(всё одним запросом с использованием Join)
На этом месте вроде бы есть 2 варианта:
1) Вариант, но он какой то не докнца полный, при этом выкинул таблицу 'group', так как с 
запрос не работает
select * 
from students 
LEFT JOIN books on students.id = books.id
LEFT JOIN marks on books.id = marks.id 
LEFT JOIN subjets on marks.id = subjets.id
WHERE students.id  = '12'

2) Вариант более верный, и отображает вроде все то, что надо
SELECT s.id, s.name, s.second_name, g.title AS 'Group name', b.title AS 'Book name', l.title AS 'Lesson name', s2.title AS 'Subject name', m.value AS 'Оценка'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.id = '12'



