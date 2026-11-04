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

    def transfer(self,amount,account):
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

# creating an interest account which will have all the accounts props plus it will have an altered version of deposit
# using inheritence 
class InterestRewardsAcc(BankSystem):
    def deposit(self, amount):
        self.validTransction(amount)
        self.balance=self.balance+(amount*1.05)
        print(f"Deposit complete new balance:{self.balance}")

            
# now creating a saving account this will inherit from InterestRewardsAcc so it will get 5% everytime when a deposit is made but also will pay fee of 5 RS when ever a withdrawal is made


class SavingsAcc(InterestRewardsAcc):
    
    def __init__(self, initialamount, accountname):
        super().__init__(initialamount,accountname)
        self.fee=5
    def withdraw(self, amount):
        try:
            self.validTransction(amount)
            self.balance=self.balance-amount
            self.getBalance()

        except BalanceException as error:
            print(f"Saving account error!{error}")






# 
#  
# acc1=BankSystem(2000,"Usama")
# acc2=BankSystem(2000,"manan")
# acc3=BankSystem(2000,"hamad")
# acc4=BankSystem(2000,"abbas")
# # print(acc1.balance)
# acc1.accountBalance()

#CNIC
#TRANSACTIONS HISTORY
#CARD  



