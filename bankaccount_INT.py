# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

# ToDo : Do kazdej klasy dodac typ konta(string)(przez override) / done & checked
# ToDo : Brak limitu wyplaty - override : withdraw / done & checked

import bankaccount

class BankAccount_INT(bankaccount.BankAccount):
    # init superclass bankaccount
    def __init__(self, bal, na, acctnb, initdate):
        # init superclass
        bankaccount.BankAccount.__init__(self, bal, na, acctnb)

        # init date attribute
        self.__initdate = initdate
        self.__acctype = "International bank account"


    # -- Overrided methods --

    # Get account type
    def get_acctype(self):
        return self.__acctype

 
