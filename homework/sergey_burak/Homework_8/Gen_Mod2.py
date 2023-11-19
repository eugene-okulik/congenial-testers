# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
import sys
sys.set_int_max_str_digits(100000)


def fibonachi_num():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# count = 0
# for num in fibonachi_num():
#     count += 1
#     if count == 5:
#         print(num)
#     elif count == 200:
#         print(num)
#     elif count == 1000:
#         print(num)
#     elif count == 10**5:
#         print(num)
#         break
def output_fibonachi(*args):
    count = 0
    for arg in fibonachi_num():
        count += 1
        if count in args:
            print(arg)
        elif count >= max(args):
            break


output_fibonachi(5, 200, 1000, 100000)