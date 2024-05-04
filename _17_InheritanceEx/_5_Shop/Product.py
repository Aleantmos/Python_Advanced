class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity_dec: int):
        if self.quantity >= quantity_dec:
            self.quantity -= quantity_dec

    def increase(self, quantity_inc: int):
        self.quantity += quantity_inc

    def __repr__(self):
        return self.name

