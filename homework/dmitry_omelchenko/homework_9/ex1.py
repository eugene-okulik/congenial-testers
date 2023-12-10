from datetime import datetime

date_string = "Jan 15, 2023 - 12:05:33"

date_object = datetime.strptime(date_string, "%b %d, %Y - %H:%M:%S")

month_name = date_object.strftime("%B")
print(f"Полное название месяца: {month_name}")

new_date_format = date_object.strftime("%d.%m.%Y, %H:%M")
print(f"Дата в новом формате: {new_date_format}")
