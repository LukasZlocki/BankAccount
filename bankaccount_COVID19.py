# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

# ToDo : Do kazdej klasy dodac typ konta(string)(przez override)

import bankaccount

class BankAccount_COVID19(bankaccount.BankAccount):
     # init superclass bankaccount
    def __init__(self, bal, na, acctnb, initdate):
        # init superclass
        bankaccount.BankAccount.__init__(self, bal, na, acctnb)