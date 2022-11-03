class Cuenta():

    def __init__(self, nombre, balance, balance_min):

        self.nombre = nombre
        self.balance = balance
        self.balance_min = balance_min

    
    def deposito(self, monto):

        self.balance += monto

    def retiro(self, monto):

        if self.balance - monto >= self.balance_min:
            self.balance -= monto
        else:
            print("Saldo insuficiente.")

    def declaracion(self):
        print(f"Tu saldo es: ${self.balance}")


class Corriente(Cuenta):

    def __init__(self, nombre, balance):

        super().__init__(nombre, balance, balance_min = -1000)


    def __str__(self):
        return f"Cuenta corriente de {self.nombre} - Balance: ${self.balance}"


class Ahorro(Cuenta):

    def __init__(self, nombre, balance):

        super().__init__(nombre, balance, balance_min=0)

    def __str__(self):
        return f"Cuenta de ahorro de {self.nombre} - Balance: ${self.balance}"


t = Ahorro("Tomas", 400)
t.deposito(5000)
t.retiro(3000)
t.declaracion()
t.retiro(3000)
print(t)