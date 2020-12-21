# The BankAccount class simulates a bank account.

class BankAccount:

    # The __init__ method accepts an argument for
    # the account's balance. It is assigned to
    # the __balance attribute.

    # ! ToDo : !  dodac jako parametr date twprzenia konta (cos jak DateTime.now)
    def __init__(self, bal, na, acctnb):
        self.__balance = bal
        self.__name = na
        self.__acct_nb = acctnb

    # The deposit method makes a deposit into the
    # account.

    def deposit(self, amount):
        self.__balance += amount

    # The withdraw method withdraws an amount
    # from the account.
    def withdraw(self, amount):
        if amount > 1000 :
            print("Za duza kwota pobrania. Pobierz max 1000")
        else :
            if self.__balance >= amount:
                print("Amount to withdraw : ", amount)
                self.__balance -= amount
                print("Amount withdrawn.")
            else:
                print('Error: Insufficient funds')

    # The close method is closing account by
    # -> withdraw all money
    # -> deleting this object (BankAccount)

    def close(self, account_number):
        zero_balance = self.__balance
        self.withdraw(zero_balance)
        del self

    # The print_all method returns all class fields
    def print__all(self):
        print("Account number : ", self.__acct_nb)
        print("Owner name : ", self.__name)
        print("Account balance : ", self.__balance)

    # GETTERS

    def get_balance(self):
        return self.__balance
    
    def get_name(self):
        return self.__name
    
    def get_accountNb(self):
        return self.__acct_nb
    



