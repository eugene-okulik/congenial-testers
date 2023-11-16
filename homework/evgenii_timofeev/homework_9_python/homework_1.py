import datetime

my_time = "Jan 15, 2023 - 12:05:33"

data_for_python = datetime.datetime.strptime(my_time, "%b %d, %Y - %H:%M:%S")
month_name = data_for_python.strftime("%B")
full_data_name = data_for_python.strftime("%d.%m.%Y, %H:%M")
print(f"Название месяца - {month_name} \nПолная дата - {full_data_name}")
