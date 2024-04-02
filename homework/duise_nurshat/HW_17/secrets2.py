import mysql.connector as mysql
import os
import dotenv
import csv

encoding = 'utf-8'

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)
all_info_query = '''
    select
        s.name, s.second_name,
        g.title as `group`,
        b.title as book,
        g.start_date, g.end_date,
        sub.title  as subject,
        m.value as mark,
        l.title as lesson
    from students as s
    left join `groups` as g on g.id = s.group_id
    left join books as b on s.id = b.taken_by_student_id
    left join marks as m on s.id = m.student_id
    left join lessons as l on m.lesson_id = l.id
    left join subjets as sub on l.subject_id = sub.id
    order by name asc;
'''
cursor.execute(all_info_query)
all_info = cursor.fetchall()
db.commit()
db.close()

base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
needed_file_path = os.path.join(file_path, 'eugeny_okulik', 'Lesson_17', 'hw_data', 'db_data.csv')

with open(needed_file_path, newline='', encoding=encoding) as csv_file:
    csv_data = csv.reader(csv_file)
    data = []
    for row in csv_data:
        data.append(row)

skipped_data = []
for row in data:
    if row not in all_info:
        skipped_data.append(row)

print(skipped_data)
