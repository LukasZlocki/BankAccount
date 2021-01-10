# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

# ToDo : Do kazdej klasy dodac typ konta(string)(przez override)
# ToDo : Limit wyplaty 1k pln tylko w okresie covid 01.04.2019

import bankaccount

class BankAccount_STANDARD(bankaccount.BankAccount):
     # init superclass bankaccount
    def __init__(self, bal, na, acctnb, initdate):
        # init superclass
        bankaccount.BankAccount.__init__(self, bal, na, acctnb)

        # init date attribute
        self.__initdate = initdate
        self.__acctype = "Standard bank account"


    # -- Overrided methods --

    # Get account type
    def get_acctype(self):
        return self.__acctype
    
     # The withdraw method withdraws an amount from the account.
    # (Overrided) Covid19 rule : withdraw not more than 1 k pln
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
            
            

    