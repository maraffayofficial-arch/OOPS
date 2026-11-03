class BalanceException(Exception):
  pass

class BankSystem:
    def __init__(self,amount,employeeName):
        self.name=employeeName
        self.balance=amount
        # print(f"The current amount of {self.name} account is ${self.balance}")
    
    
    def getBalance(self):
        return print(f"Account:{self.name}\n Balance:{self.balance}")

    def deposit(self,amount):
        self.balance=self.balance+amount
        return print(f"Transaction successfull!!\nAccount:{self.name}\n Balance: ${self.balance}")
    
    def validTransction(self,amount):
        if self.balance>=amount:
            return 
            # print("validTransction 1")
        else:
            # print("validTransction 2")
            raise BalanceException(
                f"Sorry account:{self.name} has only balance:{self.balance:.2f} "
            )

    def withdraw(self,amount):
        try:
            self.validTransction(amount)
            print("withdraw 1")
            self.balance=self.balance-amount
            print("\nWithdrawal Complete")
            print(f"Balance:")
            self.getBalance()
          

        except BalanceException as error:
            
           print(f"withdraw interupted{error}")

    def transaction(self,amount,account):
        try:
            print("\n**********\n\nBegining Transfer...🚀🚀")
            self.validTransction(amount)
            # print("execution 1")
            account.deposit(amount)
            print(f"Amount transfered:{amount:.2f}")
            self.balance=self.balance-amount
            
            print(f"Transfer Complete..✅\nYour Balance:{self.balance:.2f}")
            # print("execution 2")
        except BalanceException as error:
            # print("execution 3")
            print(f"Transcation interupted{error}")




            

# acc1=BankSystem(2000,"Usama")
# acc2=BankSystem(2000,"manan")
# acc3=BankSystem(2000,"hamad")
# acc4=BankSystem(2000,"abbas")
# # print(acc1.balance)
# acc1.accountBalance()

#CNIC
#TRANSACTIONS HISTORY
#CARD  



