from bank_accounts import *

Dave = BankAccount(1000, 'Dave')
Sarah = BankAccount(2000, 'Sarah')

Dave.getBalance()
Sarah.getBalance()

Sarah.deposit(500)

Dave.withdraw(1500)
Dave.withdraw(100)

Dave.transfer(200, Sarah)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
print(Blaze.fee)
Blaze.transfer(1000, Sarah)