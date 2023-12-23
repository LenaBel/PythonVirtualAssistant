from alarm.AlarmManager import AlarmManager
from calculator.Сalculator import Calculator
from money.MoneyConverter import MoneyConverter
from weather.WeatherGetter import WeatherGetter
import time


class Assistant:

    def __set_alarm(self): #(date, hour, minute):
        pass


    def __calculate_math(self):
        calc = Calculator()
        calc.calculate()


    def __convert_money(self): #(valuta1, valuta2):
        pass


    def __print_wrong_input(cls):
        print("Введено неверное значение. Попробуйте ещё раз.")


    def start_virtual_assistant(self):
        operation = input('''Выберите раздел: 1. Будильник 
                 2. Калькулятор 
                 3. Прогноз погоды в Томске
                 4. Конвертер валют
                 5. Выход\n''')
        try:
            if operation == '1':
                self.__set_alarm()

            elif operation == '2':
                self.__calculate_math()

            elif operation == '3':
                WeatherGetter.get_Tomsk_weather()

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




