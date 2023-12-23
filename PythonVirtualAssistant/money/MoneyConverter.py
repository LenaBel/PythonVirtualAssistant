from typing import Any
from money import MoneyType
import requests

class MoneyConverter:

    def get_exchange_rates(self, summ: float, valuta_from: Any, valuta_to: Any) -> str:
        # todo return курс нужных валют
        pass

    
    def convert_money(self) -> str:
        try:
            summ: float = input('сумма: ')
            valuta_from = input('из валюты: ')
            valuta_to = input('в валюту: ')
            return self.get_exchange_rates(summ, valuta_from, valuta_to)
        except:
           print("Ошибка. Попробуйте ещё раз")
                                       





