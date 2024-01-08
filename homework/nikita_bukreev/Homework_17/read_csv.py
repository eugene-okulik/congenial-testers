import csv
import os


need_file_path = os.path.join(
    os.path.dirname(__file__), '..', '..', 'eugeny_okulik', 'Lesson_17', 'hw_data', 'db_data.csv'
)

with open(need_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)
