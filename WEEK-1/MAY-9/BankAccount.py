#This program is to understand the concept of OOPS 
#Creation of bank account,displaying the balance,withdrawing and depositing

class BankAccount: #Creating a class BankAccount
    def __init__(self,accno,accname,balance):  #Implementing a constructor and adding account details
        self.accno=accno 
        self.accname=accname
        self.balance=balance
    
    def deposit(self,amount): #Adding a deposit method to add the amount to the account
        self.balance+=amount 
        print("The new balance after adding the amount :",amount," in account number:",self.accno," account holder name :",self.accname,"is:",self.balance)

    def withdraw(self,amount):  #Adding a withdraw method to withdraw the amount from the account
        if amount>=self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount 
            print("The balance after withdrawing amount :",amount," in account number :",self.accno,"account holder name :",self.accname,"is:",self.balance)

    def showbalance(self): #Adding a method to display the account details
        print("Your Bank Account Deatils are :\n")
        print("Account Number:",self.accno,end="\n")
        print("Account Holder Name:",self.accname,end="\n")
        print("Current Balance:",self.balance)
    
def main(): #Main function to implement the BankAccount class
    print("******WELCOME TO ABM BANK*******")
    accno=int(input("Enter your account number:"))
    accname=input("Enter your account name:")
    balance=float(input("Enter your bank balance if you remember otherwise mark as 0:"))
    account=BankAccount(accno,accname,balance) #Creating an object of the class BankAccount

    choice=input("Enter 'c' to continue the bank operations or 'q' to exit from the application :")

    while True:
        if choice=='q':
            print("Exiting from the application.\n Thank You")
            break
        elif choice=='c': 
            print("The operations in the Bank are: \n")
            print("1.Deposit to your account \n")
            print("2.Withdraw from your account \n")
            print("3.Display the Bank Balance \n")
            ch=int(input("Enter your choice from 1-3 for performing the operations:"))
            if ch==1:
                print("DEPOSIT TO YOUR ACCOUNT \n")
                amount=float(input("Enter a positive value amount to deposit to your account:"))
                account.deposit(amount)
                choice=input("Please Enter 'c' to continue the bank operations or 'q' to exit from the application :")
            elif ch==2:
                print("WITHDRAWING FROM YOUR ACCOUNT \n")
                amt=float(input("Enter the amount to withdraw from your account:"))
                account.withdraw(amt)
                choice=input("Please Enter 'c' to continue the bank operations or 'q' to exit from the application :")
            elif ch==3:
                print("DISPLAYING YOUR ACCOUNT DETAILS")
                account.showbalance()
                choice=input("Please Enter 'c' to continue the bank operations or 'q' to exit from the application :")
            else:
                print("Enter valid choice")
if __name__=="__main__":
    main()
