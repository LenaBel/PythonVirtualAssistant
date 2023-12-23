import math

class Calculator:
    

    def __add(self, x, y) -> float:
        return x + y


    def __subtract(self, x, y) -> float:
        return x - y


    def __multiply(self, x, y) -> float:
        return x * y


    def __divide(self, x, y) -> float:
        return x / y


    def __percent(self):
        try:
            num1 = float(input("Введите число равное 100%: "))
            num2 = float(input("Введите % для вычисления: "))
            print(num2, '% от', num1, '=', num1*num2/100)
        except ValueError:
            print("Введено неверное значение. Введите число.")


    def __exponentiation(self):
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите степень для возведения: "))
            print(num1, 'в', num2, 'степени =', num1**num2)
        except ValueError:
            print("Введено неверное значение.")


    def __log(self):
        print('Логарифм первого числа по основанию второго')
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            print('Логарифм', num1, 'от', num2, '=', math.log(num1, num2))
        except ValueError:
            print("Введено неверное значение.")


    def calculate(self):
        while True:
            operation = input('''Выберите номер операции: 
                     1. Сложить
                     2. Вычесть
                     3. Умножить
                     4. Разделить
                     5. Процент
                     6. Возведение в степень
                     7. Вычисление логарифма 
                     8. Вернуться в основное меню виртуального помощника \n''')

            if operation in ('1', '2', '3', '4'):
                try:
                    num1 = float(input("Введите первое число: "))
                    num2 = float(input("Введите второе число: "))
                except ValueError:
                    print("Введено неверное значение")
                    continue

                if operation == '1':
                    print(num1, '+', num2, '=', self.__add(num1, num2))

                elif operation == '2':
                    print(num1, '-', num2, '=', self.__subtract(num1, num2))

                elif operation == '3':
                    print(num1, '*', num2, '=', self.__multiply(num1, num2))

                elif operation == '4':
                    print(num1, '/', num2, '=', self.__divide(num1, num2))
        
            elif operation == '5':
                self.__percent()

            elif operation == '6':
                self.__exponentiation()

            elif operation == '7':
                self.__log()

            elif operation == '8':
                break
            else:
                print("Неверный ввод")




