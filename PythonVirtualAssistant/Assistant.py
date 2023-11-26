from alarm import AlarmManager
from calculator import Сalculator
from money import MoneyConverter
from weather import WeatherGetter


class Assistant:

    def set_alarm(self): #(date, hour, minute):
        pass


    def calculate_math(self): #(*args, operation):
        pass


    def get_weather(self):
        pass


    def convert_money(self): #(valuta1, valuta2):
        pass


    def print_wrong_input(cls):
        print("Введено неверное значение. Попробуйте ещё раз.")


    def start_virtual_assistant(self):
        operation = input('''Выберите номер операции: 1. Установить будильник 
                             2. Вычислить математическую операцию 
                             3. Показать прогноз погоды 
                             4. Сконвертировать валюту\n''')
        try:
            operation_number = int(operation)
            # switch case?
            if operation_number == 1:
                self.set_alarm()
            elif operation_number == 2:
                self.calculate_math()
            elif operation_number == 3:
                self.get_weather()
            elif operation_number == 4:
                self.convert_money()
            else:
                self.print_wrong_input()
        except:
            self.print_wrong_input()

        self.start_virtual_assistant()




