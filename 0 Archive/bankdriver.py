# Banking task by Lukasz Zlocki / 76103

# ToDo : refactor to dziedziczenie na bazie zadania covid itp.

import bankaccount
import pickle


# Show all accounts
def showAllAccounts(accounts_list):
    print("-- Listing all accounts --")

    for account in accounts_list:
      acc = account.get_accountNb()
      nam = account.get_name()
      bal = account.get_balance()
      print("** ** **")
      print("Account number :  ",acc)
      print("Owner name :  ",nam)
      print("Account balance :  ",bal)
      print("** ** **")

# Save data to file function
def saveData(FILENAME, accounts_list):
    print("Accounts list updated to file") 
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

# Create new account function
def createAccount(FILENAME, accounts_list):
    print("-- Creating account --")    
        
    # Get data from user
    accountNb = int(input('Account number : '))
    ownerName = input('Owner name : ')
    accountBalance = float(input('Account balance : '))

    # Create an object
    newAccount = bankaccount.BankAccount(accountBalance, ownerName, accountNb)
            
    # Add object to list of accounts
    accounts_list.append(newAccount)

    # Save accounts list to file
    saveData(FILENAME, accounts_list)

# Laad accounts from file
def loadAccounts(FILENAME, accounts_list):
    print("-- Loading accounts from data base --") 
    eof = False #End of file indicator

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

# Delete account function with withdraw all money
def deleteAccount(FILENAME, account_list):
    print("-- Delete account --")
    account_number = int(input("Account number to delete : ")) 
    id = 0
    for account in account_list: 
        if account.get_accountNb() == account_number:
            # ToDo : code to withdraw all money here.
            account_balance = account.get_balance()
            account.withdraw(account_balance)
            account_list.pop(id)   
            print("Account nb " + str(account_number) + " deleted.")        
        else:
            id = id +1                
    # Saving updated data
    saveData(FILENAME, account_list)

# Deposity money to account 
def deposit(FILENAME, account_list):
    print("-- Deposit to account --")  
    account_number = int(input("Account number to deposit : "))
    for account in account_list: 
        if account.get_accountNb() == account_number:
            depo = float(input("Amount to deposit : "))
            account.deposit(depo)
    # Saving updated data
    saveData(FILENAME, account_list)

# Withdraw money from account
def withdraw(FILENAME, account_list):
    print("-- Withdraw from account --")
    account_number = int(input("Account number to wihdraw : ")) 
    for account in account_list: 
        if account.get_accountNb() == account_number:
            balance = account.get_balance()
            print("Account balance: ", balance) 
            wdraw = float(input("Amount to withdraw : "))
            account.withdraw(wdraw)
    # Saving updated data
    saveData(FILENAME, account_list)



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
            
        # [E] - Exit.
        if user_selektor == 'E':
            exit_looper = True
 
# Call main function
if __name__ == "__main__":
    main()   