
from datetime import datetime

date_string = "Jan 15, 2023 - 12:05:33"
date_format = "%b %d, %Y - %H:%M:%S"

parsed_date = datetime.strptime(date_string, date_format)

print(parsed_date.strftime("%B"))
print(parsed_date.strftime('%d.%m.%Y, %H:%M'))
