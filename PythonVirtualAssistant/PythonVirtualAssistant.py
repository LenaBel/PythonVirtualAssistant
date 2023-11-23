#Задача минимум
#Написать виртуального помощника (служба + консольный клиент).
#Приложение интерпретирует команды пользователя, выполняя ряд полезных операций:
#Установить будильник/напоминание на указанное время.
#Вычислить математическое выражение/найти корни уравнения/построить график функции/и т.п. (чем сложнее, тем лучше).
#Показать прогноз погоды.
#Сконвертировать валюты по текущему курсу (любому).

#Дополнительные навороты (желательно, но не обязательно)
#Добавить поддержку плагинов (пользовательских команд).
#Прикрутить историю команд и удобный способ навигации по ней.
#Добавить GUI приложение для конфигурации.

import math
import datetime
import enum


class Money(enum.Enum):
    ruble = 1
    dollar = 2
    euro = 3


def set_alarm(): #(date, hour, minute):
    pass


def calculate_math(): #(*args, operation):
    pass


def get_weather():
    pass


def convert_money(): #(valuta1, valuta2):
    pass


def print_wrong_input():
    print("Введено неверное значение. Попробуйте ещё раз.")


def start_virtual_assistant():
    operation = input('''Выберите номер операции: 1. Установить будильник 
                         2. Вычислить математическую операцию 
                         3. Показать прогноз погоды 
                         4. Сконвертировать валюту\n''')
    try:
        operation_number = int(operation)
        # switch case?
        if operation_number == 1:
            set_alarm()
        elif operation_number == 2:
            calculate_math()
        elif operation_number == 3:
            get_weather()
        elif operation_number == 4:
            convert_money()
        else:
            print_wrong_input()
    except:
        print_wrong_input()

    start_virtual_assistant()
    


start_virtual_assistant()
