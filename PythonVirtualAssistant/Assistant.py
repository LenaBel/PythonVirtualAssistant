from alarm.AlarmManager import AlarmManager
from calculator.Сalculator import Calculator
from money.MoneyConverter import MoneyConverter
from weather.WeatherGetter import WeatherGetter
import time

class Assistant:


    def __init__(self, alarmManager: AlarmManager):
        self.__alarmManager = alarmManager

    def __start_alarm(self):
        self.__alarmManager.start_manage_alarms()


    def __calculate_math(self):
        calc = Calculator()
        calc.calculate()


    def __convert_money(self):
        money_converter = MoneyConverter()
        money_converter.start_money_converter()


    def __print_wrong_input(cls):
        print("Введено неверное значение. Попробуйте ещё раз.")


    def start_virtual_assistant(self):
        operation = input('''Выберите раздел: 1. Будильник 
                 2. Калькулятор 
                 3. Прогноз погоды
                 4. Конвертер валют
                 5. Выход\n''')
        try:
            if operation == '1':
                self.__start_alarm()

            elif operation == '2':
                self.__calculate_math()

            elif operation == '3':
                city_name = input('Введите название города: ')
                WeatherGetter.get_weather_scheme(city_name)

            elif operation == '4':
                self.__convert_money()

            elif operation == '5':
                return

            else:
                self.__print_wrong_input()

        except Exception as err:
            print(f'Error: {err}')

        time.sleep(1)
        self.start_virtual_assistant()




