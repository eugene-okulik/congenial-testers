-- Добавление студента
insert into students (name, second_name, group_id)
values ('Nurshat', 'Duise', 124)

-- Добавление книги
insert into books (title, taken_by_student_id)
values
	('1984', 184),
	('Lists', 184),
	('ASU', 184);

-- Создание группы
insert into `groups` (title, start_date, end_date)
values ('DNA group', '01/04/24', '01/04/25')

-- Создание учебных предметов
insert into subjets (title)
values
	('Мат. анализ'),
	('Труд'),
	('Python. Основы'),
	('JAVA. Basic')

-- Создание занятии для предметов
INSERT INTO lessons (title, subject_id)
values
	('Занятие в пн', 191),
	('Занятие в вт', 191),
	('Занятие в ср', 192),
	('Занятие в чт', 192),
	('Занятие в пт', 193),
	('Занятие в сб', 193),
	('Занятие в летом', 194),
	('Занятие в весной', 194);

-- Ставка оценки
INSERT INTO marks (value, lesson_id, student_id)
values
	(1, 509, 184),
	(2, 510, 184),
	(3, 511, 184),
	(4, 512, 184),
	(5, 513, 184),
	(6, 514, 184),
	(7, 515, 184),
	(8, 516, 184);

-- Получите информацию из базы данных:
-- Все оценки студента
select * from marks m where m.student_id = 184

-- Все книги, которые находятся у студента
select * from books b where b.taken_by_student_id = 184

-- Для вашего студента выведите всё, что о нем есть в базе: группа, книги,
-- оценки с названиями занятий и предметов (всё одним запросом с использованием Join)

SELECT * FROM `groups` g
JOIN students s ON g.id = s.group_id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s2 ON l.subject_id = s2.id
where s.id = 184