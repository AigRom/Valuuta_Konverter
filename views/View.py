
import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    def __init__(self, model):
        super().__init__()
        self.model = model

        self.__width = 800  # Suurem aken
        self.__height = 150
        self.title("Valuutakonverter")
        self.center_window(self.__width, self.__height) #Aken ekraani keskele.

        self.currencies = ["EUR", "USD", "GBP", "JPY"] #Kasutatavad valuutad.
        # Ainult numbrite sisestuse kontrollimine
        vcmd = (self.register(self.validate_number), "%P")


        ttk.Label(self, text="Minu valuuta:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
        self.from_currency = ttk.Combobox(self, values=self.currencies, font=("Arial", 12))
        self.from_currency.grid(row=1, column=1, padx=10, pady=10)
        self.from_currency.current(0)

        # Swap nuppu tegemine(kigil valuutakalkulaatoritel ju on selline :)).Loon stiili, kuna ttk.Button ei toeta otsest font määramist.
        style = ttk.Style()
        style.configure("Swap.TButton", font=("Arial", 12))

        self.swap_button = ttk.Button(self, text="⇄", command=self.swap_currencies, style="Swap.TButton")
        self.swap_button.grid(row=1, column=2, padx=10, pady=10)

        ttk.Label(self, text="Vali valuuta:", font=("Arial", 12)).grid(row=1, column=3, padx=10, pady=10)
        self.to_currency = ttk.Combobox(self, values=self.currencies, font=("Arial", 12))
        self.to_currency.grid(row=1, column=4, padx=10, pady=10)
        self.to_currency.current(1)

        ttk.Label(self, text="Summa:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self, font=("Arial", 12), validate="key", validatecommand=vcmd)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        self.convert_button = ttk.Button(self, text="Teisenda", style="Swap.TButton")
        self.convert_button.grid(row=2, column=2, padx= 10, pady=10)

        self.result_label = ttk.Label(self, text="Tulemus: ", font=("Arial", 12))
        self.result_label.grid(row=2, column=3, columnspan=5, pady=10)

    @staticmethod
    def validate_number(new_value):
        """Kontrollib, kas sisestatakse ainult numbreid ja koma"""
        if new_value == "" or new_value.replace(".", "", 1).isdigit():
            return True
        return False

    "Vahetab valitud valuutad omavahel"
    def swap_currencies(self):
        from_value = self.from_currency.get()
        to_value = self.to_currency.get()
        self.from_currency.set(to_value)
        self.to_currency.set(from_value)

    "Paigutab akna ekraani keskele."
    def center_window(self, width, height):
        x = int((self.winfo_screenwidth() / 2) - (width / 2))
        y = int((self.winfo_screenheight() / 2) - (height / 2))
        self.geometry(f'{width}x{height}+{x}+{y}')

    "Seob teisendamise nupu funktsiooniga"
    def set_convert_action(self, action):
        self.convert_button.config(command=action)

    "Tagastab kasutaja sisestatud summa või None, kui sisestus on vale"
    def get_amount(self):
        try:
            return float(self.amount_entry.get())
        except ValueError:
            return None

    """Tagastab valitud valuutade koodid (näiteks 'EUR' ja 'USD')"""
    def get_selected_currencies(self):
        return self.from_currency.get(), self.to_currency.get()

    def update_result(self, result, currency):
        self.result_label.config(text=f"Tulemus: {result:.2f} {currency}" if result else "Viga")
