# Create a class named BankAccount that has the following attributes: account_number, balance, and owner_name. 
# It should also have methods called deposit() and withdraw() that update the balance accordingly.

class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = 100
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is deposited")

    def withdraw(self, amount):
        if (self.balance < amount):
            print("Insufficient funds.")
    
        else:
            self.balance -= amount
            print(f"{amount} is withdrawn from account")
    

    def newbalance(self):
        print(self.balance,"is the end balance of", self.owner_name, "account number", self.account_number)

account = BankAccount("LV.....",100,"Natalja Knazeva")
account.deposit(150)
account.withdraw(90)
account.newbalance()   

