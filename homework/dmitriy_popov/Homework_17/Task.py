import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()


def db_query(query):
    db = mysql.connect(
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSW'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME')
    )

    cursor = db.cursor(dictionary=True)
    cursor.execute(query)
    file_content = cursor.fetchall()
    db.commit()
    db.close()
    return file_content


if __name__ == '__main__':
    select_query = '''SELECT DISTINCT  s.name, s.second_name, g.title as 'group_title',
    b.title as 'book_title', s2.title as 'subject_title', l.title as 'lesson_title', m.value as 'mark_value'
    FROM students s
    JOIN `groups` g on g.id = s.group_id
    JOIN books b on b.taken_by_student_id = s.id
    JOIN marks m on m.student_id = s.id
    JOIN lessons l on l.id = m.lesson_id
    JOIN subjets s2 on s2.id = l.subject_id'''

    result = db_query(select_query)

    file_path = os.path.join(
        os.path.dirname(__file__), '..', '..', 'eugeny_okulik', 'Lesson_17', 'hw_data', 'db_data.csv'
    )

    with open(file_path, newline='', encoding="utf-8") as csv_file:
        file_data = csv.DictReader(csv_file)
        data = []
        for row in file_data:
            data.append(row)

    diff_csv = [x for x in result if x not in data]
    for x in diff_csv:
        print(x)
