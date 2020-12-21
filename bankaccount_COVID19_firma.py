# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

# ToDo : bezzwrotna pozycza 5k pln przy zalozeniu konta / done Check it 
# ToDo : Brak mozliwosci skasowania konta (Overide : close) / done Check it 
# ToDo : brak mozliwosci wyplaty wiecej niz 1 k pln (override : withdraw) / done Check it 

import bankaccount

class BankAccount_COVID19_firma(bankaccount.BankAccount):
    # init superclass bankaccount
    def __init__(self, bal, na, acctnb, initdate):
        # 5k grand for company from government
        bal = bal + 5000
        # init superclass
        bankaccount.BankAccount.__init__(self, bal, na, acctnb)
   
        # init date attribute
        self.__initdate = initdate
        self.__acctype = "Covid19 firma bank account"


    # -- Overrided methods --

    # Get account type
    def get_acctype(self):
        return self.__acctype
    
    # The withdraw method withdraws an amount
    # from the account.
    def withdraw(self, amount):
        if amount > 1000 :
            print("Too large amount of money. Withdraw max 1000 pln")
        else :
            if self.__balance >= amount:
                print("Amount to withdraw : ", amount)
                self.__balance -= amount
                print("... Amount withdrawn.")
            else:
                print('Error: Insufficient funds')

    # The close method is closing account by
    # -> withdraw all money
    # -> deleting this object (BankAccount)
    def close(self, account_number):
        print('Deleting company account not allowed')    