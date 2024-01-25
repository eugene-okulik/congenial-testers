import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)
db_all_info = '''
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
left join subjets as sub on l.subject_id = sub.id;
'''
cursor.execute(db_all_info)
db_all_info = (cursor.fetchall())
cursor.close()
db.close()

base_path = os.path.dirname(__file__)
hm_path = os.path.dirname(os.path.dirname(base_path))
hw_file_path = os.path.join(hm_path, 'eugeny_okulik', 'Lesson_17', 'hw_data', 'db_data.csv')

with open(hw_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data_csv = []
    for row in file_data:
        data_csv.append(row)

missing_data = []
for row in data_csv:
    if row not in db_all_info:
        missing_data.append(row)

print(missing_data)