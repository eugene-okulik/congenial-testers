INSERT INTO students (name, second_name, group_id) VALUES ('Evgeniy', 'Puysho', 1)
INSERT INTO books (title, taken_by_student_id) VALUES ('QA basics', 136),  ('book name', 136)
INSERT INTO  `groups` (title, start_date, end_date) VALUES ('New group', 'jan 22', 'feb 28')
UPDATE students SET group_id = 95 where id = 136 
INSERT INTO subjets (title) VALUES ('Матеша'), ('Русская literatura'), ('Физическая cultura')
INSERT INTO lessons (title, subject_id) VALUES ('Вторник', 168), ('Четверг', 169), ('Суббота', 170)
INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 492, 136), (4, 493, 136), (10, 494, 136)


SELECT value  FROM marks WHERE student_id = 136
SELECT title FROM books WHERE taken_by_student_id = 136

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
WHERE stu.id = 136;