import os, time
from sys import platform
#Привет, это программа-задачник!

#Функция для очистки терминала от визуального мусора
def clear_shell():
    if platform == "linux" or platform == "linux2":
        print('linux')
        os.system('clear')
    elif platform == "darwin":
        print('history -c')
    elif platform == "win32":
        print('windows')
        os.system('cls')
clear_shell()

#Создадим необходимое окружение для задачника

#Создадим двумерный массив для название и описание задач. Для большей масштабируемости можно было бы использовать numpy, но в целом излишне для такой задачи  
tasks = [[], []]

#Создадим функции задачника

#Функция ожидание перед каждой функцией
def task_sleep(time_sleep):
    time.sleep(time_sleep)
#Функция проверки пустоты задачника
def task_check():
    if len(tasks[0]) == 0:
        print('\033[31mНевозможно удалить задачу, нет задач\033[0m')
        task_sleep(1)
        return 0
    else:
        return 1
#Функция добавление задачи
def task_add():
    clear_shell()
    tasks[0].append(input('\033[33mНапиши название задачи:\033[0m '))
    tasks[1].append(input('\033[33mНапиши описание задачи:\033[0m '))
    print('\n\033[32mЗадача добавлена')
    task_sleep(1)
#Функция просмотра задачи, перебирает массив
def task_view(call):
    clear_shell()
    if task_check() == 0:
        return
    else:
        print ('Название задачи | Описание задачи\033[33m')
        for i in range(len(tasks[0])):
            print(tasks[0][i], '|', tasks[1][i])
        if call == 1:
            input('\n\033[32mНажмите Enter, чтобы вернуться назад')
#Функция удаление задачи по названию
def task_remove():
    clear_shell()
    if task_check() == 0:
        return
    else:
        task_view(0)
        tasks[0].remove(input('\033[35mУдалить задачу по названию задачи: '))
        print('\033[31mЗадача удаленна')
        task_sleep(1)
#Функция выхода из задачника
def task_exit():
    print('\033[32mПриятно было с тобой работать, пока!')
    task_sleep(1)
    clear_shell()
    quit()
#Кладу всё нужное в словарь, так будет проще обращаться к нему и вызывать нужные функции
menu = {
    1:'1.Добавить задачу',
    2:'2.Просмотреть все задачи', 
    3:'3.Удалить задачу', 
    4:'4.Выйти из программы'
    }
#Функция отображение меню в терминале 
def menu_loading():
    print('\033[34m----------------------------------------------------------------------------')
    for i in range (len(menu)):
        print(list(dict.values(menu))[i])
    print('----------------------------------------------------------------------------\nПривет, ты попал в задачник, выбери нужное действие ^_^\033[0m')
#Запуск программы происходит тут, сделаем бексонечный цикл-костыль, который будет крутить все наши функции
i = 1
while i >= 0:
    clear_shell()
    menu_loading()
    menu_task_fuction = input()
    #Объявляем switch-case конструкцию для обращение к нужным функциям
    match menu_task_fuction:
        case '1':
            task_add()
        case '2':
            task_view(1)
        case '3':
            task_remove()
        case '4':
            task_exit()
        case _:
            print('\033[31mЯ тебя не понял.')
            task_sleep(0.25)