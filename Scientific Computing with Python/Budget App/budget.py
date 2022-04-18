class Category():

    __slots__ = ["ledger","amount","nameCategory","disenio"]

    def __init__(self,nameCategory,amount=0):
        self.nameCategory = nameCategory
        self.disenio = (len("initial deposit") + len(str(self.agregarDosDecimales(amount)))) - len(self.nameCategory)+1
        self.amount = 0
        self.ledger = {"amount":[],"description":[]}
        self.deposit(amount,"initial deposit")

        return None
    
    def deposit(self,amount,description=""):
        assert amount>0, "El monto ingresado tiene que ser positivo"

        if (len(description) + len(str(self.agregarDosDecimales(amount))))  - len(self.nameCategory)+1 > self.disenio:
            self.disenio = (len(description) + len(str(self.agregarDosDecimales(amount))))  - len(self.nameCategory)+1

        self.ledger["amount"].append(self.agregarDosDecimales(amount))
        self.ledger["description"].append(description)
        self.amount += amount

    def withdraw(self,amount,description):
        assert amount<0, "El monto ingresado tiene que ser negativo"
        if self.check_funds(amount):
        
            if (len(description) + len(str(self.agregarDosDecimales(amount))))  - len(self.nameCategory)+1 > self.disenio:
                self.disenio = (len(description) + len(str(self.agregarDosDecimales(amount)))) - len(self.nameCategory)+1

            self.ledger["amount"].append(self.agregarDosDecimales(amount))
            self.ledger["description"].append(description)
            self.amount += amount
            return True
        else:
            return False

    def transfer(self,amount,otraCategoria):
        assert amount>0, "El monto ingresado tiene que ser positivo"
        if self.check_funds(-amount):

            if (len(otraCategoria.nameCategory) + len(str(self.agregarDosDecimales(amount)))) - len(self.nameCategory)+1 > self.disenio:
                self.disenio = (len(otraCategoria.nameCategory) + len(str(self.agregarDosDecimales(amount)))) - len(self.nameCategory)+1

            self.withdraw(-amount,f"Transfer to {otraCategoria.nameCategory}")
            otraCategoria.deposit(amount,f"Transfer from {self.nameCategory}")

    def get_balance(self):
        return self.amount

    def check_funds(self,montoAGastar):
        bool =  True if (self.amount + montoAGastar) >= 0 else False
        return bool
    
    def agregarDosDecimales(self,amount):
        amount = (amount) if "." in str(amount) else (str(amount)+".00")
        return amount

#   print(description[i]+" "+" "*((self.disenio)-(len(description[i]))-(len(str(amount[i]))+1)//2)+str(amount[i]))


    def __repr__(self):
        description = self.ledger["description"]
        amount = self.ledger["amount"]
        print("*"*((self.disenio//2)) + self.nameCategory + "*"*((self.disenio//2)))
        for i in range(len(description)):
            print(description[i]+" "*((self.disenio + len(self.nameCategory))-(len(description[i]) + len(str(amount[i])) + 1)),amount[i])
        print(f"Total: {self.amount}")
        return ""


Food = Category("Food",1000)
Clothing = Category("Clothing",1)

Food.withdraw(-10.15,"groceries")
Food.withdraw(-15.89,"restaurant and more foo")
Food.transfer(50,Clothing)

print(Food)
print(Clothing)