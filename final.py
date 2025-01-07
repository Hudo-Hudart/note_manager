# В Завершение этапа 1
# Сказано реализовать note как словарь.
# Ниже реализация через словарь.
username = input("Введите имя пользователя:")
titles = [input("Введите заголовок заметки:")]
title_adding = True
while title_adding:
    title_adding_process = input("Вы хотите добавить ещё заголовки к заметке?\nY-Да\nN-Нет\n")
    if (title_adding_process == "y") or (title_adding_process == "Y"):
        titles.append(input("Введите дополнительный заголовок заметки:"))
    else:
        title_adding = False
        del title_adding_process
content= input ("Введите описание заметки:")
status = input ("Введите статус заметки:")
created_date = input ("Введите дату создания заметки в формате dd-mm-year:")
issue_date = input ("Введите дату истечения заметки в формате dd-mm-year:")
note = {'Username': username, 'Titles': titles, 'Content': content,
        'Status': status, 'Created_date': created_date, 'Issue_date': issue_date}
print("Имя пользователя:", note['Username'])
print("Заголовки заметки:", *note['Titles'])
print("Описание заметки:", note['Content'])
print("Статус заметки:", note['Status'])
print("Дата создания заметки:", note['Created_date'][0:5])
print("Дата истечения заметки:", note['Issue_date'][0:5], end='')
#//////////////////////////////////////////////////////////////////////////////////////
# В Grade 1. Этап1: Задание 5
# Сказано реализовать note как список.
# Ниже реализация через список.

# note = [input("Введите имя пользователя:")]
# titles = [input("Введите заголовок заметки:")]
# title_adding = True
# while title_adding:
#     title_adding_process = input("Вы хотите добавить ещё заголовки к заметке?\nY-Да\nN-Нет\n")
#     if (title_adding_process == "y") or (title_adding_process == "Y"):
#         titles.append(input("Введите дополнительный заголовок заметки:"))
#     else:
#         title_adding = False
#         del title_adding_process
# note.append(titles)
# note.append(input ("Введите описание заметки:"))
# note.append(input ("Введите статус заметки:"))
# note.append(input ("Введите дату создания заметки в формате dd-mm-year:"))
# note.append(input ("Введите дату истечения заметки в формате dd-mm-year:"))
# for i in range(6):
#     if i != 1:
#         print(note[i])
#     else:
#         print(*note[i], sep = ', ')
