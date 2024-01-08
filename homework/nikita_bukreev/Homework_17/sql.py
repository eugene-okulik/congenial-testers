from connection import db_query as db


query = '''SELECT DISTINCT  s.name, s.second_name, g.title as 'group_title', 
b.title as 'book_title', s2.title as 'subject_title', l.title as 'lesson_title', m.value as 'mark_value'
FROM students s 
JOIN `groups` g on g.id = s.group_id 
JOIN books b on b.taken_by_student_id = s.id 
JOIN marks m on m.student_id = s.id 
JOIN lessons l on l.id = m.lesson_id 
JOIN subjets s2 on s2.id = l.subject_id'''

result = db(query)
