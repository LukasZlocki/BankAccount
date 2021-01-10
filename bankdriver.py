# Banking task by Lukasz Zlocki / 76103
# zlocki_76103@cloud.wsb.wroclaw.pl

import bankaccount
import bankaccount_STANDARD
import bankaccount_COMPANY
import bankaccount_INT
import pickle
from datetime import date

def testCreating(FILENAME, accounts_list):
    print("-- Creating TEST account STANDARD --")    
        
    # Get data from user
    accountNb = int(input('Account number : '))
    ownerName = input('Owner name : ')
    accountBalance = float(input('Account balance : '))
    # initdate = date.today()
    initdate = date(2018, 4, 3)

    # Create an object
    newAccount = bankaccount_STANDARD.BankAccount_STANDARD(accountBalance, ownerName, accountNb, initdate)
            
    # Add object to list of accounts
    accounts_list.append(newAccount)
    print("... Account added to list.")

    # Save accounts list to file
    saveData(FILENAME, accounts_list)


# Show all accounts
def showAllAccounts(accounts_list):
    print("-- Listing all accounts --")

    for account in accounts_list:
      acc = account.get_accountNb()
      nam = account.get_name()
      bal = account.get_balance()
      acctype = account.get_acctype()

      print("** ** **")
      print("Account number :  ",acc)
      print("Owner name :  ",nam)
      print("Account balance :  ",bal)
      print("Account type : ", acctype)
      print("** ** **")

# Save data to file function
def saveData(FILENAME, accounts_list):
    print("-- Savings accounts --")     
    # Opening file
    db_file = open(FILENAME, 'wb')  
    # Logic data for while loop
    loop = len(accounts_list)
    i = 0
    while not i == loop :   
        # Write i object to file
        pickle.dump(accounts_list[i], db_file)
        i = i + 1          
    # Close file
    db_file.close()
    print("... Accounts list updated to file.")
    print("...")
    print("..")
    print(".")

# Create new account function
def createAccount(FILENAME, accounts_list):
    print("-- Creating account --")    
    print("Implement an account type :")
    print("[C] - Company account.")
    print("[I] - International account.")
    print("[S] - Standard account.")
    
    _user_account = input('account type -> ')

    # Get data from user
    accountNb = int(input('Account number : '))
    ownerName = input('Owner name : ')
    accountBalance = float(input('Account balance : '))
    accountInitdate = date.today()

    if _user_account == 'C':
        # Create an COMPANY account object
        newAccount = bankaccount_COMPANY.BankAccount_COMPANY(accountBalance, ownerName, accountNb,accountInitdate) 
    if _user_account == 'I':
        # Create an INTERNATIONAL account object
        newAccount = bankaccount_INT.BankAccount_INT(accountBalance, ownerName, accountNb,accountInitdate) 
    if _user_account == 'S':
        # Create an STANDARD account object
        newAccount = bankaccount_STANDARD.BankAccount_STANDARD(accountBalance, ownerName, accountNb,accountInitdate) 
          
    # Add object to list of accounts
    accounts_list.append(newAccount)
    print("... Account added to list.")

    # Save accounts list to file
    saveData(FILENAME, accounts_list)

# Laad accounts from file
def loadAccounts(FILENAME, accounts_list):
    print("-- Loading accounts from data base --") 
    eof = False #End of file indicator
    try:
        # Open the binary file
        db_file = open(FILENAME, 'rb')
        # Reat up to the end of file
        while not eof:
            try:
                #Unpickle the next object
                account = pickle.load(db_file)
                accounts_list.append(account)
            except EOFError:
                # Set the flag of and of file
                eof = True
        # Close the file
        db_file.close()
        print("... Accounts loaded to list.")
    except:
        print("No file found. Create account first.")

# Delete account function with withdraw all money
def deleteAccount(FILENAME, accounts_list):
    print("-- Delete account --")
    _account_found = False
    _account_deleted = 0
    account_number = int(input("Account number to delete : ")) 
    id = 0
    for account in accounts_list: 
        if account.get_accountNb() == account_number:
            account.close(accounts_list, id)
           
            _account_found = True
            # Saving updated data
            saveData(FILENAME, accounts_list)        
        else:
            id = id +1
    if _account_found == False:
        print("No account number " + str(account_number) + " found.")               
    
# Deposity money to account 
def deposit(FILENAME, account_list):
    print("-- Deposit to account --") 
    _account_found = False
    account_number = int(input("Account number to deposit : "))
    for account in account_list: 
        if account.get_accountNb() == account_number:
            depo = float(input("Amount to deposit : "))
            account.deposit(depo)
            print("... Amount deposited to account.")
            _account_found = True
            # Saving updated data
            saveData(FILENAME, account_list)
    if _account_found == False:
        print("No account number " + str(account_number) + " found.") 

# Withdraw money from account
def withdraw(FILENAME, account_list):
    print("-- Withdraw from account --")
    _account_found = False
    account_number = int(input("Account number to wihdraw : ")) 
    for account in account_list: 
        if account.get_accountNb() == account_number:
            balance = account.get_balance()
            print("Account balance: ", balance) 
            wdraw = float(input("Amount to withdraw : "))
            account.withdraw(wdraw)
            # Saving updated data
            saveData(FILENAME, account_list)
    if _account_found == False:
        print("No account number " + str(account_number) + " found.")

# main function
def main():
    exit_looper = False
    accounts_list = []

    FILENAME = "accountDb.dat"

    while exit_looper == False:
        user_selektor = ""

        # Menu area
        print("-- LukasBankAccount --")
        print("Records in data base :",len(accounts_list))
        print("Choose action :")
        print("[C] - Create new account.")
        print("[D] - Delete account.")
        print("[DEP] - Deposit money to account.")
        print("[WDR] - Withdraw money from account.")
        print("[L] - List of all accounts.")
        print("[R] - Read data from file.")
        print("[W] - Write data to file.")
        print("[TEST] - Create : Test Covid19 firma")
        print("[E] - Exit.")
        user_selektor = input('Your command -> ')

        # User select area
        # [C] - Create new account.
        if user_selektor == 'C':
            createAccount(FILENAME, accounts_list)

        # [D] - Delete account.
        if user_selektor == 'D':
            deleteAccount(FILENAME, accounts_list)            

        # [DEP] - Deposit money to account.
        if user_selektor == 'DEP':
            deposit(FILENAME, accounts_list)

        # [WDR] - Withdraw money from account..
        if user_selektor == 'WDR':
            withdraw(FILENAME, accounts_list)    
            
        # [L] - List of accounts.
        if user_selektor == 'L':
            showAllAccounts(accounts_list)
            
        #[R] - Read data from file.
        if user_selektor == 'R':
            loadAccounts(FILENAME, accounts_list)
            
        # [W] - Write data to file.
        if user_selektor == 'W':
            saveData(FILENAME, accounts_list)

        # [TEST] - Create : Test Covid19 firma
        if user_selektor == 'TEST':
            testCreating(FILENAME, accounts_list)  

        # [E] - Exit.
        if user_selektor == 'E':
            exit_looper = True
 
# Call main function
if __name__ == "__main__":
    main()   