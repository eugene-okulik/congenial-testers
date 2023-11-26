import datetime
import os


def data_writer(file_path):
    with open(file_path, "r") as file:
        for line in file:
            # divide line on 2 parts
            line_with_date = line.strip().split(" - ")
            # create 2 variables, 1 for number in the line(1,2,3) 2 for date (2023-06-12 15:23:45.312167)
            number_in_line, date_in_line = line_with_date[0].split(". ")
            date_in_line_iso_format = datetime.datetime.fromisoformat(date_in_line)

            if number_in_line == "1":
                print(
                    f"{date_in_line} через неделю будет такой "
                    f"{date_in_line_iso_format + datetime.timedelta(weeks=1)}"
                )
            elif number_in_line == "2":
                print(
                    f"День недели у {date_in_line} - {date_in_line_iso_format.strftime('%A')}"
                )
            elif number_in_line == "3":
                days_ago = (datetime.datetime.now() - date_in_line_iso_format).days
                print(f"Дата {date_in_line} была {days_ago} дней назад")
            else:
                print(
                    f"Строка не входит в условие, поэтому посмотрим на красвиую дату {date_in_line}"
                )


current_dir = os.path.dirname(__file__)
homework_dir = os.path.dirname(os.path.dirname(current_dir))
path_to_file = os.path.join(homework_dir, "eugeny_okulik", "hw_13", "data.txt")

data_writer(path_to_file)
