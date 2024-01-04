INSERT INTO `groups` (title, start_date, end_date) VALUES ('QA', 'Oct 2023', 'Feb 2024')

INSERT INTO students (name, second_name, group_id) VALUES ('Yuliya', 'Hetsman', '55')

INSERT INTO books (title, taken_by_student_id) VALUES ('Manual testing', '96')
INSERT INTO books (title, taken_by_student_id) VALUES ('Automation testing', '96')

INSERT INTO subjets (title) VALUES ('Subject 1')
INSERT INTO subjets (title) VALUES ('Subject 2')

INSERT INTO lessons (title, subject_id) VALUES ('Lesson 1', '124')
INSERT INTO lessons (title, subject_id) VALUES ('Lesson 2', '124')
INSERT INTO lessons (title, subject_id) VALUES ('Lesson 3', '125')
INSERT INTO lessons (title, subject_id) VALUES ('Lesson 4', '125')

INSERT INTO marks  (value, lesson_id, student_id) VALUES ('10', '432', '96')
INSERT INTO marks  (value, lesson_id, student_id) VALUES ('7', '433', '96')
INSERT INTO marks  (value, lesson_id, student_id) VALUES ('9', '434', '96')
INSERT INTO marks  (value, lesson_id, student_id) VALUES ('10', '435', '96')

SELECT * FROM marks WHERE student_id = '96'

SELECT * FROM books WHERE taken_by_student_id = '96'

SELECT s.name, s.second_name, g.title, b.title, l.title, sub.title, m.value
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets sub ON l.subject_id = sub.id
WHERE s.id = '96'