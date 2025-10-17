# account:
# *balance
# *Name
# *ac_no
# *bank_name
# 1.get_balance()
# 2.deposit()
# 3.withdraw
# saving account
#interest rate
#calculate intrest
#
#
from abc import ABC, abstractmethod

# Abstraction
class BankService(ABC):
    @abstractmethod
    def transaction(self):
        pass

class account:
    bank_name="Phitron Bank"

    def __init__(self,name,account_name,balance):
        self.name=name
        self.accout_name=account_name
        self.__balance=balance#private attribute

    def get_balance(self):
        return self.__balance
    def deposit(self,money):
        self.__balance+=money
        return f"{money} is added , new Balance is :{self.__balance}"
    def withdraw(self,withDrawMoney):
        if withDrawMoney>self.__balance:
         return f"Insufficient Money"
        self.__balance-=withDrawMoney
        return f'{withDrawMoney} is Withdrawed,New balance is:{self.__balance}'
    

class SavingsAccount(account):
    def __init__(self,name,account_name,balance,interest_rate):
        super().__init__(name,account_name,balance)
        self.interest_rate=interest_rate

    def calculate_interest(self):
        interest=self.get_balance()*self.interest_rate/100
        return f'Interest rate is : {interest}'
    
class currentAccount(account):
    def __init__(self,name,account_name,balance,overlimit):
        super().__init__(name,account_name,balance)
        self.overlimit=overlimit

    def withdraw(self, withDrawMoney):
        if withDrawMoney>self.get_balance+self.overlimit:
            return f'Insufficient Balance'
        balance= self.get_balance()-withDrawMoney
        return f'{withDrawMoney} is withdrawed ,new balance is {balance}'

class ATM(BankService):
    def transaction(self):
        print("ATM Transaction: Cash Withdraw or balance Check")



currentUser=currentAccount("Arman",123,1000,500)
        

     