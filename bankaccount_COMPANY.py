# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

# ToDo : bezzwrotna pozycza 5k pln przy zalozeniu konta / done & checked with date
# ToDo : Brak mozliwosci skasowania konta (Overide : close) / done & checked
# ToDo : brak mozliwosci wyplaty wiecej niz 1 k pln (override : withdraw) / done & checked

import bankaccount
from datetime import date

class BankAccount_COMPANY(bankaccount.BankAccount):
    # init superclass bankaccount
    def __init__(self, bal, na, acctnb, initdate):

        # Covid19 Rules : from 01.04.2019 +1 k PLN init loan for all COMPANY accounts.
        covid19_loan_date = date(2019, 4, 1)
        if initdate >= covid19_loan_date:
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

    # The close method is closing account 
    # (Overrided) -> this method is not closing account 
    def close(self, accounts_list, id):
        print('Deleting company account not allowed')
       