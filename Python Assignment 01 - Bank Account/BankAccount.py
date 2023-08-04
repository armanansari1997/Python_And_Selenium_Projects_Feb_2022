class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """

    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.deposit_ls = [0]
        self.withdraw_ls = [0]
        self.fees_ls = [0]
        self.balance = initial_balance
        self.withdraw_count = 0

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.deposit_ls.append(amount)
        self.balance += self.deposit_ls[-1]

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.withdraw_count += 1
        if self.withdraw_count <= 5:
            if (self.balance - amount) < 0:
                self.withdraw_ls.append(amount)
                self.fees_ls.append(5)
                self.balance -= (self.withdraw_ls[-1] + self.fees_ls[-1])

            elif (self.balance - amount) >= 0:
                self.withdraw_ls.append(amount)
                self.balance -= (self.withdraw_ls[-1])
            else:
                pass
        else:
            raise Exception("Withdraw limit exceeded")

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return sum(self.fees_ls)
