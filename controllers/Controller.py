class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_convert_action(self.convert_currency)

    def convert_currency(self):
        amount = self.view.get_amount()
        if amount is None:
            self.view.update_result(None, "")
            return

        from_currency, to_currency = self.view.get_selected_currencies()
        result = self.model.convert_currency(amount, from_currency, to_currency)
        self.view.update_result(result, to_currency)
