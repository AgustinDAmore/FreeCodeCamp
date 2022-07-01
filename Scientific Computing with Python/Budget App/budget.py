class Category:

    __slots__ = ["description", "ledger", "_balance"]

    def __init__(self, description):
        self.description = description
        self.ledger = []
        self._balance = 0.0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self._balance += amount

    def withdraw(self, amount, description=""):
        if self._balance - amount >= 0:
            self.ledger.append({"amount": -1 * amount, "description": description})
            self._balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self._balance

    def transfer(self, amount, category):
        if self.withdraw(amount, "Transfer to {}".format(category.description)):
            category.deposit(amount, "Transfer from {}".format(self.description))
            return True
        else:
            return False

    def check_funds(self, amount):
        if self._balance >= amount:
            return True
        else:
            return False

    def __repr__(self):
        header = self.description.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            ledger += line_description[:23] + line_amount[:7]+ "\n"
        total = "Total: {:.2f}".format(self._balance)
        return header + ledger + total