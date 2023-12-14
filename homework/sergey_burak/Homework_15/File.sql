INSERT INTO `groups` (title, start_date, end_date) VALUES ('BGPA_107227', 'sep 1997', 'jun 2002')
INSERT INTO students (name, second_name, group_id) VALUES ('Sergey', 'Burak', 7)

INSERT INTO books  (title, taken_by_student_id) VALUES ('Turbo Pascal', 25)
INSERT INTO books  (title, taken_by_student_id) VALUES ('VisualC++', 25)
UPDATE books SET taken_by_student_id=25 WHERE id=9

INSERT INTO subjets (title) VALUES ('Higher mathematics')
INSERT INTO subjets (title) VALUES ('Physics')
INSERT INTO subjets (title) VALUES ('SUBD')

INSERT INTO lessons (title, subject_id) VALUES ('Math analys', 9)
INSERT INTO lessons (title, subject_id) VALUES ('Math logic', 9)
INSERT INTO lessons (title, subject_id) VALUES ('Kinematics', 10)
INSERT INTO lessons (title, subject_id) VALUES ('Mechanics', 10)
INSERT INTO lessons (title, subject_id) VALUES ('Relational DB', 11)
INSERT INTO lessons (title, subject_id) VALUES ('NonSQL DB', 11)

INSERT INTO marks (value, lesson_id, student_id) VALUES (2,19,25)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('UD',20,25)
INSERT INTO marks (value, lesson_id, student_id) VALUES (3,21,25)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('XOR',22,25)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('OTL',23,25)
INSERT INTO marks (value, lesson_id, student_id) VALUES (4,24,25)

SELECT s.name, s.second_name, l.title, m.value
FROM students s
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
WHERE student_id  = 25

SELECT * FROM books WHERE taken_by_student_id =25


SELECT s.name, s.second_name, g.title, b.title, l.title, sj.title, m.value
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets sj ON l.subject_id = sj.id
WHERE s.second_name = 'Burak'