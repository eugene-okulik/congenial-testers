import datetime

# проблема в том что код не рабочий) Он должен отрабатыватся без ошибок?

# Открываем файл
with open('homework/eugeny_okulik/hw_13/data.txt', 'r') as file:
    lines = file.readlines()

# Проходим по каждой строке
for line in lines:
    parts = line.split(' - ')  # Разделяем строку на части по тире
    date_part = parts[0]  # Получаем часть строки с датой
    action_part = parts[1]  # Получаем часть строки с действием

    # Разделяем дату и время
    date_string = date_part.split(' ')[0]  # Получаем только часть строки с датой
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')  # Преобразуем строку в объект datetime

    # Выполняем действие в зависимости от номера
    if date_part.startswith('1.'):
        # Добавляем неделю к дате и выводим результат
        new_date = date + datetime.timedelta(weeks=1)
        print(new_date.strftime('%Y-%m-%d %H:%M:%S.%f'))
    elif date_part.startswith('2.'):
        # Выводим день недели
        print(date.strftime('%A'))
    elif date_part.startswith('3.'):
        # Вычисляем количество дней между этой датой и сегодняшней
        today = datetime.datetime.now()
        days_ago = (today - date).days
        print(days_ago)
