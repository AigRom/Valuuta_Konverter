from models.CurrencyConverter import CurrencyConverter

class Model:
    def __init__(self):
        api_key = "8942a46e782565dca3b704e8"  # Minu api võti
        self.converter = CurrencyConverter(api_key)

    def convert_currency(self, amount, from_currency, to_currency):
        return self.converter.convert(amount, from_currency, to_currency)
