import time
from currency_converter import CurrencyConverter


class MoneyConverter:

    def __init__(self):
        self.__conv: CurrencyConverter = CurrencyConverter()

    def __help(self):
        print('Доступные коды валют:')
        print(self.__conv.currencies)


    def __convert(self, summ: float, valuta_from: str, valuta_to: str):
        try:
            res = self.__conv.convert(summ, valuta_from, valuta_to)
            print('Результат: ' + str(summ) + valuta_from + ' = ' + str(res) + valuta_to)
        except Exception as ex:
            print(ex)


    def start_money_converter(self):
        print('Запущен конвертер валют на базе данных Европейсого центрального банка (https://www.ecb.europa.eu/home/html/index.en.html)')
        while True:
            time.sleep(1)
            operation = input('''Выберите номер операции: 
                     1. Получить курс валют
                     2. Сконвертировать валюту
                     3. Показать доступные коды валют
                     4. Вернуться в основное меню виртуального помощника \n''')

            if operation == '1':
                print('Узнать курс валюты 1 по отношению к валюте 2. Введите коды валют.')
                valuta1 = input("Введите код валюты 1: ")
                valuta2 = input("Введите код валюты 2: ")
                self.__convert(1, valuta1.upper(), valuta2.upper())

            elif operation == '2':
                try:
                    print('Сконвертировать валюту 1 в валюту 2. Введите сумму и коды валют.')
                    summ = float(input("Введите сумму: "))
                    valuta1 = input("Введите код валюты 1: ")
                    valuta2 = input("Введите код валюты 2: ")
                    self.__convert(summ, valuta1.upper(), valuta2.upper())
                except ValueError:
                    print('Неверно введена сумма')

            elif operation == '3':
                self.__help()

            elif operation == '4':
                break

            else:
                print("Неверный ввод")
