import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"
        self.rates = {}
        self.update_rates()

    def update_rates(self, base_currency="EUR"):
        try:
            response = requests.get(self.api_url + base_currency)
            data = response.json()
            if data["result"] == "success":
                self.rates = data["conversion_rates"]
            else:
                print("API viga: ", data)
        except Exception as e:
            print("Viga valuutakursside hankimisel:", e)

    def convert(self, amount, from_currency, to_currency):
        if from_currency in self.rates and to_currency in self.rates:
            return amount * (self.rates[to_currency] / self.rates[from_currency])
        else:
            return None
