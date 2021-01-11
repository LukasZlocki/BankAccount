# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

# The BankAccount class simulates a bank account.

class BankAccount:

    # The __init__ method accepts an argument for
    # the account's balance. It is assigned to
    # the __balance attribute.

    # ! ToDo : !  dodac jako parametr date tworzenia konta (cos jak DateTime.now)
    def __init__(self, bal, na, acctnb):
        self.__balance = bal
        self.__name = na
        self.__acct_nb = acctnb
        self.__acctype = "Regular bank account"

    # The deposit method makes a deposit into the
    # account.
    def deposit(self, amount):
        self.__balance += amount

    # The withdraw method withdraws an amount
    # from the account ! without any limits !
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("... Amount withdrawn.")
        else:
            print('Error: Insufficient funds')


    # The close method is closing account by
    # -> withdraw all money
    # -> deleting this object in accounts list
    def close(self, accounts_list, id):
        # Withdraw all money here.
        zero_balance = self.__balance
        self.withdraw(zero_balance)

        # Removing account from account list
        accounts_list.pop(id)
        print("... Account nb " + str(self.__acct_nb) + " deleted.")   
        

           
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

    # Get account type
    def get_acctype(self):
        return self.__acctype
    

    # SETTERS

    # set balance
    def set_balance(self, bal):
        self.__balance = bal

