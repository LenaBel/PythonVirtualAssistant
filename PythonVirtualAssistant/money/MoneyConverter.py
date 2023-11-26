from money import MoneyType

class MoneyConverter:

    def get_exchange_rates(self, valuta_from: MoneyType, valuta_to: MoneyType) -> float:
        # todo return курс нужных валют
        pass

    
    def convert_moey(self, valuta_from: MoneyType, valuta_to: MoneyType, summ: float) -> str:
        rate = self.get_exchange_rates(valuta_from, valuta_to)
        return print(summ * rate)
                                       





