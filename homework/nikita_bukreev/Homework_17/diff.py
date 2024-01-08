from read_csv import data as csv_data
from sql import result as sql_data


diff_1 = [x for x in csv_data if x not in sql_data]
print(diff_1)

# Решил двумя способами, воторой оставил на память)
# diff_2 = []
# for x in csv_data:
#     if x not in sql_data:
#             diff_2.append(x)
# print(diff_2)
