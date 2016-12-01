class KCBBankAccount(object):
    def __init__(self, holder, number, actual_amount, minimum_balance=1000): 
        self._Holder = holder 
        self._Number = number                         # using _ to hide data (protect)
        self._actual_amount = actual_amount
        self._ minimum_balance= minimum_balance

    def deposit(self, amount): 
        self.actual_amount = amount # amount in your account after depositing

    def withdraw(self, amount): 
        if(self.actual_amount - amount < self.minimum_balance): # your bank requires that a minumum balance of ksh 1000 remains in your account
            
            return False  # so, if eg you have actual amount of 40,000 and you want to withdraw all of it, it becomes impossibe since no amount<1000
        else: 
            self.actual_amount -= amount #when the above condition is false, it means that you can withdraw 38,000 and below
            return True

    def actual_amount(self):          # This is the amount you will be left with after you successfully withdraw
        return self.actual_amount

    def transfer(self, target, amount):
    if(self.actual_amount - amount < self.minimum_balance):
            
            return False  
        else: 
            self.actual_amount -= amount 
            target.actual_amount += amount 
            return True