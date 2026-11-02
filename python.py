class BalanceException(Exception):
  pass

class BankSystem:
    def __init__(self,amount,employeeName):
        self.name=employeeName
        self.balance=amount
        print(f"The current amount of {self.name} account is ${self.balance}")
    
    
    def getBalance(self):
        return print(self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount
        return print(f"Transaction successfull!!\n Balance: ${self.balance}")
    
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
            print(error)
            f"Sorry account:{self.name} has only balance:{self.balance:.2f}"

            

# acc1=BankSystem(2000,"Usama")
# acc2=BankSystem(2000,"manan")
# acc3=BankSystem(2000,"hamad")
# acc4=BankSystem(2000,"abbas")
# # print(acc1.balance)
# acc1.accountBalance()

#CNIC
#TRANSACTIONS HISTORY
#CARD  



