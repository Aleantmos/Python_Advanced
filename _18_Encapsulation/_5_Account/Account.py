class Account:
    def __init__(self, id, balance, pin):
        self.id = id
        self.balance = balance
        self.pin = pin

    def get_id(self, pin):
        if pin == self.pin:
            return self.id
        else:
            return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            return "Pin changed"
        else:
            return "Wrong pin"
